from django.urls import  path
from watchlist_app.api.views import ReviewDetail, ReviewList, WatchListDetailAV, WatchListListAV,StreamPlatformListAV,StreamPlatformDetailAV

urlpatterns = [
    path('list', WatchListListAV.as_view(), name='movie_list'),
    path('<int:pk>', WatchListDetailAV.as_view(), name='movie_detail'),
    path('stream', StreamPlatformListAV.as_view(), name = 'stream_list'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream_detail'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name='review_list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review_detail')
]
