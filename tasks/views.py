from django.shortcuts import render
from rest_framework.reverse import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from tasks.forms import *
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)


from tasks.models import *
# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task-list.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task-detail.html'
    context_object_name = 'task'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task-create.html'
    success_url = reverse_lazy('task-list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task-update.html'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task-delete.html'
    success_url = reverse_lazy('task-list')

class UserCreateView(CreateView):
    model = User
    template_name = 'authentication/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('task-list')

class UserLoginView(LoginView):
    template_name = 'authentication/login.html'
    next_page = ''

class UserLogoutView(LogoutView):
    next_page = 'login'
