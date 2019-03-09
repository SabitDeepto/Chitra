from builtins import object

from django.shortcuts import render
from urllib3 import request


# Create your views here.
def home(request):
    executive = Executive.objects.all
    templates = 'index.html'
    context = {
        'name': 'deepto'
    }
    return render(request, templates, context)