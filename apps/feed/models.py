import uuid
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, related_name='categories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(max_length=50, unique=True, default=uuid.uuid4)

    def get_absolute_url(self):
        return reverse('tags', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)


class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, related_name='bookmarks', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='bookmarks', on_delete=models.CASCADE)
    body = models.TextField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    tags = models.ManyToManyField('Tag', blank=True, related_name='tags')

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


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    bookmark = models.ForeignKey(Bookmark, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(max_length=255, verbose_name='Comment')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

