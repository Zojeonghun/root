from django.contrib import admin
from . import models


@admin.register(models.Content)
class CustomUserAdmin(admin.ModelAdmin):
    filter_horizontal = (
        'category',
    )

    list_filter = (
        'category',
    )

@admin.register(models.Category)
class CustomUserAdmin(admin.ModelAdmin):
    pass