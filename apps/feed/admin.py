from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Bookmark, Comment, Tag

admin.site.register(Tag)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'id',
        'user',
    )
    search_fields = (
        'title',
    )
    date_hierarchy = ('created_at')

admin.site.register(Category, CategoryAdmin)

class BookmarkAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'id',
        'url',
        'user',
    )
    list_filter = ('created_at', 'user')
    raw_id_fields = ('user',) 
    search_fields = ('title',)
    date_hierarchy = ('created_at')


admin.site.register(Bookmark, BookmarkAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'body',
        'user',
    )

admin.site.register(Comment, CommentAdmin)


    

    