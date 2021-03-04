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
from django.views.generic import ListView

from ganttchart.models import Contact
from ganttchart.models import Project
from ganttchart.models import Task
from ganttchart.models import Report
from ganttchart.models import TascsReport

def create_project_home(request):
    return render(request, 'projects/create-project-home.html', {})


class ListContactView(ListView):

      model = Contact