from django.shortcuts import render
from django.conf import settings
from datetime import date


# Create your views here.
def home(request):
    return render(request, "mainapp/home.html", {
        "phone": settings.TWILIO_PHONE,
        "months": range(1, 13),
        "days": range(1, 32)
    })
