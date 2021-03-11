from django.contrib import admin
from .models import Symptom
from .models import Record
from .models import CancerImage
# Register your models here.
admin.site.register(Symptom)
admin.site.register(Record)
admin.site.register(CancerImage)
