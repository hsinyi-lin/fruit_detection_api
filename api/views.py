import hashlib, random, string

from django.core.mail import send_mail
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import AccountSerializer
from .models import *

from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def register(request):
    data = request.data

    if Account.objects.filter(email=data['email'].strip()).exists():
        return Response({'success': False, 'msg': '已註冊過帳號'})

    serializer = AccountSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    sha256 = hashlib.sha256()
    sha256.update(serializer.validated_data['password'].encode('utf-8'))
    password_hash = sha256.hexdigest()
    serializer.validated_data['password'] = password_hash
    serializer.save()

    return Response({'success': True, 'msg': '註冊成功'})


@api_view(['POST'])
def login(request):
    data = request.data
    email = data.get('email').strip()
    password = data.get('password').strip()

    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    password_hash = sha256.hexdigest()

    user = Account.objects.filter(email=email, password=password_hash)
    if not user.exists():
        return Response({'success': False, 'msg': '帳號或密碼錯誤'})

    user = user.first()

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    return Response({'success': True, 'message': '登入成功', 'access_token': access_token})


@api_view(['GET'])
def get_recipes(request):
    recipes = Recipe.objects.all()
    return Response({'success': True, 'data': recipes.values_list()})


@api_view(['GET'])
def get_recipes(request):
    recipes = Recipe.objects.all()
    return Response({'success': True, 'data': recipes.values_list()})


@api_view(['GET'])
def get_recipe(request):
    data = request.query_params
    recipe_id = data.get('id')

    recipe = Recipe.objects.get(id=recipe_id)

    return Response({ 'success': True, 'data': recipe.values_list()})

@api_view(['GET'])
def filter_recipes(request):
    data = request.query_params

    search_string = data.get('title')
    recipe = Recipe.objects.filter(title__icontains=search_string)

    return Response({'success': True,'data': recipe.values_list()})


@api_view(['GET'])
def all_fruit_info(request):
    fruits = Fruit.objects.all()

    return Response({'success': True,'data': fruits.values_list()})


@api_view(['GET'])
def fruit_info(request):
    data = request.query_params
    fruit_id = data.get('id')

    try:
        fruit = Fruit.objects.get(id=fruit_id)
    except:
        return Response({'success': False, 'msg': '查無資料'})

    return Response({'success': True, 'data': fruit.values_list()})


@api_view(['GET'])
def get_questions(request):
    questions = Question.objects.all()

    return Response({
        'success': True,
        'data': questions.values_list()
    })


@api_view(['GET'])
def get_question(request):
    data = request.query_params
    fruit_id = data.get('id')

    try:
        question = Question.objects.get(id=fruit_id)
    except:
        return Response({'success': False, 'msg': '查無資料'})

    answers = Answer.objects.filter(question=question)

    return Response({
        'success': True,
        'data': {
            'question': question.id,
            'title': question.title,
            'content': question.content,
            'email': question.email,
            'answers': answers.values_list()
        }
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_question(request):
    data = request.data

    title = data.get('title')
    content = data.get('content')
    email = request.user_id

    try:
        question = Question.objects.create(title=title, content=content, email_id=email)
    except:
        return Response({'success': False, 'msg': '請輸入完整'})

    return Response({'success': True, 'msg': '新增成功'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_answer(request):
    data = request.data

    question_id = data.get('question_id')
    email = request.user_id

    try:
        answer = Answer.objects.create(question_id=question_id, email_id=email)
    except:
        return Response({'success': False, 'msg': '請輸入完整'})

    return Response({'success': True, 'msg': '新增成功'})


