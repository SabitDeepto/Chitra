from django import forms

from CRUD.models import Executive


class AmbassadorForm(forms.ModelForm):
    class Meta:
        model = Executive
        fields = ['ambassador_name', 'email', 'phone']