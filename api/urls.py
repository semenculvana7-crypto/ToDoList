from rest_framework.routers import DefaultRouter

from .views import TaskViewSet, ProfileViewSet


router = DefaultRouter()

router.register('tasks', TaskViewSet, basename='task')
router.register('profiles', ProfileViewSet, basename='profile')

urlpatterns = router.urls