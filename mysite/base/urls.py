from django.urls import path
from mysite.base import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('esqueci/', views.esqueci, name='esqueci'),
    path('senha_enviada/', views.senha_enviada, name='senha_enviada'),
]
