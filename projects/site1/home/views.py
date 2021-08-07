from django.shortcuts import render
from django.http import HttpResponse
from patient_view.models import patient_key


def index(request):
    if patient_key.objects.filter(patient_id=request.user.username).count()>0:
        is_patient = True
        return render(request, "home.html",{'is_patient':is_patient})
    else:
        return render(request, "home.html")