from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import IsOwner

# Create your views here.
class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = ['completed']
    search_fields = ['tittle']
    ordering_fields = ['tittle', 'completed']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)

class ProfileViewSet(ModelViewSet):
    serializer_class =  ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    filter_backends = [
        SearchFilter,
        OrderingFilter,
    ]

    search_fields = ['name']
    ordering_fields = ['name', 'age']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Profile.objects.filter(user = self.request.user)