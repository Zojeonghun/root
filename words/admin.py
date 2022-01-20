from django.contrib import admin
from . import models

@admin.register(models.Word)
class CustomUserAdmin(admin.ModelAdmin):
    pass