from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'songs', views.SongViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('data/', include(router.urls)),
    path('', views.SongListView.as_view(), name='song_list'),
    path('<pk>/edit', views.SongUpdateView.as_view()),
]
