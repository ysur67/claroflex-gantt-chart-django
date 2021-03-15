from django.conf import settings
from django.db import models


class Project(models.Model):
    name = models.CharField('Project name', max_length=100)
    description = models.TextField('Project Description', null=True, blank=True)
    user_created = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     on_delete=models.PROTECT,
                                     verbose_name='User created',
                                     related_name='user_created_projects', )
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)
    completed_at = models.DateTimeField('Completed at', null=True, blank=True)
    responsible_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                         on_delete=models.PROTECT,
                                         null=True,
                                         blank=True,
                                         verbose_name='Responsible User',
                                         related_name='responsible_user_projects', )
    deleted = models.BooleanField('Deleted?', default=False)

    def __str__(self):
        return self.name

    @property
    def user_created_name(self):
        obj = self.user_created
        return f"{obj.first_name} {obj.last_name}" if obj.first_name else obj.username

    @property
    def responsible_user_name(self):
        obj = self.responsible_user
        if not obj:
            return None
        return f"{obj.first_name} {obj.last_name}" if obj.first_name else obj.username


class ProjectFile(models.Model):
    file = models.FileField('Project file', upload_to='project_files/%Y/%m/%d')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='files')
    created_at = models.DateTimeField('Created at', auto_now_add=True)


class ProjectTask(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Task user')
    description = models.TextField('Task Description', null=True, blank=True)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)
    start_date = models.DateField('Start date')
    close_date = models.DateField('Close date')
    related_task = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
