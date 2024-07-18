from django_components import component
from uuid import uuid4

class LiveComponent(component.Component):

	def __init__(self, *args, **kwargs):
		key = kwargs.pop("key", None)
		self.session = kwargs.pop('session', None)

		super().__init__(*args, **kwargs)

		if 'outer_context' in kwargs:
			if 'request' in kwargs['outer_context']:
				self.session = kwargs['outer_context']['request'].session
		
		if not key:
			self.key = str(uuid4())
			if hasattr(self.__class__, "state"):
				self.session[self.key] = self.__class__.state 
				self.state = self.__class__.state
			else:
				self.session[self.key] = {}
				self.state = {}
			
			print(f"DIDNT HAVE KEY {self.key}", self.session[self.key])
		else:
			self.key = key
			self.state = self.session.get(self.key)


	def get_context_data(self, **kwargs):
		return {
			**self.state,
			**kwargs,
			"key": self.key,
			"registered_name": self.registered_name,
		}

	def _set_state(self, new_state):
		self.state = {**self.state, **new_state}
		self.session[self.key] = self.state
	
	def set_pule(self, **data):
		print("=== SET PULE ===")
		self._set_state({"pule": data["pule"]})