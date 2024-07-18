from django.urls import re_path
from dlcapp.consumers import DLCConsumer

websocket_urlpatterns = [
    re_path(r"ws/dlc/(?P<group_name>\w+)/$", DLCConsumer.as_asgi()),
]