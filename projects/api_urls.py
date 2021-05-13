from django.conf.urls import include
from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('projects', views.ProjectViewSet, basename='projects')
router.register('project-tasks', views.ProjectTaskViewSet, basename='projects')
router.register('project-comments', views.ProjectCommentViewSet, basename='projects')
router.register('task-comments', views.TaskCommentViewSet, basename='projects')

urlpatterns = [
    path('', include(router.urls)),
]
