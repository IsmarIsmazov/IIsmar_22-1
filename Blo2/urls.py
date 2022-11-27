
from django.contrib import admin
from django.urls import path, include
from posts.views import *
from django.conf.urls.static import static
from Blo2 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)