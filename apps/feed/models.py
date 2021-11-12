import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=255, blank=True, null=True)#RichTextField(blank=True, null=True)
    # visits = models.IntegerField(default=0)
    user = models.ForeignKey(User, related_name='categories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Bookmark(models.Model):
    user = models.ForeignKey(User, related_name='bookmarks', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='bookmarks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)

    number_of_votes = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Bookmarks'


    def __str__(self):
        return self.title



class Vote(models.Model):
    bookmark = models.ForeignKey(Bookmark, related_name='votes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='votes', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.bookmark.number_of_votes = self.bookmark.number_of_votes + 1
        self.bookmark.save()

        super(Vote, self).save(*args, **kwargs)





