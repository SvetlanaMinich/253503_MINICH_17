"""
URL configuration for start project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from hello import views

urlpatterns = [
    path('', views.main),
    path('about_company/',views.about_company),
    path('contacts/',views.contacts),
    path('news/',views.news),
    path('politics/',views.politics),
    path('promocodes/',views.promocodes),
    path('qa/',views.qa),
    path('reviews/',views.reviews),
    path('vacancies/',views.vacancies),

    path('register/master/<int:master_id>',views.mastersview, name="master"),
    path('login/master/<int:master_id>',views.mastersview, name="master"),
    path('register/client/<int:client_id>',views.clientsview, name="client"),
    path('login/client/<int:client_id>',views.clientsview, name="client"),
    path('register/',views.register),
    path('login/',views.login),

    re_path(r'^(login|register)/master/editmaster/(?P<master_id>\d+)', views.editmaster, name="editmaster"),
    re_path(r'^(login|register)/client/editclient/(?P<client_id>\d+)', views.editclient, name="editclient"),

    re_path(r'^(login|register)/client/createorder/(?P<client_id>\d+)', views.createorder, name="createorder")
]
