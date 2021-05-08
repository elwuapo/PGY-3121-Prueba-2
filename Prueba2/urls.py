"""Prueba2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from knox import views as KnoxViews 

from backend.login.LoginAPI import LoginAPI
from backend.registro.RegistroAPI import ValidationAPI, RegisterAPI

urlpatterns = [
    path('admin/', admin.site.urls),

    #SIGNUP
    path('api/v1/validation/all/', ValidationAPI.as_view()),
    path('api/v1/signup/', RegisterAPI.as_view()),

    # SIGNIN
    path('api/v1/signin/', LoginAPI.as_view()),

    # SIGNOUT
    path('api/v1/signout/', KnoxViews.LogoutView.as_view()),
    path('api/v1/signout/all/', KnoxViews.LogoutAllView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
