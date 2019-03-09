from django.shortcuts import redirect, render
from httplib2 import Response
from urllib3 import request

from CRUD.forms import ExecutiveForm
from CRUD.models import Executive


# Create your views here.
def home(request):
    executive = Executive.objects.all()
    templates = 'index.html'
    context = {

        'ex': executive
    }
    return render(request, templates, context)


def create_executive(request):
    form = ExecutiveForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'reg.html', {'form': form})


def update(request, id):
    qs = Executive.objects.get(pk=id)
    form = ExecutiveForm(request.POST or None, instance=qs)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'reg.html',  {'form': form})
