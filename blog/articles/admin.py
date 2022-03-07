from django.contrib import admin

from .models import Article


# admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'author')
    date_hierarchy = 'published'
    search_fields = ('title', 'description')
