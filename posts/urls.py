from django.urls import path
from .views import *

urlpatterns = [
    path('hashtags/', hashtags_view),
    path('posts/', posts_view),
    path('posts/<int:id>/', comment_view),
]