from django.shortcuts import render
from .forms import ProfileForm

# Create your views here.


def form_1(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        x = form.cleaned_data.get('first_name')
        print(x)
    return render(request,'form_1.html', {'form':form})