from django import forms
from matatu.models import ParcelFee


class PayParcelFeeForm(forms.Form):
    # parcel = ParcelFee.objects.all()
    # PARCEL_TYPE = (
    #     [(str(p.parcel_type), str(p.parcel_type))for p in parcel]
    #
    # )
    parcel_type = forms.ChoiceField(choices=[])
    phoneNumber = forms.CharField(max_length=13, required=True)
    parcel_fee = forms.DecimalField(max_digits=10, decimal_places=2, disabled=False)



