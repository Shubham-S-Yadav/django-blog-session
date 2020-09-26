from rest_framework.generics import (GenericAPIView,
                                     CreateAPIView,
                                     ListAPIView)
from rest_framework.response import Response
from .serializers import (UserLoginSerializer,
                          UserSignUpSerializer
                          )
from .models import User


class UserSignUpAPIView(CreateAPIView):
    serializer_class = UserSignUpSerializer

    def post(self, request, *args, **kwargs):
        print("REQUEST DATA", request.data)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            obj = User.objects.get(email=request.data["email"])

            response_data = {
                "id": obj.id,
                "first_name": obj.first_name,
                "last_name": obj.last_name,
                "email": obj.email,
                "username": obj.username
            }
            return Response(response_data)
        else:
            return Response(serializer.errors)


class GetUserListView(ListAPIView):
    serializer_class = UserSignUpSerializer

    def get_queryset(self):
        return User.objects.filter(is_superuser=False)

    def get(self, request, *args, **kwargs):
        serializer = super().list(request, *args, **kwargs)
        print("SERIALIZER", serializer.data)
        return Response(serializer.data)


class UserLoginAPIView(GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        print("REQUEST DATA", request.data)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            obj = serializer.user

            response_data = {
                "id": obj.id,
                "first_name": obj.first_name,
                "last_name": obj.last_name,
                "email": obj.email,
                "username": obj.username
            }
            return Response(response_data)
        else:
            return Response(serializer.errors)