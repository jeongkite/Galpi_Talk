from django.urls import path

from . import views

app_name = 'talk'

urlpatterns = [
    path('chap_bridge/<int:cn>/', views.done, name='chap_bridge'),
    path('chap/<int:cn>/', views.done, name="chap"),
    path('update/<int:rn>/', views.done, name="update_answer"),
    path('chapter/49/', views.done, name="chapter49"),
    path('chapter/50/', views.done, name="chapter50"),
    path('write_last/', views.done, name="write_last"),
    path('address/', views.done, name="address"),
    path('final/', views.done, name="final"),
    path('chap5/', views.done, name="chap5"),
    path('done/', views.done, name='done'),
]
