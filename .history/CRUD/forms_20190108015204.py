from django import forms

from CRUD.models import CreateAmbassador


class AmbassadorForm(forms.ModelForm):
    class Meta:
        model = CreateAmbassador
        fields = ['ambassador_name', 'email', 'phone']