"""address_book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function viewsv
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from a_b.views import Main, DeletePerson, EditPerson, AddPerson, ShowPerson, EditPerson, EditAddress, EditPhone
from a_b.views import EditEmail, EditName


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^person/(?P<id>\d+)/delete/$', DeletePerson.as_view()),
    url(r'^person/(?P<id>\d+)/edit/$', EditPerson.as_view()),
    url(r'^person/(?P<id>\d+)/edit/edit-name/$', EditName.as_view()),
    url(r'^person/(?P<id>\d+)/edit/edit-address/$', EditAddress.as_view()),
    url(r'^person/(?P<id>\d+)/edit/edit-phone/$', EditPhone.as_view()),
    url(r'^person/(?P<id>\d+)/edit/edit-email/$', EditEmail.as_view()),
    url(r'^$', Main.as_view()),
    url(r'^person/add_person/$', AddPerson.as_view()),
    url(r'^person/(?P<id>\d+)/$', ShowPerson.as_view()),
]
