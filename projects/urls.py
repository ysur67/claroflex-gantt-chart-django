from django.urls import path

from projects.views import (
    UserProjectListView,
    ClosedProjectListView,
    MemberProjectListView,
    MemberClosedProjectListView, 
    ProjectDetailView
)

urlpatterns = [
    path('', UserProjectListView.as_view(), name='project-list'),
    path('closed/', ClosedProjectListView.as_view(), name='closed-projects-list'),
    path('member/', MemberProjectListView.as_view(), name='member-projects-list'),
    path('member-closed/', MemberClosedProjectListView.as_view(), name='member-closed-projects-list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
]
