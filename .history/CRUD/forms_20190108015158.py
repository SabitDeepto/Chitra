from django import forms

from Manage_Ambassador.models import CreateAmbassador


class AmbassadorForm(forms.ModelForm):
    class Meta:
        model = CreateAmbassador
        fields = ['ambassador_name', 'email', 'phone']