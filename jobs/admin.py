from django.contrib import admin
from django.apps import apps
from .models import Job

# models = apps.get_models()
admin.site.register(Job)

# for model in models:
    # admin.site.register(model)
# Register your models here.