from django.shortcuts import render

# Create your views here.


def form_1(request):
    form = ProfileForm(request.POST)
    return render(request,'form_1.html')