from tasks.models import *
from django import forms
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['tittle', 'description', 'completed']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'description', 'age']
