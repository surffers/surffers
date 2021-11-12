from django.urls import path
from django.contrib.auth import views

from django.conf.urls import handler400, handler403, handler404, handler500


from apps.profiles.views import profile, edit_profile, follow_user, unfollow_user, followers, follows, categories


urlpatterns = [
    #
    #
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('<str:username>/', profile, name='profile'),
    path('<str:username>/categories/', categories, name='categories'),
    path('<str:username>/followers/', followers, name='followers'),
    path('<str:username>/follows/', follows, name='follows'),
    path('<str:username>/follow/', follow_user, name='follow_user'),
    path('<str:username>/unfollow/', unfollow_user, name='unfollow_user'),


] 