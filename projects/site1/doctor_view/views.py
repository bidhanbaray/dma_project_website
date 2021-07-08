from django.shortcuts import render, redirect
from user_data.models import user_data
from audio_file.models import audio_file
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from doctor_view.models import doctor_data
from patient_view.models import patient_key
from rest_framework import permissions

def doctor_view(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        return HttpResponse("Please Log in")
    patient_list = doctor_data.objects.filter(doctor_id=username)
    if patient_list.count()<1:
        return HttpResponse("No doctor dashboard available for this user.<br> <a href='http://bidhanbaray.pythonanywhere.com/doctor_view/logout'>Logout</a><br>")
    else:
        return render(request, 'doctorDashboard.html',{'patient_list': patient_list})
#    return HttpResponse("Doctor View")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("doctor_view")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect("login")

    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

def add_patient(request):
    if request.method == "POST":
        username = request.user.username
        pat_id = request.POST["patient_id"]
        submitted_key = request.POST["approval_key"]
        patient = patient_key.objects.filter(patient_id=pat_id)
        if doctor_data.objects.filter(patient_id=pat_id):
            messages.info(request,'Already added.')
            return redirect("doctor_view")
        if (patient[0].approval_key ==submitted_key and len(patient)==1):
            new_patient = doctor_data(doctor_id=username, patient_id=pat_id)
            new_patient.save()
            return redirect("doctor_view")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect("doctor_view")

def patient_data(request, patient_id):
    if (request.user.is_authenticated and doctor_data.objects.filter(doctor_id=request.user.username).count()>0):
        entries = user_data.objects.filter(device_id=patient_id)
        audio_entries = audio_file.objects.filter(device_id=patient_id)
        return render(request, 'userDashboard.html',{'entries': entries,'audio_entries':audio_entries})
    else:
        return HttpResponse("Please Log in as doctor")
