from django.urls import path

from . import views

urlpatterns = [
    path('', views.doctor_view, name='doctor_view'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('add_patient', views.add_patient, name='add_patient'),
    path('<patient_id>/', views.patient_data, name='patient_data'),
]