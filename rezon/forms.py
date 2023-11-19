from django import forms
from datetime import date
from dateutil.relativedelta import relativedelta
from .models import ModelFiscalStorage, FiscalStorage


class FiscalStorageCreate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['model_fiscal_storage'].empty_label = "Модель не выбрана"
        self.fields['validity'].initial = (date.today() + relativedelta(months=+15))

    class Meta:
        model = FiscalStorage
        fields = ['number', 'validity', 'model_fiscal_storage', 'other']
        widgets = {
            'validity': forms.DateInput(attrs={'type': 'date'}),
            'other': forms.Textarea(attrs={'cols': 30, 'rows': 5}),
        }
