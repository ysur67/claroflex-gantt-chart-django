"""engineers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)
# from django.contrib.auth.decorators import login_required
from django.urls import path

# import ganttchart.views

# login_required(views.create_project_home),
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^login/$',
        LoginView.as_view(
            template_name='admin/login.html'
        ),
        name="ganttchart-login"
        ),
    url(r'^logout/$',
        LogoutView.as_view(
            template_name='logout.html'
        ),
        name="ganttchart-logout"
        ),

    # url(r'^$',
    #     ganttchart.views.ListContactView.as_view(),
    #     name='contacts-list', ),
    # url(r'^(?P<pk>\d+)/$', ganttchart.views.ContactView.as_view(),
    #     name='contacts-view', ),
    # url(r'^new$',
    #     ganttchart.views.CreateContactView.as_view(),
    #     name='contacts-new', ),
    # url(r'^edit/(?P<pk>\d+)/$', ganttchart.views.UpdateContactView.as_view(),
    #     name='contacts-edit', ),
    # url(r'^edit/(?P<pk>\d+)/addresses$', ganttchart.views.EditContactAddressView.as_view(),
    #     name='contacts-edit-addresses', ),
    # url(r'^delete/(?P<pk>\d+)/$', ganttchart.views.DeleteContactView.as_view(),
    #     name='contacts-delete', ),
    # url(r'^project$',
    #     ganttchart.views.FillProjectView.as_view(),
    #     name='ganttchart-project', ),
    url(r'^admin/',
        admin.site.urls),
    # url(r'^project/create/home$',
    #     ganttchart.views.create_project_home,
    #     name='project-create-home'),
    path('', RedirectView.as_view(url='/projects/')),
    path('projects/', include('projects.urls')),
    path('api/v1/', include(('users.urls', 'users'))),
    path('api/v1/', include(('projects.api_urls', 'projects'))),
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
