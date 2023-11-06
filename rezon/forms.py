from django import forms
from datetime import date
from .models import Corporation, Version


class AddCorporation(forms.ModelForm):
    class Meta:
        model = Corporation
        fields = '__all__'


class AddVersion(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


class EditCorporation(forms.ModelForm):
    class Meta:
        model = Corporation
        fields = '__all__'
