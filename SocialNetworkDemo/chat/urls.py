from django.urls import path

from .views import chats_list, chat_room

urlpatterns = [
    path("", chats_list, name="chats_list"),
    path("<str:room_name>/", chat_room, name="chat_room"),
]
