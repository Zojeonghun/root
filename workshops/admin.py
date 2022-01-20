from django.contrib import admin
from . import models

@admin.register(models.Location)
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Workshop)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'address_text',
    )
    filter_horizontal = (
        'location',
    )
    list_filter = (
        'location',
    )

# Register your models here.
