from django.urls import path

from . import views

app_name = 'talk'

urlpatterns = [
    path('chap_bridge/<int:cn>/', views.chap_bridge, name='chap_bridge'),
    path('chap/<int:cn>/', views.chap, name="chap"),
    path('update/<int:rn>/', views.update_answer, name="update_answer"),
    path('chapter/49/', views.chapter49, name="chapter49"),
    path('chapter/50/', views.chapter50, name="chapter50"),
    path('write_last/', views.write_last, name="write_last"),
    path('address/', views.address, name="address"),
    path('final/', views.final, name="final"),
    path('chap5/', views.chap5, name="chap5"),
]
