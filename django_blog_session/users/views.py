from rest_framework.views import APIView
from rest_framework.response import Response


class HelloWorld(APIView):

    def get(self, request):
        return Response("Hello World")


class HelloWorldTwo(APIView):
    def get(self, request):
        return Response("Today is Sunday. What a busy day.")
