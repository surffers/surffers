from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300, blank=True)
    url = models.URLField(max_length=200, blank=True)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
    created = models.DateTimeField(auto_now_add=True)

User.profile = property(lambda u:Profile.objects.get_or_create(user=u)[0])


