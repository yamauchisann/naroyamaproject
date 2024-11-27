from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
from django.views.generic import CreateView,ListView

from django.urls import reverse_lazy

from .forms import NovelPostForm

from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required

from .models import NovelPost

from django.views.generic import FormView

from .forms1 import ContactForm

from django.contrib import messages

from django.core.mail import EmailMessage

from django.views.generic import DetailView,DeleteView



class IndexView(ListView):
  template_name='index.html'

  model=NovelPost

  queryset=NovelPost.objects.order_by('-posted_at')

  paginate_by=4

  
#デコレーター
@method_decorator(login_required, name='dispatch')
class CreateNovelView(CreateView):
  #小説投稿のビュー

  form_class=NovelPostForm

  template_name='post_novel.html'

  success_url=reverse_lazy('novelapp:post_done')

  def form_valid(self, form):


    postdata=form.save(commit=False)

    postdata.user=self.request.user

    postdata.save()
    return super().form_valid(form)
  
class PostSuccessView(TemplateView):

  template_name='post_success.html'


class ContactView(FormView):
  template_name='contact.html'

  form_class=ContactForm
  #送信後にリダイレクトするページ

  success_url=reverse_lazy('novelapp:contact')

  def form_valid(self, form):
    
    name = form.cleaned_data['name']
    email = form.cleaned_data['email']
    title = form.cleaned_data['title']
    message = form.cleaned_data['message']
    #メールのタイトルの書式を設定
    subject='お問い合わせ: {}'.format(title)
    #フォームの入力データの書式を設定
    message=\
    '送信者名: {0}\nメールアドレス: {1}\n タイトル: {2}\n メッセージ:{3}'\
    .format(name,email,title,message)
    #メールの送信元もアドレス
    from_email='knz2474406@stu.o-hara.ac.jp'
    #送信先のメールアドレス
    to_list=['knz2474406@stu.o-hara.ac.jp']
    #EmailMessageオブジェクト生成
    message=EmailMessage(subject=subject,body=message,from_email=from_email,to=to_list)
    #メールを送信
    message.send()
    #送信終了後に表示
    messages.success(
      self.request,'お問い合わせは正常に送信されました。')
    
    return super().form_valid(form)

class HowUseView(TemplateView):
  template_name='use_detail.html'

class DetailView(DetailView):
  template_name='post_detail.html'
  
  model=NovelPost

class DeleteView(DeleteView):
  template_name='post_delete.html'

  model=NovelPost
  success_url=reverse_lazy('novelapp:index')

  def delete(self, request, *args, **kwargs):
    
    return super().delete(request, *args, **kwargs)

class MypageView(ListView):
  template_name='mypage.html'
  
  paginate_by=3

  def get_queryset(self):
    #オーバーライド
    #ログインした場合、HttpRequest.userにユーザ名が格納
    #自分自身のみのリストを取り出す
    queryset=NovelPost.objects.filter( \
      user=self.request.user).order_by('posted_at')
    return queryset

#カテゴリの絞り込み機能のルーティング

#animal
class AnimalView(ListView):
  template_name='index.html'
  model=NovelPost
  queryset=NovelPost.objects.filter(category_id=13).order_by('-posted_at')
#anime
class AnimeView(ListView):
  template_name='index.html'
  model=NovelPost
  queryset=NovelPost.objects.filter(category_id=19).order_by('-posted_at')
#music
class MusicView(ListView):
  template_name='index.html'
  model=NovelPost
  queryset=NovelPost.objects.filter(category_id=18).order_by('-posted_at')
#sports
class SportsView(ListView):
  template_name='index.html'
  model=NovelPost
  queryset=NovelPost.objects.filter(category_id=17).order_by('-posted_at')
#food
class FoodView(ListView):
  template_name='index.html'
  model=NovelPost
  queryset=NovelPost.objects.filter(category_id=16).order_by('-posted_at')
#plant
class PlantView(ListView):
  template_name='index.html'
  model=NovelPost
  queryset=NovelPost.objects.filter(category_id=8).order_by('-posted_at')
#man
class ManView(ListView):
  template_name='index.html'
  model=NovelPost
  queryset=NovelPost.objects.filter(category_id=14).order_by('-posted_at')
#woman
class WomanView(ListView):
  template_name='index.html'
  model=NovelPost
  queryset=NovelPost.objects.filter(category_id=15).order_by('-posted_at')

#hobby
class HobbyView(ListView):
  template_name='index.html'
  model=NovelPost
  queryset=NovelPost.objects.filter(category_id=20).order_by('-posted_at')


#other
class OtherView(ListView):
  template_name='index.html'
  model=NovelPost
  queryset=NovelPost.objects.filter(category_id=9).order_by('-posted_at')

class UserView(ListView):
  template_name='index.html'

  paginate_by=3

  def get_queryset(self):
    #categoryの値を上書きするため
    #オーバーライド
    user_id=self.kwargs['user']

    user_list=NovelPost.objects.filter( \
      user=user_id).order_by('posted_at')
    return user_list



