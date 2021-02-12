from django.db import models
from datetime import datetime    

# Create your models here.
class Symptom(models.Model):
    symptom = models.CharField(max_length=50)

    def __str__(self):
        return self.symptom

class Record(models.Model):
    symptoms=models.CharField(max_length=50)
    disease=models.CharField(max_length=50)
    dateTime=models.DateField(default=datetime.now(), blank=True)

    
