from django.contrib import admin
from .models import Symptom
from .models import Record

# Register your models here.
admin.site.register(Symptom)
admin.site.register(Record)
