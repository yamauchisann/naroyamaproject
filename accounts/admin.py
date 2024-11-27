#dbを管理者サイトへ登録

from django.contrib import admin

from .models import CustomUser
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):

  #レコード一覧にidとusernemeを表示
  list_display=('id','username')

  list_display_links=('id','username')

admin.site.register(CustomUser,CustomUserAdmin)