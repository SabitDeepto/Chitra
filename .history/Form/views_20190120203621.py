from django.shortcuts import render
from .forms import ProfileForm

# Create your views here.


def form_1(request):
    form = ProfileForm(request.POST)
    if form.request == 'POST':
        x = form.request.get('first_name')
        print(x)
    return render(request,'form_1.html', {'form':form})