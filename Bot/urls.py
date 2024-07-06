from django.urls import path

from Bot.views import EchoChat

urlpatterns = [
    path('bot/', EchoChat.as_view()),
]
