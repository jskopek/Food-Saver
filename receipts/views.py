from receipts.models import Receipt
from members.models import Member
from django.shortcuts import render
from django.shortcuts import get_object_or_404


# Create your views here.
def scan(request):
    phone_number = request.GET["phone_number"]
    code = request.GET["code"]

    receipt = get_object_or_404(Receipt, code=code)
    member, created = Member.objects.get_or_create(phone_number=phone_number)

    receipt.member = member
    receipt.save()

    return render(request, "receipts/scan.html", {
        "receipt": receipt,
        "member": member
    })
