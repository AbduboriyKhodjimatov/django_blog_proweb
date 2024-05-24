from django.contrib import admin
from .models import Category
from .models import Article, Comment


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    list_display_links = ['pk', 'name']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'views', 'author', 'category']
    list_display_links = ['pk', 'name']
    readonly_fields = ['views']
    list_editable = ['author', 'category']
    list_filter = ['created_at', 'category', 'author']
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
