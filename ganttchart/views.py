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
from django.urls import reverse
from django.views.generic import (
    ListView,
    CreateView,
)

from ganttchart.models import (
    Contact,
    Project,
    Task,
    Report,
    TasksReport,
)

def create_project_home(request):
    return render(request, 'projects/create-project-home.html', {})

# Форма добавления выговора
def fill_projects_add_form():
    return reverse ('ganttchart/add_form.tpl')

class ListContactView(ListView):
    model = Contact
    template_name = 'contact_list.html'

class CreateContactView(CreateView):

    model = Contact
    template_name = 'edit_contact.html'
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('contacts-list')

class FillProjectView(CreateView):
    model = Project
    template_name = 'ganttchart/projects.tpl'
    fields = ['deleted', 'closed', 'head_confirmed', 'name']

    def get_success_url(self):
 #       if(_GET['part']==1 && _GET['part']==2)
            # Форма добавления нового проекта
        add_form = fill_projects_add_form()
#        return reverse('contacts-list')
