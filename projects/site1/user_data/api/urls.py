# todo/api/urls.py : API urls.py
from django.conf.urls import url
from django.urls import path, include
from .views import (
    user_dataListApiView,
)

urlpatterns = [
    path('', user_dataListApiView.as_view()),
]