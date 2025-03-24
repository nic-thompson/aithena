from django.urls import path
from .views import chat, chat_page

urlpatterns = [
    path('chat', chat, name='chat'),
    path("", chat_page, name="chat-ui"),
    path("api/chat", chat, name="chat"),
    path('', chat_page, name='chat-ui'),          # HTML page
    path('api/chat', chat, name='chat-endpoint'), # API
]

