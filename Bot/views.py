from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Bot.service import chat_with_echo_bot


class EchoChat(APIView):
    def post(self, request):
        try:
            data = request.data
            chat_with_echo_bot(data)
            response = "uploaded successfully"
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response("Failed", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
