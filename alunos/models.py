from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date 
from django.db.models import UniqueConstraint 


class Faculdade(models.Model):
    nome = models.CharField(max_length=100, unique=True) 
    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)

    faculdade = models.ForeignKey(Faculdade, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        
        
        constraints = [
            UniqueConstraint(
                fields=['nome', 'faculdade'], 
                name='unique_nome_faculdade',
              
                violation_error_message='Este curso já existe para a faculdade selecionada!', 
            )
        ]
        
    def __str__(self):
        return f"{self.nome} ({self.faculdade.nome})"


class Aluno(models.Model):
    
    nome = models.CharField(max_length=100) 
    
    email = models.EmailField(
        unique=True, 
        error_messages={
            'required': 'Por favor, insira um endereço de email.',
            'unique': 'Este email já está registado no sistema.' 
        }
    )
    ano_entrada = models.PositiveIntegerField(validators=[
        MinValueValidator(1900, message="O ano de entrada deve ser válido."),
        MaxValueValidator(date.today().year + 1, message=f"O ano de entrada não pode ser maior que {date.today().year}.")
    ])
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nome} - {self.email}"