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

from apps.core.views import test, categorylists, bookmarklists, toplists, followslists, home, sponsor, users, blog
from . import views


urlpatterns = [
    #
    #

    path('', home, name='home'),
    path('categories/', categorylists, name='category_lists'),
    path('explore/', bookmarklists, name='explore'),
    path('top-lists/', toplists, name='top_lists'),
    path('follows-lists/', followslists, name='follows_lists'),
    path('users/', users, name='users'),
    path('sponsor/', sponsor, name='sponsor'),
    path('tests/', test, name='test'),
    path('blog/', blog, name='blog'),



] 

