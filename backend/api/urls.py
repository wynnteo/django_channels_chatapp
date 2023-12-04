from django.urls import path
from .views import MessageList

urlpatterns = [
    path(
        "chat/<slug:room_name>/messages/", MessageList.as_view(), name="chat-messages"
    ),
]
