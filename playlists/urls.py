from django.urls import path
from . import views

app_name = "playlists"
urlpatterns = [
    path('', views.main, name="main"),
    path('search/', views.search, name="search"),
    path('show/<int:id>/',views.show, name="show"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('edit/<int:id>/', views.edit, name="edit"),

    # 음악 삭제
    path('delete_music/<int:playlist_id>/<int:music_id>/', views.delete_music, name="delete_music"),

    # 새 플레이리스트 생성
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),

    # tag
    path('tag/<int:tag_id>/', views.tag, name="tag"),

    # likes
    path('<int:playlist_id>/like_toggle/', views.like_toggle, name="like_toggle"),

    # comment
    path('create_comment/<int:playlist_id>/', views.create_comment, name="create_comment"),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name="delete_comment"),

    # follow
    path('follow_toggle/<int:id>/', views.follow_toggle, name="follow_toggle"),
]