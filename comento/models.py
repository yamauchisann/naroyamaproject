from django.db import models

from accounts.models import CustomUser

# Create your models here.
class Comment(models.Model):
  
  user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='ユーザー',
        # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
        )
  
  # タイトル用のフィールド
  title = models.CharField(
      verbose_name='タイトル', # フィールドのタイトル
      max_length=200        # 最大文字数は200
    )

  #本文用のフィールド
  content=models.TextField(
    verbose_name='本文'
  )
  #投稿日時のフィールド
  posted_at=models.DateTimeField(
    verbose_name='投稿日時',
    auto_now_add=True
  )
  

  def __str__(self):
    '''
    Django管理サイトでデータを表示する際に識別名として
    投稿記事のタイトル(titleフィールドの値)を表示するために
    必要
    '''
    return self.title