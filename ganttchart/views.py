# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.


import json
import ast
import csv

from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView,
    CreateView,
    UpdateView,
)

from ganttchart.models import (
    Contact,
    Project,
    Task,
    Report,
    TasksReport,
)
import forms

def create_project_home(request):
    return render(request, 'projects/create-project-home.html', {})

# Форма добавления выговора
def fill_projects_add_form():
    return reverse ('ganttchart/add_form.tpl')

class LoggedInMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class ListContactView(ListView):
    model = Contact
    template_name = 'contact_list.html'
    
    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)
    
class ContactOwnerMixin(object):
    def get_object(self, queryset=None):
        """Returns the object the view is displaying.
        """
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        queryset = queryset.filter(
            pk=pk,
            owner=self.request.user,
        )
        try:
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise PermissionDenied
        return obj

class ContactView(LoggedInMixin, ContactOwnerMixin, DetailView):
    model = Contact
    template_name = 'contact.html'

class CreateContactView(LoggedInMixin, CreateView):
    model = Contact
    template_name = 'edit_contact_custom.html'
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('contacts-list')
    
    def get_context_data(self, **kwargs):
        context = super(CreateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-new')
        return context

class FillProjectView(CreateView):
    model = Project
    template_name = 'ganttchart/projects.tpl'
    fields = ['deleted', 'closed', 'head_confirmed', 'name']

    def get_success_url(self):
 #       if(_GET['part']==1 && _GET['part']==2)
            # Форма добавления нового проекта
        add_form = fill_projects_add_form()
#        return reverse('contacts-list')
