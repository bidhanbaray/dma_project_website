from django.shortcuts import render, redirect
from user_data.models import user_data
from audio_file.models import audio_file
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from doctor_view.models import doctor_data
def patient_view(request):
    if request.user.is_authenticated:
         username = request.user.username
         if doctor_data.objects.filter(doctor_id=username).count()>0:
             return HttpResponse("Please Log in as patient.<br> <a href='http://bidhanbaray.pythonanywhere.com/patient_view/logout'>Logout</a><br>")
    else:
        return HttpResponse("Please Log in")
    entries = user_data.objects.filter(device_id=username)
    audio_entries = audio_file.objects.filter(device_id=username)

    return render(request, 'userDashboard.html',{'entries': entries,'audio_entries':audio_entries})

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("patient_view")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect("login")

    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")
