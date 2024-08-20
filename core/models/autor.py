from django.db import models

class Autor (models.Model):
    nome = models.CharField(max_length=100, default="")
    email = models.URLField(max_length=100, null=True)

    def __str__(self):
        return f"(#{self.id} {self.nome}"