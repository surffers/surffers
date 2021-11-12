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

from apps.feed.views import category, category_edit, category_delete, bookmark_add, bookmark_delete, vote, detail



urlpatterns = [
    #
    #
    path('b/<int:bookmark_id>/vote/', vote, name='vote'),
    path('b/<int:bookmark_id>/', detail, name='detail'),
    path('category/<uuid:category_id>/', category, name='category'),
    path('category/<uuid:category_id>/edit/', category_edit, name='category_edit'),
    path('category/<uuid:category_id>/delete/', category_delete, name='category_delete'),
    path('category/<uuid:category_id>/add_bookmark/', bookmark_add, name='add_bookmark'),
    path('category/<uuid:category_id>/delete_bookmark/<int:bookmark_id>/', bookmark_delete, name='bookmark_delete'),


] 

