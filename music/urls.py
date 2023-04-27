from django.urls import path

from music import views

urlpatterns = [
    path('', views.list_musics, name = 'list_musics'),
    path('new/', views.create_musics, name = 'add_music'),
    path('home/', views.home, name = 'home'),
    path('update/<int:id>/', views.update_music, name = 'update_music'),
    path('delete/<int:id>/', views.delete_music, name='delete_music'),
]
