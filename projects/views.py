from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Projects
from .forms import ProjectForm
# Create your views here.


def project_list(request):
    return render(request, 'project/list.html', {
        'project_list': Projects.objects.all()
    })


def project_view(request, id):
    project = Projects.objects.get(pk=id)
    return HttpResponseRedirect(reverse('project_list'))


def add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_creator = form.cleaned_data['creator']
            new_created_on = form.cleaned_data['created_on']
            new_deadline = form.cleaned_data['deadline']
            new_description = form.cleaned_data['description']
            new_project_resources = form.cleaned_data['project_resources']

            new_project = Projects(
                name=new_name,
                creator=new_creator,
                created_on=new_created_on,
                deadline=new_deadline,
                description=new_description,
                project_resources=new_project_resources
            )
            new_project.save()
            return render(request, 'project/add.html', {
                'form': ProjectForm(),
                'success': True
            })
    else:
        form = ProjectForm()
    return render(request, 'project/add.html', {
        'form': ProjectForm()
    })
