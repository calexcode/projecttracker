from django import forms
from .models import Projects


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['name', 'creator', 'created_on',
                  'deadline', 'description', 'project_resources']
        labels = {
            'name': 'Project Name',
            'creator': 'Created By',
            'created_on': 'Created On',
            'deadline': 'Deadline',
            'description': 'Description',
            'project_resources': 'Project Resources'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'creator': forms.TextInput(attrs={'class': 'form-control'}),
            'created_on': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'deadline': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'project_resources': forms.FileInput(attrs={'class': 'form-control'}),
        }
