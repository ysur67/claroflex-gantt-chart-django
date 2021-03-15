from django.conf.urls import include
from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('projects', views.ProjectViewSet, basename='projects')

urlpatterns = [
    path('', include(router.urls)),
]
