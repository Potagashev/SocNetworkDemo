from django.shortcuts import render


def chats_list(request):
    return render(request, "chat/chats_list.html")


def chat_room(request, room_name):
    return render(request, "chat/chat_room.html", {"room_name": room_name})
