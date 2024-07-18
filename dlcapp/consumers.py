from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django_components.component_registry import registry
from django_components.component import Component

class DLCConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		self.group_name = "dlc_" + self.scope["url_route"]["kwargs"]["group_name"]
		await self.channel_layer.group_add(self.group_name, self.channel_name)
		await self.accept()

	async def receive(self, text_data):
		data = json.loads(text_data)
		Cmp = registry.get(name=data['registered_name'])

		component = Cmp(
			registered_name=data['registered_name'],
			key=data['key'], 
			session=self.scope['session'],
		)
		getattr(component, data['method'])(**data)

		await self.send(
			text_data=component.render(
				getattr(component, "get_context_data")(**data)
			)
		)

	async def disconnect(self, close_code):
		print("DISCONNECT")
		await self.channel_layer.group_discard(self.group_name, self.channel_name)