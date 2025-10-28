from django.urls import path
from . import views

urlpatterns = [path('inserir/', views.inserir_tudo, name='inserir_aluno'),]