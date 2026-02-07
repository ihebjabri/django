from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    day = models.DateField(help_text="Date du repas")
    name = models.CharField(max_length=100)
    description = models.TextField()
    preparation_time = models.PositiveIntegerField(help_text="Temps en minutes", default=30)
    servings = models.PositiveIntegerField(help_text="Nombre de personnes", default=2)

    def __str__(self):
        return f"{self.name} ({self.day})"
