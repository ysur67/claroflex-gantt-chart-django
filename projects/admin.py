from django.contrib import admin

from projects.models import Project, ProjectTask, ProjectComment, TaskComment


class ProjectTaskInline(admin.TabularInline):
    model = ProjectTask
    extra = 0


class ProjectCommentInline(admin.TabularInline):
    model = ProjectComment
    extra = 0


class TaskCommentInline(admin.TabularInline):
    model = TaskComment
    extra = 0


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'user_created',
        'created_at',
        'updated_at',
        'completed_at',
        'responsible_user',
    )
    inlines = (
        ProjectTaskInline,
        ProjectCommentInline
    )


@admin.register(ProjectTask)
class ProjectTaskAdmin(admin.ModelAdmin):
    inlines = (
        TaskCommentInline,
    )
    list_display = (
        'project', 'user',
        'created_at',
    )
