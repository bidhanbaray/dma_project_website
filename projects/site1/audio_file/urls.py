from django.conf.urls import url
from .views import audio_fileView

urlpatterns = [
    url('upload/', audio_fileView.as_view(), name='audio_file_upload'),
]