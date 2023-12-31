from django.urls import path

from api.views import *


urlpatterns = [
    path('user/register/', register, name='register'),
    path('user/login/', login, name='login'),
    path('get_recipes/', get_recipes, name='get_recipes'),
    path('get_recipe/', get_recipe, name='get_recipe'),
    path('filter_recipes/', filter_recipes, name='filter_recipes'),
    path('all_fruit_info/', all_fruit_info, name='all_fruit_info'),
    path('fruit_info/', fruit_info, name='fruit_info'),
    path('get_questions/', get_questions, name='get_questions'),
    path('get_question/', get_question, name='get_question'),
    path('add_question/', add_question, name='add_question'),
    path('add_answer/', add_answer, name='add_answer'),
    path('fruit_detection/', fruit_detection, name='fruit_detection'),
]