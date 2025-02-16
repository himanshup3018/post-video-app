from .import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index' ),
    path('index/',views.index,name='index' ),
    path('video/',views.video_list,name='video_list'),
    path('Create/',views.Video_create,name='Video_create'),
    path('tweet/',views.tweet_list, name='tweet_list'),
    path('create/',views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/edit/',views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/delete/',views.tweet_delete, name='tweet_delete'),
    path('<int:video_id>/editvideo/',views.video_edit, name='video_edit'),
    path('<int:video_id>/deletevideo/',views.video_delete, name='video_delete'),
    path('register/', views.register, name='register'),
]
