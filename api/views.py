from django.shortcuts import *
from matatu.models import *
from api.forms import PayParcelFeeForm
import random


def pay_fare(request):
    if request.method == 'POST':
        return


def pay_parcel_fee(request):

    if request.method == 'POST':
        form = PayParcelFeeForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            parcel_type = cd['parcel_type']
            phoneNumber = cd['phoneNumber']
            parcel_fee = cd['parcel_fee']

            """
             do the logic of m-pesa payment
             bt for now just by pass
            """
            transaction_id = random.randrange(10, 100000, 6)
            payment_mode = "M-PESA"
            payment = Payment.objects.create(
                transaction_id=transaction_id,
                phone_no=phoneNumber,
                payment_for=parcel_type,
                payment_mode=payment_mode,
                amount=parcel_fee
            )
            payment.save()
            return HttpResponse("Payment for the parcel was successful")
    else:
        form = PayParcelFeeForm()
    return render(request, 'paymentapp/parcel_payment.html', {'form': form, })


"""
this method listens for payment notification from
m-pesa api and updates the status of the payments

"""


def payment_notification(request):
    return None


