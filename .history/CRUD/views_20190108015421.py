from django.shortcuts import render
from urllib3 import request
from CRUD.models import Executive


# Create your views here.
def home(request):
    executive = Executive.objects.all()
    templates = 'index.html'
    context = {
        'name': 'deepto',
        'ex':executive
    }
    return render(request, templates, context)


def create_executive(request):
    