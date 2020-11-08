from django.db import models

# Create your models here.
class Symptom(models.Model):
    symptom = models.CharField(max_length=50)

    def __str__(self):
        return self.symptom