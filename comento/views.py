from django.shortcuts import render

from django.views.generic import ListView,FormView,TemplateView,DeleteView

from .models import Comment

from django.urls import reverse_lazy

from .forms_comment import CommentCreateForm

# Create your views here.

class CommentView(ListView):
  template_name='comment_list.html'
  #使うデータベースの種類
  model=Comment
  #コメントを降順に並び替える
  queryset=Comment.objects.order_by('-posted_at')

  paginate_by=4

class PostCommnetView(FormView):

  template_name='post_comment.html'
  #書式をform_commentから適用させる
  form_class=CommentCreateForm
  #成功後リダイレクト
  success_url=reverse_lazy('comento:comment_done')

  #投稿を押した場合
  def form_valid(self, form):
    
    #ワンクッションおいて投稿したusernameを追加する
    postdata=form.save(commit=False)

    postdata.user=self.request.user
    #追加して保存した後
    postdata.save()
    return super().form_valid(form)
#commentを投稿後
class PostDoneView(TemplateView):
  
  template_name='comment_done.html'
#comment削除
class CommentDeleteView(DeleteView):
  template_name='comment_delete.html'

  model=Comment
  success_url=reverse_lazy('comento:comment_delete_done')

  def delete(self, request, *args, **kwargs):
    
    return super().delete(request, *args, **kwargs)
#削除後のリダイレクト
class CommentDeleteDoneView(TemplateView):
  template_name='comment_delete_done.html'