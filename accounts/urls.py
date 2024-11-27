from django.urls import path

from . import views

from django.contrib.auth import views as auth_views
app_name='accounts'

urlpatterns = [

  #signupのルーティング
  path('signup/',views.SignUpView.as_view(),name='signup'),
  
  #signup成功後のルーティング
  path('signup_success/',views.SignUpSuccessView.as_view(),name='signup_success'),
  
  #ログインさせる
  path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),

  #ログアウトさせる処理のためのルーティング
  path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
  #ログアウト後表示されるルーティング
  path('logout_done/',auth_views.LogoutView.as_view(template_name='logout_done.html'),name='logout_done'),
]