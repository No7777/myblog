from django.contrib import admin
from models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('block', 'article', 'owner', 'content', 'status', 'create_timestamp', 'last_update_timestamp')
    search_fields = ['block', 'article', 'owner', 'content']
    list_filter = ('block', 'owner')
    
admin.site.register(Comment, CommentAdmin)
