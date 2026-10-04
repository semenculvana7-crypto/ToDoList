from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View
from rest_framework.reverse import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from tasks.forms import *
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)


from tasks.models import *
# Create your views here.
class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'tasks/task-list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['has_profile'] = Profile.objects.filter(
            user=self.request.user
        ).exists()

        return context



class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task-detail.html'
    context_object_name = 'task'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task-create.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        messages.success(self.request, 'Задача создана!')
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task-update.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        messages.success(self.request, 'Задача изменена!')
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task-delete.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        messages.success(self.request, 'Задача удалена!')
        return super().form_valid(form)

class UserCreateView(CreateView):
    model = User
    template_name = 'authentication/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        messages.success(self.request, 'Вы зарегестрировались!')
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = 'authentication/login.html'
    next_page = ''

    def form_valid(self, form):
        messages.success(self.request, 'Вы вошли в аккаунт!')
        return super().form_valid(form)

class UserLogoutView(LogoutView):

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Вы успешно вышли из аккаунта.')

        logout(request)

        return redirect('login')

class ProfileDetailView(DetailView):
    template_name = 'tasks/profile.html'
    model = Profile
    context_object_name = 'profile'

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'tasks/profile-create.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        messages.success(self.request, 'Профиль создан!')
        form.instance.user = self.request.user
        return super().form_valid(form)

class LogoutView(View):

    def post(self, request):
        logout(request)

        messages.success(request, 'Вы успешно вышли из аккаунта.')

        return redirect('login')



