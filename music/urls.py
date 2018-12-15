from django.conf.urls import url
from . import views
from django.urls import path


app_name = 'music'
urlpatterns = [
    # /music
    path('', views.IndexView.as_view(), name="index"),
    # /music/66
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    #/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name="album_add"),
]
