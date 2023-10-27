from django.contrib import admin
from .models import Article, Comment


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "body",
        "author",
    ]

class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "article",
        "comment",
        "author",
    ]


admin.site.register(Comment, CommentAdmin)
admin.site.register(Article, ArticleAdmin)
