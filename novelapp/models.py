from django.db import models

# Create your models here.

from accounts.models import CustomUser

#カテゴリのデータベースを定義
class Category(models.Model):

  title=models.CharField(
    verbose_name='カテゴリ',
    max_length=20)

  def __str__(self):

    return self.title
  
#投稿内容のデータベースを定義

class NovelPost(models.Model):
  #Accounts,Categoryのデータベースと連携させる
  user=models.ForeignKey(
    CustomUser,
  #フィールドのタイトル
    verbose_name='ユーザー',

    on_delete=models.CASCADE
  )

  category=models.ForeignKey(
    Category,

    verbose_name='カテゴリ',
    #投稿内容を消すとき、データベースを連携させているため
    #カテゴリの削除を防ぐ

    on_delete=models.PROTECT
  )

  #タイトル用のフィールド
  
  title = models.CharField(
        verbose_name='タイトル', # フィールドのタイトル
        max_length=200        # 最大文字数は200
        )
    # コメント用のフィールド
  comment = models.TextField(
      verbose_name='コメント',  # フィールドのタイトル
      )
    # イメージのフィールド1
  image1 = models.ImageField(
    verbose_name='イメージ',# フィールドのタイトル
    upload_to = 'photos',   # MEDIA_ROOT以下のphotosにファイルを保存
    blank=True,
    null=True  
    )
    
  # 投稿日時のフィールド
  posted_at = models.DateTimeField(
    verbose_name='投稿日時', # フィールドのタイトル
    auto_now_add=True       # 日時を自動追加
    )
    
  def __str__(self):
    '''オブジェクトを文字列に変換して返す
        
        Returns(str):投稿記事のタイトル
        '''
    return self.title

  
