from django import forms

from CRUD.models import Executive


class Form(forms.ModelForm):
    class Meta:
        model = Executive
        fields = ['ambassador_name', 'email', 'phone']