from django.contrib import admin
from . import models


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'auther']
    list_filter = ['auther']
    search_fields = ['title']


admin.site.register(models.Article, ArticleAdmin)
