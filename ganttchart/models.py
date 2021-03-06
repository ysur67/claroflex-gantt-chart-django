# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Contact(models.Model):
    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,
    )
    email = models.EmailField()
    owner = models.ForeignKey(User)

    def __str__(self):
        return ' '.join([
            self.first_name,
            self.last_name,
        ])
    
    def get_absolute_url(self):
        return reverse('contacts-view', kwargs={'pk': self.id})

#    $PARS['{USER_ID}'] = $report_data['user_id'];
#    $PARS['{NAME}'] = $user_obj->get_user_name();
#    $PARS['{MIDDLENAME}'] = $user_obj->get_user_middlename();
#    $PARS['{SURNAME}'] = $user_obj->get_user_surname();
#    $PARS['{USER_POSITION}'] = $user_obj->get_user_position();
#    $PARS['{AVATAR_SRC}'] = $user_avatar_src;

class Address(models.Model):
    contact = models.ForeignKey(Contact)
    address_type = models.CharField(
        max_length=10,
    )
    address = models.CharField(
        max_length=255,
    )
    city = models.CharField(
        max_length=255,
    )
    state = models.CharField(
        max_length=255,
    )
    postal_code = models.CharField(
        max_length=20,
    )

    class Meta:
        unique_together = ('contact', 'address_type',)

class Project(models.Model):
    """Project for Grantt Chart"""

    deleted = models.BooleanField(default=False,
                                      verbose_name=_('project_deleted'))
    closed = models.BooleanField(default=False,
                                      verbose_name=_('project_closed'))
    head_confirmed = models.BooleanField(default=False,
                                      verbose_name=_('project_head_confirmed'))
    name = models.CharField(max_length=140, blank=True,
                            verbose_name=_('name'))

    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')
        ordering = ['-name']


class Task(models.Model):
    """Task for Grantt Chart"""
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, verbose_name=_('project'))
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name=_('contact'))
    name = models.CharField(max_length=140, blank=True,
                            verbose_name=_('name'))
    date_start = models.DateField(auto_now_add=True,
                                     verbose_name=_('date start'))
    date_finish = models.DateField(auto_now=True,
                                         verbose_name=_('date finish'))
    task_confirm = models.BooleanField(default=False,
                                      verbose_name=_('task_confirm'))
    task_completed = models.BooleanField(default=False,
                                      verbose_name=_('task_conpleted'))
    added_by_user_id = models.PositiveSmallIntegerField(default=0, blank=True, verbose_name=_('added by contact id'))
    after_task_id = models.PositiveSmallIntegerField(default=0, blank=True,
                                              verbose_name=_('after_task_id'))

    class Meta:
        verbose_name = _('projects_task')
        verbose_name_plural = _('projects_tasks')
        ordering = ['-date_start']


class Report(models.Model):
    """Report for Grantt Chart"""
    project_id = models.ForeignKey(
        Project, on_delete=models.CASCADE, verbose_name=_('project'))
    report_id = models.PositiveSmallIntegerField(default=0, blank=True,
                                              verbose_name=_('report_id'))
    deleted = models.BooleanField(default=False,
                                      verbose_name=_('project_deleted'))
    report_confirm = models.BooleanField(default=False,
                                      verbose_name=_('project_report_confirm'))
    report_date = models.DateField(auto_now=True,
                                         verbose_name=_('project report date'))
    report_text = models.TextField(blank=True, verbose_name=_('report_text'))


    class Meta:
        verbose_name = _('projects_report')
        verbose_name_plural = _('projects_reports')
        ordering = ['-report_id']

class TasksReport(models.Model):
    """TasksReport for Grantt Chart"""

    task_id = models.ForeignKey(
        Task, on_delete=models.CASCADE, verbose_name=_('project_task_report_project'))
    report_confirm = models.BooleanField(default=False,
                                      verbose_name=_('project_task_report_confirm'))
    deleted = models.BooleanField(default=False,
                                      verbose_name=_('project_task_report_deleted'))
    user_id = models.ForeignKey(
	Contact, on_delete=models.CASCADE, verbose_name=_('project_task_report_user_id'), default=1)


    class Meta:
        verbose_name = _('projects_tasks_report')
        verbose_name_plural = _('projects_tasks_reports')
        ordering = ['-task_id']
