from django import forms
from django.core.exceptions import ValidationError
from .models import Aluno, Faculdade, Curso

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'ano_entrada', 'curso']
    

class FaculdadeForm(forms.ModelForm):
    class Meta:
        model = Faculdade
        fields = ['nome']

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if Faculdade.objects.filter(nome__iexact=nome).exists():
         
            raise ValidationError("Esta faculdade já existe!")
        return nome


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'faculdade']

    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get('nome')
        faculdade = cleaned_data.get('faculdade')

        if nome and faculdade:
            if Curso.objects.filter(nome__iexact=nome, faculdade=faculdade).exists():
                raise forms.ValidationError("Este curso já existe para a faculdade selecionada!")

        return cleaned_data