from django.shortcuts import render
from urllib3 import request


# Create your views here.
def home(request):
    executive = Executive.
    templates = 'index.html'
    context = {
        'name': 'deepto'
    }
    return render(request, templates, context)