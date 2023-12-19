from django.urls import path
from . import views

app_name = 'minipjs'

urlpatterns = [
    path('', views.main, name='main'),
    path('calculator/', views.calculator, name='calculator'),
    path('naver_book/', views.naver_book, name='naver_book'),
]