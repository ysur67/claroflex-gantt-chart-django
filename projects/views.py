from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

from projects.models import Project, ProjectTask
from projects.serializers import ProjectSerializer, ProjectTaskSerializer
from abc import ABC, abstractmethod


class ProjectListViewCreator(LoginRequiredMixin, ListView, ABC):
    login_url = '/login/'
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'

    @abstractmethod
    def get_queryset(self):
        qs = super(ListView, self).get_queryset()
        qs = qs.filter(deleted=False).prefetch_related('tasks')
        return qs

    @abstractmethod
    def get_context_data(self):
        return super(ListView, self).get_context_data()

class UserProjectListView(ProjectListViewCreator):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user_created=self.request.user)

    def get_context_data(self):
        context = super().get_context_data()
        context['page'] = 'SELF_PROJECTS'
        return context


class ClosedProjectListView(ProjectListViewCreator):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(
            completed_at__isnull=False, 
            user_created=self.request.user
        )

    def get_context_data(self):
        context = super().get_context_data()
        context['page'] = 'CLOSED_PROJECTS' 
        return context


class MemberProjectListView(ProjectListViewCreator):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(
            completed_at__isnull=True, 
            tasks__user=self.request.user
        ).distinct()
    
    def get_context_data(self):
        context = super().get_context_data()
        context['page'] = 'MEMBER_PROJECTS'
        return context


class MemberClosedProjectListView(ProjectListViewCreator):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(
            completed_at__isnull=False, 
            tasks__user=self.request.user
        ).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'MEMBER_CLOSED_PROJECTS' 
        return context


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
