from django.urls import path

from . import views

app_name = 'talk'

urlpatterns = [
    path('chap_bridge/<int:cn>/', views.chap_bridge, name='chap_bridge'),
    path('chap/<int:qn>/', views.chap, name="chap"),
    path('update/<int:rn>/', views.update_answer, name="update_answer"),
    path('chapter/50/', views.chapter50, name="chapter50"),
    path('chapter/51/', views.chapter51, name="chapter51"),

]
