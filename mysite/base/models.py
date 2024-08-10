from django.db import models
from django_min_custom_user.models import MinAbstractUser


class User(MinAbstractUser):
    pass


class Cadastro(models.Model):
    nome = models.CharField(
        verbose_name='Nome',
        max_length=64,
    )
    email = models.EmailField(
        verbose_name='Email',
    )
    senha = models.CharField(
        verbose_name='Senha',
        max_length=64,
    )
    idade = models.IntegerField(
        verbose_name='Idade',
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.nome)
