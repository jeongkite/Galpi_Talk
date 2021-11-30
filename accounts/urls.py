from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.done, name='signup'),
    path('login/', views.done, name='login'),
    path('logout/', views.done, name='logout'),
    path('start/', views.done, name='start'),
    path('', views.done, name='intro'),
    path('info/', views.done, name='info'),
    path('help/1/', views.done, name='help1'),
    path('help/2/', views.done, name='help2'),
    path('help/3/', views.done, name='help3'),
    path('help/4/', views.done, name='help4'),
    path('question/', views.done, name='question'),
    path('privacy/', views.done, name='privacy'),
]
