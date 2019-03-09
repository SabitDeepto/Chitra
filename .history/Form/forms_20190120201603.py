from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': "form-control", 'placeholder': "your first name", 'type': "text"}),
            ,
            'last_name': forms.TextInput(
                attrs={'class': "form-control", 'placeholder': "your first name", 'type': "text"}),
            ,
        }
