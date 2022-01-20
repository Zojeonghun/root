from django import forms
from django.db.models.query_utils import Q
from . import models

class SearchForm(forms.Form):

    category = forms.ModelChoiceField(required=False, queryset=models.Category.objects.all())
    title = forms.CharField(required=False)


class UpdateForm(forms.ModelForm):
    class Meta:
        model = models.Content
        fields = [
            'title',
            'description',
            'category',
        ]