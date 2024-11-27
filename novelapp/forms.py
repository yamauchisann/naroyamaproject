#小説投稿用のフォームです
from django.forms import ModelForm
from .models import NovelPost

class NovelPostForm(ModelForm):

  class Meta:

    model=NovelPost
    fields=['category','title','comment','image1']