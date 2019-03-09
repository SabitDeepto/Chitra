from django import forms

from CRUD.models import Executive


class ExecutiveForm(forms.ModelForm):
    class Meta:
        model = Executive
        fields = ['name', 'is_executive', 'registration_date', ]