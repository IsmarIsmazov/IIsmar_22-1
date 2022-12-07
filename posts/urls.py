

from django.contrib import admin
from django.urls import path, include
from posts.views import *
from django.conf.urls.static import static
from Blo2 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', PostListVIew.as_view()),
    path('hashtags/', HashtagListView.as_view()),
    path('posts/<int:id>/', PostDetailView.as_view()),
    path('posts/create/', PostCreateView.as_view()),
    path('users/', include('users.urls')),
    path('categories/',CategoriesView.as_view())
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)