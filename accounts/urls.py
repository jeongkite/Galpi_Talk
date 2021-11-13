from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('start/', views.start, name='start'),
    path('', views.intro, name='intro'),
    path('info/', views.info, name='info'),
    path('help/1/', views.help1, name='help1'),
    path('help/2/', views.help2, name='help2'),
    path('help/3/', views.help3, name='help3'),
    path('help/4/', views.help4, name='help4'),
    path('question/', views.question, name='question'),
    path('privacy/', views.privacy, name='privacy'),
]
