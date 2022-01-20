from django.shortcuts import render
from projects.models import Project

def project_index(request):
    context = {'projects': Project.objects.all()}
    return render(request, 'project_index.html', context)

""" With the projects that I have here, a demo is more appropiate than a descriptive page. This is beyond my current abillity.
def project_detail(request, pk):
    context = {'project': Project.objects.get(pk=pk)}
    return render(request, 'project_detail.html', context) """