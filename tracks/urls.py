from django.urls import path
from .views import *

urlpatterns = [
    path('', top_list, name='top_list_url'),
    path('tracks/', tracks_list, name='tracks_list_url'),
    path('track/create/', TrackCreate.as_view(), name='track_create_url'),
    path('track/<slug>/', TrackDetail.as_view(), name='track_detail_url'),
    path('track/<slug>/update/', TrackUpdate.as_view(), name='track_update_url'),
    path('track/<slug>/delete/', TrackDelete.as_view(), name='track_delete_url'),
    path('genres/', genres_list, name='genres_list_url'),
    path('genre/create/', GenreCreate.as_view(), name='genre_create_url'),
    path('genre/<slug>/', GenreDetail.as_view(), name='genre_detail_url'),
    path('genre/<slug>/update/', GenreUpdate.as_view(), name='genre_update_url'),
    path('genre/<slug>/delete/', GenreDelete.as_view(), name='genre_delete_url')
]
