from django import forms
from matatu.models import *


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name in ['username', 'password', 'password2']:
            self.fields[field_name].help_text = None


class PassagerForm(forms.ModelForm):
    class Meta:
        model = Passager
        exclude = ('user', )


class BookSeatForm(forms.Form):
    source = forms.CharField(max_length=50, required=True)
    destination = forms.CharField(max_length=50, required=True)
    amount = forms.CharField(max_length=10)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)


class SeatPaymentForm(forms.Form):
    phoneNumber = forms.CharField(max_length=13,
                                  widget=forms.TextInput(attrs={'placeholder': '+2547 XXX XXX'}))

    amount = forms.DecimalField(max_digits=10, decimal_places=2, disabled=True)


class SendParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = '__all__'

