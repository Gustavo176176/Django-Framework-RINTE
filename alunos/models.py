from django.db import models  #criar modelo de dados


class Faculdade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    faculdade = models.ForeignKey(Faculdade, on_delete=models.CASCADE)  #se uma faculdade for eliminada,apaga os cursos relacionados.

    def __str__(self):
        return f"{self.nome} ({self.faculdade.nome})"

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    ano_entrada = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)  #se um curso for eliminado,apaga os alunos relacionados. 

    def __str__(self):
        return self.nome


