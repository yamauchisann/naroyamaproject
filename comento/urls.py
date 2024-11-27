from django.urls import path
from . import views

#掲示板に関するルーティング

app_name='comento'

urlpatterns=[
  #comennt一覧を表示
  path('comment/',views.CommentView.as_view(),name='comment'),
  #commentを投稿
  path('post_comment/',views.PostCommnetView.as_view(),name='post_comment'),
  #commentを投稿後のページ
  path('post_comment_done/',views.PostDoneView.as_view(),name='comment_done'),
  #commentを削除
  path('comment_delete/<int:pk>',views.CommentDeleteView.as_view(),name='comment_delete'),
  #commentを削除後のページ
  path('comment_delete_done/',views.CommentDeleteDoneView.as_view(),name='comment_delete_done'),

  
  
]