from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.template.loader import render_to_string
from django.http import Http404

from projects.models import Project, ProjectTask
from projects.serializers import ProjectSerializer, ProjectTaskSerializer


class ProjectListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(deleted=False).prefetch_related('tasks')
        state = self.request.GET.get('state', None)
        qs = self.filter_by_state(qs, state)
        return qs

    def filter_by_state(self, qs, state):
        user = self.request.user 
        if state == 'closed':
            return qs.filter(Q(completed_at__isnull=False) & Q(user_created=user))
        elif state == 'member':
            return qs.filter(Q(completed_at__isnull=True) & Q(tasks__user=user)).distinct()
        elif state == 'member_closed':
            return qs.filter(Q(completed_at__isnull=False) & Q(tasks__user=user)).distinct()

        return qs.filter(user_created=user)


class ProjectDetailView(DetailView):
    model = Project


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(methods=['POST'], detail=True, url_path='delete')
    def delete_project(self, *args, **kwargs):
        obj = self.get_object()
        obj.deleted = True
        obj.save()
        return Response({})

    @action(methods=['POST'], detail=True, url_path='close')
    def close_project(self, *args, **kwargs):
        obj = self.get_object()
        obj.close()
        return Response({})

    @action(methods=['POST'], detail=True, url_path='open')
    def open_project(self, *args, **kwargs):
        obj = self.get_object()
        obj.open()
        return Response({})


class ProjectTaskViewSet(generics.UpdateAPIView, viewsets.GenericViewSet):
    serializer_class = ProjectTaskSerializer
    queryset = ProjectTask.objects.all()

    @action(methods=['POST'], detail=True, url_path='close')
    def close(self, *args, **kwargs):
        obj = self.get_object()
        obj.close()
        return Response({})

    @action(methods=['POST'], detail=True, url_path='open')
    def open(self, *args, **kwargs):
        obj = self.get_object()
        obj.open()
        return Response({})
