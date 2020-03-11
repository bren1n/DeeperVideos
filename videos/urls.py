from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_videos),
    path('thumbs_video/<int:video_id>/<int:thumb_type>/', views.thumbs_video, name='thumbs_video'),
    path('delete/<int:video_id>/', views.delete_video, name='delete_video'),
    path('rank/', views.rank_themes)
]
