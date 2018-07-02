from django import forms
from .models import *

class accessForm(forms.ModelForm):
    name = forms.CharField(label='name', max_length=250)
    employee_id = forms.IntegerField(label='id')
    project = forms.CharField(label='project', max_length=250)
    position =  forms.CharField(label='position', max_length=250)
    duration = forms.IntegerField(label='duration')
    access = forms.CharField(label='access', max_length=250)
    status = forms.CharField(max_length=250,required=False)


    class Meta():
        model = detail
        fields = ['name','employee_id','project','position','duration','access','status']
