from django_components import component
from dlcapp.components import LiveComponent
from uuid import uuid4

@component.register("text")
class LiveText(LiveComponent):
	template_name = "text.html"
	state = {
		"pule": ""
	}

	def set_pule(self, **data):
		self._set_state({
			"pule": data["pule"]
		})
