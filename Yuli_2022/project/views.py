from django.shortcuts import render
from .models import Prroject
# Create your views here.
# def project(request):
#     return render(request, 'project.html')

def project_index(request):
    projects = Prroject.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Prroject.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)