from receipts.models import Receipt
from members.models import Member
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def scan(request):
    import ipdb; ipdb.set_trace()
    phone_number = request.POST["From"]
    code = request.POST["Body"]

    receipt = get_object_or_404(Receipt, code=code)
    member, created = Member.objects.get_or_create(phone_number=phone_number)

    receipt.member = member
    receipt.save()


    return render(request, "receipts/scan_xml.html", {
        "receipt": receipt,
        "member": member
    })
    return render(request, "receipts/scan.html", {
        "receipt": receipt,
        "member": member
    })
