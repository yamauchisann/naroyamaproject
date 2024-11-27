from django.contrib import admin

from .models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):

  list_display=('id','title')

  list_display_links=('id','title')


admin.site.register(Comment,CommentAdmin)

