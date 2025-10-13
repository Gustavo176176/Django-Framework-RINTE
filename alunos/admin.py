from django.contrib import admin
from .models import Faculdade, Curso, Aluno

@admin.register(Faculdade) #registrar o modelo Faculdade no admin
class FaculdadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Curso)  #registrar o modelo Curso no admin
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'faculdade')
    search_fields = ('nome', 'faculdade__nome')

@admin.register(Aluno) #registrar o modelo Aluno no admin
class AlunoAdmin(admin.ModelAdmin): 
    list_display = ('nome', 'curso', 'ano_entrada', 'email')
    search_fields = ('nome', 'curso__nome', 'curso__faculdade__nome', 'email')


