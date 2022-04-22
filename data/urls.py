from django.urls import path
from .views import UploadView, DataView

urlpatterns = [
    path('upload/', UploadView, name='upload'),
    path('table/', DataView, name='table'),
    ]