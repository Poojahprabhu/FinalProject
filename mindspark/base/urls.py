
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/course/', views.course, name='course'),
    path('result/', views.result, name='result'),
    path('userregister/', views.userregister, name='userregister'),
    path('quiz/', views.quiz, name='quiz'),
    path('profile/', views.profile, name='profile'),
    path('home/', views.home, name='home')
]