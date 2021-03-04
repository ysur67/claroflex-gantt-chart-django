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

from models import Contact
from models import Project
from models import Task
from models import Report
from models import TascsReport

def create_project_home(request):
    return render(request, 'projects/create-project-home.html', {})

