from django.shortcuts import render
from .forms import ProfileForm
from django.contrib import messages

# Create your views here.


def form_1(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Form submission successful')
    return render(request,'form_1.html', {'form':form})