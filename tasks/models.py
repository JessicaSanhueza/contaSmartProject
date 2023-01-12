from django.contrib.auth.models import User
from django.db import models

task_complejidad=[
    (1, 'Baja'),
    (2, 'Media'),
    (3, 'Alta')
]

class Categoria(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    code = models.CharField(max_length=48)
    def __str__(self):
        return self.title
class Subcategoria(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=48)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class Task(models.Model):
    title = models.CharField(max_length=100)
    complejidad = models.IntegerField(
        null=False, blank=False,
        choices=task_complejidad
    )
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '- by ' + self.user.username
class Solicitud(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=False)
    datecompleted = models.DateTimeField(null=True, blank=True)
    requerimiento = models.ForeignKey(Task, on_delete=models.CASCADE)