from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('start/', views.start, name='start'),
    path('intro/', views.intro, name='intro'),
    path('info/', views.info, name='info'),
    path('question/', views.question, name='question'),
    path('privacy/', views.create_privacy, name='create_privacy'),
    path('privacy/update/', views.update_privacy, name='update_privacy'),
]
