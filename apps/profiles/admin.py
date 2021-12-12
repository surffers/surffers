from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'id',
        'bio',
        'url',
    )

admin.site.register(Profile, ProfileAdmin)



