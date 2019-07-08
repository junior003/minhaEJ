from django.db import models

# Create your models here.

class Membro(models.Model):
    STATUS_CHOICES = [
        ["T", "Trainee"],
        ["M", "Membro"],
        ["P", "Pós Júnior"]
    ]

    nome = models.CharField(max_length=20, null=False)
    cargo = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    def __unicode__(self):
                return self.nome