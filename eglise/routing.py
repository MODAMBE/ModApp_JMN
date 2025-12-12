from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"^ws/discussion/(?P<discussion_id>\w+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(r"^ws/appel/(?P<appel_id>\w+)/$", consumers.CallConsumer.as_asgi()),
]