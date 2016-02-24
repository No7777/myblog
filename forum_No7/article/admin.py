# -*- coding:utf-8 -*-
from django.contrib import admin
from models import Article
from comment.models import Comment

class CommentInLine(admin.TabularInline):
    model = Comment
    readonly_fields = ("owner", "content", "status", "create_timestamp", "last_update_timestamp")
    fieldsets = (
        (
            None, {
             "fields": ("owner", "content", "status", "create_timestamp")
            }
        ),
    )
    
CommentInLine.can_delete = False
CommentInLine.max_num = 20
CommentInLine.min_num = 0

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'block', 'author', 'status', 'create_timestamp', 'last_update_timestamp')
    search_fields = ['title', 'content']
    list_filter = ('block', )
    
    actions = ["make_picked"]
    inlines = [CommentInLine]
    readonly_fields = ("title", "author", "block", "content", "status", "create_timestamp", "last_update_timestamp")
    fieldsets = (
        (
            None, {
                "fields": ("title", "author", "content", "status", "create_timestamp")
            }
        ),
        (
            u"其他", {
                "classes": ("collapse",),
                "fields": ("block", "last_update_timestamp")
            }
        )
    )
    
    def make_picked(modeladmin, request, queryset):
        for i in queryset:
            i.status = 10
            i.save()

    make_picked.short_description = u"设置精华"

admin.site.register(Article, ArticleAdmin)
