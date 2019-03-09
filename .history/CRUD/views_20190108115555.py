from django.shortcuts import redirect, render
from urllib3 import request

from CRUD.forms import ExecutiveForm
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
    form = ExecutiveForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'reg.html', {'form': form})

def update_executive(request, id):
    qs = Executive.objects.get(pk=id)
    form = ExecutiveForm(request.POST)
    return render()