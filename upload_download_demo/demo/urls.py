# urls.py
from django.urls import path
from .views import upload_image, download_image

urlpatterns = [
    path('upload/', upload_image, name='upload_image'),
    path('download/<str:filename>/', download_image, name='download_image'),
]
