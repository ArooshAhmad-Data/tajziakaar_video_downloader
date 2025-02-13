from django.urls import path
from .views import ItemListView, VideoDownloadAPIView

urlpatterns = [
    path("", ItemListView.as_view(), name="item-list"),
    path("api/download-videos/", VideoDownloadAPIView.as_view(), name="download_videos"),
]
