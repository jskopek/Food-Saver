from django.shortcuts import render
from django.conf import settings
from datetime import date
from receipts.models import Receipt


# Create your views here.
def home(request):
    receipts = Receipt.objects.all()

    return render(request, "mainapp/home.html", {
        "receipts": receipts,
        "phone": settings.TWILIO_PHONE_CLEAN,
        "months": range(1, 13),
        "days": range(1, 32)
    })
