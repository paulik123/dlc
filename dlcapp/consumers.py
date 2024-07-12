from channels.generic.websocket import AsyncWebsocketConsumer
import json

class DLCConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		self.group_name = "dlc_" + self.scope["url_route"]["kwargs"]["group_name"]
		await self.channel_layer.group_add(self.group_name, self.channel_name)
		print(111111111111)
		await self.accept()

	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		print(text_data_json)

	async def disconnect(self, close_code):
		print("DISCONNECT")
		await self.channel_layer.group_discard(self.group_name, self.channel_name)