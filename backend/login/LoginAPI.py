import os

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from django.contrib.auth import login, logout
from django.contrib.auth.models import User

from knox.views import LoginView, LogoutView, LogoutAllView
from knox.auth import TokenAuthentication
from knox.models import AuthToken


#API QUE CREA UN INICIO DE SESION CON LAS CREDENCIALES OPTENIDAS.
class LoginAPI(LoginView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        try:
            serializer = AuthTokenSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']

            login(request, user)

            response = super(LoginAPI, self).post(request, format=None)

            return response
        except:
            return Response(status = 400)