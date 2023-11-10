import hashlib, random, string

from django.core.mail import send_mail
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.serializers import AccountSerializer
from .models import *


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    data = request.data

    if Account.objects.filter(email=data['email'].strip()).exists():
        return Response({
            'success': False,
            'msg': '已註冊過帳號'
        })

    serializer = AccountSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    sha256 = hashlib.sha256()
    sha256.update(serializer.validated_data['password'].encode('utf-8'))
    password_hash = sha256.hexdigest()
    serializer.validated_data['password'] = password_hash
    serializer.save()

    return Response({
        'success': True,
        'msg': '註冊成功'
    })