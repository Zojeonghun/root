from django import forms
from . import models

class SearchForm(forms.Form):
    location = forms.ModelChoiceField(required=False, empty_label='전체보기', queryset=models.Location.objects.all())
    name = forms.CharField(required=False)
    address_text = forms.CharField(required=False)

class WorkshopAdminForm(forms.ModelForm):
    class Meta:
        model = models.Workshop
        fields = [
            'name',
            'location',
            'address_text',
            'number',
            'link',
            'address_x',
            'address_y',
        ]
