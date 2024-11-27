from django.urls import path
from . import views

app_name='novelapp'

urlpatterns=[

  path('',views.IndexView.as_view(),name='index'),

  path('contact/',views.ContactView.as_view(),name='contact'),

  path('post/',views.CreateNovelView.as_view(),name='post'),

  path('post_done',views.PostSuccessView.as_view(),name='post_done'),

  path('how to use/',views.HowUseView.as_view(),name='admin_detail'),

  path('post-detail/<int:pk>',views.DetailView.as_view(),name='post_detail'),

  path('post-delete/<int:pk>',views.DeleteView.as_view(),name='post_delete'),

  path('mypage/',views.MypageView.as_view(),name='mypage'),

  #カテゴリごとのルーティング
  #animal
  path('animal/',views.AnimalView.as_view(),name='animal'),
  #anime
  path('anime/',views.AnimeView.as_view(),name='anime'),
  #music
  path('music/',views.MusicView.as_view(),name='music'),
  #sports
  path('sports/',views.SportsView.as_view(),name='sports'),
  #food
  path('food/',views.FoodView.as_view(),name='food'),
  #plant
  path('plant/',views.PlantView.as_view(),name='plant'),
  #man
  path('man/',views.ManView.as_view(),name='man'),
  #woman
  path('woman/',views.WomanView.as_view(),name='woman'),

  #hobby
  path('hobby/',views.HobbyView.as_view(),name='hobby'),

  #other
  path('other/',views.OtherView.as_view(),name='other'),

  

  #選択したユーザーが投稿した小説のurl
  path('user-list/<int:user>/',views.UserView.as_view(),name='user_list'),

]