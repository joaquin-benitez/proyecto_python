from django.shortcuts import render
from .models import Hamburguesa

def hamburguesas_list(request):
    hamburguesas = Hamburguesa.objects.all()
    return render(request, 'hamburguesas_list.html', {'hamburguesas': hamburguesas})
