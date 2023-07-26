"""
URL configuration for project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("about-me/", views.about_me, name="about-me"),
    path("say-hi/", views.say_hi, name="say-hi"),
    path(
        "create-article/<str:title>/<str:content>/<str:published>",
        views.create_article,
        name="create-article",
    ),
    path("get-article/", views.get_article, name="get-article"),
    path("edit-article/<int:id>", views.edit_article, name="edit-article"),
    path("article/", views.list_article, name="list-article"),
    path("motorcycle/", views.list_motorcycle, name="list-motorcycle"),
    path(
        "create-motorcycle/<str:brand>/<str:reference>/",
        views.create_motorcycle,
        name="create-motorcycle",
    ),
    path("delete-article/<int:id>", views.del_article, name="delete-article"),
]
