from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse


def get_user_name(user):
    return f"{user.first_name} {user.last_name}" if user.first_name else user.username


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

    def get_absolute_url(self):
        return reverse("project-detail", kwargs={"pk": self.id})

    @property
    def user_created_name(self):
        return get_user_name(self.user_created)

    @property
    def responsible_user_name(self):
        obj = self.responsible_user
        if not obj:
            return None
        return get_user_name(obj)

    def close(self):
        self.completed_at = timezone.now()
        self.save(update_fields=['completed_at', 'updated_at', ])

    def open(self):
        self.completed_at = None
        self.save(update_fields=['completed_at', 'updated_at', ])


class ProjectFile(models.Model):
    file = models.FileField('Project file', upload_to='project_files/%Y/%m/%d')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='files')
    created_at = models.DateTimeField('Created at', auto_now_add=True)


class ProjectTask(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Task user', related_name='tasks')
    description = models.TextField('Task Description', null=True, blank=True)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)
    start_date = models.DateField('Start date  by plan')
    close_date = models.DateField('Close date by plan')
    actual_start_date = models.DateField('Actual start date', null=True, blank=True)
    actual_close_date = models.DateField('Actual close date', null=True, blank=True)
    related_task = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def user_name(self):
        return get_user_name(self.user)

    def close(self):
        self.actual_close_date = timezone.now()
        self.save(update_fields=['actual_close_date', 'updated_at', ])

    def open(self):
        self.actual_close_date = None
        self.save(update_fields=['actual_close_date', 'updated_at', ])
