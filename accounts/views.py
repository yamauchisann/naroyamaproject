from django.shortcuts import render

from django.views.generic import TemplateView,CreateView

from .forms import CustomUserCreationForm

from django.urls import reverse_lazy
# Create your views here.

#signupのビュー
class SignUpView(CreateView):
  #forms.pyで作成したCustomUserCreationFormを使う
  form_class=CustomUserCreationForm
  #レンダリング
  template_name='signup.html'
  #認証成功後のリダイレクト先
  success_url=reverse_lazy('accounts:signup_success')

  #signupボタンを押した後
  def form_valid(self, form):

    user=form.save()
    self.object=user
    return super().form_valid(form)

#signup成功後のビュー
class SignUpSuccessView(TemplateView):

  #レンダリング
  template_name='signup_success.html'