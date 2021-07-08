from django.urls import path

from . import views

urlpatterns = [
    path('', views.patient_view, name='patient_view'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]