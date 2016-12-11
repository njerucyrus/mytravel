from django.shortcuts import *
from matatu.models import *
from api.forms import PayParcelFeeForm
import random
from django.views.decorators.csrf import csrf_exempt
import json
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

@csrf_exempt
def get_mpesa_ipn(request):
    if request.method == 'POST':
        payment_data = json.loads(request.body)
        transactionId = payment_data['transactionId']
        status = payment_data['status']
        provider = payment_data['provider']
        payment = get_object_or_404(Payment, transaction_id=transactionId)
        booking = get_object_or_404(Booking, transaction_id=transactionId)
        if status == 'Success':
            # payment was completed successfully now we process the booking
            # we first update our local database to show transaction is complete

            payment.status = status
            payment.payment_mode = provider
            booking.status = status

            payment.save()
            booking.save()
            message = "booking created successfully"

            return HttpResponse(json.dumps(message), content_type='application/json')
        else:
            booking.delete()
            payment.delete()
            message = "booking Failed"

            return HttpResponse(json.dumps(message), content_type='application/json')

    else:
        message = "No data received yet"
    return HttpResponse(json.dumps(message), content_type='application/json')





