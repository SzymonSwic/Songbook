from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    SongViewSet,
    SongListView,
    SongDetailView,
    SongCreateView,
    SongUpdateView,
    SongDeleteView)

router = DefaultRouter()
router.register(r'song', SongViewSet)

urlpatterns = [
    path('data/', include(router.urls)),
    path('', SongListView.as_view(), name='song_list'),
    path('create/', SongCreateView.as_view(), name='song_create'),
    path('<int:pk>/', SongDetailView.as_view(), name='song_detail'),
    path('<int:pk>/edit/', SongUpdateView.as_view(), name='song_update'),
    path('<int:pk>/delete/', SongDeleteView.as_view(), name='song_delete'),

]
