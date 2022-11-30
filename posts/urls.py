
from django.contrib import admin
from django.urls import path
from posts.views import posts_view, categories_view, post_create_view, post_detail_view, hashtags_view
from django.conf.urls.static import static
from Blo2 import settings


urlpatterns = [
    path('hashtags/', hashtags_view),
    path('posts/', posts_view),
    path('posts/<int:id>/', post_detail_view),
    path('categories/', categories_view),
    path('posts/create/', post_create_view)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)