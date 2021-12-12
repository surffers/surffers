from datetime import timezone, timedelta
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.utils.timezone import now
from djpaddle.models import Checkout


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300, blank=True)
    skills = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=30, blank=True)
    url = models.URLField(max_length=200, blank=True)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
    created = models.DateTimeField(auto_now_add=True)

    def has_subscription(self):
        return self.subscriptions.filter(Q(status='active') | Q(status='deleted', next_bill_date__gte=now)).exists() or Checkout.objects.filter(completed=True, email=self.email, created_at__day=now.day).exists()

User.profile = property(lambda u:Profile.objects.get_or_create(user=u)[0])


