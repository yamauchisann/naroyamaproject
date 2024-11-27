#signupにつかうための書式を設定


from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

  class Meta:
  #使いたい機能を継承。
  #連携するモデルの設定
    model=CustomUser


    fields=('username','email','password1','password2')