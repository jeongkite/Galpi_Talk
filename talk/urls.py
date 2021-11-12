from django.urls import path

from . import views

app_name = 'talk'

urlpatterns = [
    path('chap_bridge/<int:cn>/', views.chap_bridge, name='chap_bridge'),
    path('chap/<int:qn>/', views.chap, name="chap"),
]
