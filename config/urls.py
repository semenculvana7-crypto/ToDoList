"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from django.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from tasks.views import (
    TaskListView,
    TaskCreateView,
    TaskDetailView,
    TaskDeleteView,
    TaskUpdateView, UserCreateView, UserLoginView, UserLogoutView, ProfileDetailView, ProfileCreateView
)

urlpatterns = [
    path('api/token/', obtain_auth_token),
    path('admin/', admin.site.urls),
    path('',TaskListView.as_view(), name = 'task-list'),
    path('task/<int:pk>/',TaskDetailView.as_view(), name = 'task-detail'),
    path('task/create',TaskCreateView.as_view(), name = 'task-create'),
    path('task/<int:pk>/delete',TaskDeleteView.as_view(), name = 'task-delete'),
    path('task/<int:pk>/update',TaskUpdateView.as_view(), name = 'task-update'),
    path('register/', UserCreateView.as_view(), name= 'register'),
    path('login/', UserLoginView.as_view(), name= 'login'),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path('user/<int:pk>/profile',ProfileDetailView.as_view(), name = 'profile'),
    path('user/profile/create', ProfileCreateView.as_view(), name= 'profile-create'),
    path('api/', include('api.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
    'api/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
),
]
