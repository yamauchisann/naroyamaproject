from django.contrib import admin

# Register your models here.
from .models import NovelPost,Category

class CategoryAdmin(admin.ModelAdmin):


  #レコード一覧にidとtitleを表示
  list_display=('id','title')

  #表示するカラムにリンクを表示

  list_display_links=('id','title')

class NovelPostAdmin(admin.ModelAdmin):

  #レコード一覧にidとtitleを表示
  list_display=('id','title')

  #表示するカラムにリンクを表示

  list_display_links=('id','title')

admin.site.register(Category,CategoryAdmin)

admin.site.register(NovelPost,NovelPostAdmin)