from django.shortcuts import render
from .forms import ProfileForm

# Create your views here.


def form_1(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        form.save()
        return
    return render(request,'form_1.html', {'form':form})