from django.urls import path

from api.views import *


urlpatterns = [
    path('user/register/', register, name='register'),
]