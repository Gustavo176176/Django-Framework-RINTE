from django.contrib import admin
from .models import Faculdade, Curso, Aluno

@admin.register(Faculdade) 
class FaculdadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Curso) 
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'faculdade')
    search_fields = ('nome', 'faculdade__nome')

@admin.register(Aluno) 
class AlunoAdmin(admin.ModelAdmin): 
    list_display = ('nome', 'curso', 'ano_entrada', 'email')
    search_fields = ('nome', 'curso__nome', 'curso__faculdade__nome', 'email')


