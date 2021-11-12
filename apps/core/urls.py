"""surffers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path
from django.contrib.auth import views

from django.conf.urls import handler400, handler403, handler404, handler500

from apps.core.views import test, settings, dashboard, home, sponsor, users, blog
from . import views


urlpatterns = [
    #
    #

    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('users/', users, name='users'),
    path('sponsor/', sponsor, name='sponsor'),
    path('tests/', test, name='test'),
    path('settings/', settings, name='settings'),
    path('blog/', blog, name='blog'),

    path('user_settings/', views.userSettings, name="user_settings"),
	path('update_theme/', views.updateTheme, name="update_theme"),
 
] 

