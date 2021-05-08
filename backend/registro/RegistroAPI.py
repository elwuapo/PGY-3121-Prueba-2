from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from django.contrib.auth.models import User

from knox.models import AuthToken


#API QUE VALIDA LOS DATOS Y VERIFICA QUE NO EXISTA PREVIAMENTE.
class ValidationAPI(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        try:
            data = request.data

            username = data['username']
            email = data['email']
            password1 = data['password1']
            password2 = data['password2']

            if(User.objects.filter(username = username).exists()):
                errorUsername = True
            else:
                errorUsername = False

            if(User.objects.filter(email = email).exists()):
                errorEmail = True
            else:
                errorEmail = False

            if(password1 != password2):
                errorPassword = True
            else:
                errorPassword = False

            return Response({ "errorUsername": errorUsername, "errorEmail": errorEmail, "errorPassword": errorPassword }, status=200)
        except:
            return Response(status = 400)

#API QUE REGISTRA AL NUEVO USUARIO.
class RegisterAPI(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        try:
            data = request.data

            username = data['username']
            email = data['email']
            password = data['password']

            usuario = User.objects.create_user(username = username, email = email, password = password)
            usuario.save()

            token = AuthToken.objects.create(usuario)[1]

            return Response({"user": usuario.username, "token": token}, status=201)
        except:
            return Response(status = 400)