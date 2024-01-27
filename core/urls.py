"""
URL configuration for core project.

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
from django.urls import include, path
from .views import account_login, account_logout, account_register, overview

# https://docs.djangoproject.com/en/4.2/intro/tutorial01/#path-argument-route
# The include() function allows referencing other URLconfs.
urlpatterns = [
    path('accounts/', include ('django.contrib.auth.urls')),
    path("", include("dailylogs.urls")),
    path("", include("projects.urls")),
    path("", include("tasks.urls")),
    path("", include("sprints.urls")),
    path("", overview, name="overview"),
    path("login/", account_login, name="login"),
    path("logout/", account_logout, name="logout"),
    path("register/", account_register, name="register"),
    path("admin/", admin.site.urls),
]
