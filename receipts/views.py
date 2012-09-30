from receipts.models import Receipt
from members.models import Member
from products.models import Product
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date, timedelta
from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
from django.conf import settings


# Create your views here.
@csrf_exempt
def scan_sms(request):
    phone_number = request.POST["From"]
    code = request.POST["Body"]

    try:
        receipt = Receipt.objects.get(code=code)
    except:
        return render(request, "response_sms.html", {
            "response": "Sorry! We couldn't find a receipt with the code '%s'" % code
        })
    else:
        member, created = Member.objects.get_or_create(phone_number=phone_number)
        receipt.member = member
        receipt.save()

        return render(request, "response_sms.html", {
            "response": "Your receipt was saved. We are now tracking %s more things!" % receipt.products.count()
        })


@csrf_exempt
def scan(request):
    phone_number = request.GET["From"]
    code = request.GET["Body"]

    receipt = get_object_or_404(Receipt, code=code)
    member, created = Member.objects.get_or_create(phone_number=phone_number)

    receipt.member = member
    receipt.save()

    return render(request, "receipts/scan.html", {
        "receipt": receipt,
        "member": member
    })


def remind(request):
    WARN_DAYS = 1

    year = int(request.GET.get("year", date.today().year))
    month = int(request.GET.get("month", date.today().month))
    day = int(request.GET.get("day", date.today().day))

    current_date = date(year, month, day)
    warn_date = current_date + timedelta(days=WARN_DAYS)

    phones_to_warn = {}

    products = Product.objects.filter(perishable=True, expires_at=warn_date)
    for product in products:
        for receipt in product.receipts.filter(member__isnull=False):
            phone_number = receipt.member.phone_number
            if not phones_to_warn.get(phone_number):
                phones_to_warn[phone_number] = []
            phones_to_warn[phone_number].append(product)

    print phones_to_warn

    client = TwilioRestClient(settings.TWILIO_ACCOUNT, settings.TWILIO_TOKEN)
    for phone, products in phones_to_warn.items():
        products_str = ', '.join(list(map(lambda p: p.name, products)))
        msg = "The following items are about to expire in %d days: %s" % (WARN_DAYS, products_str)
        try:
            client.sms.messages.create(from_=settings.TWILIO_PHONE, to=phone, body=msg)
        except TwilioRestException, e:
            print settings.TWILIO_PHONE
            raise e
            print "Error reminding %s" % phone
        else:
            print "Reminded %s: %s" % (phone, msg)

    return HttpResponse(phones_to_warn)
