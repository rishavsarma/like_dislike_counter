from django.urls import path
from .views import index, like_button, dislike_button

urlpatterns = [
    path('', index, name='index'),
    path('like_button/', like_button, name='like_button'),
    path('dislike_button/', dislike_button, name='dislike_button'),
]
