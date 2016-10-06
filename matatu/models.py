from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Driver(models.Model):
    user = models.OneToOneField(User)
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE')
    )
    gender = models.CharField(max_length=10, choices=GENDER)
    national_id = models.PositiveIntegerField()
    license = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=13)

    def __unicode__(self):
        return str(self.national_id)


class Passager(models.Model):
    user = models.OneToOneField(User)
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
    )
    gender = models.CharField(max_length=10, choices=GENDER)
    national_id = models.PositiveIntegerField(blank=True)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=13)

    def __unicode__(self):
        return self.phone


class Routes(models.Model):
    source = models.CharField(max_length=100, )
    destination = models.CharField(max_length=100, )
    fare = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Routes'

    def __unicode__(self):
        return "{0} To {1}".format(self.source, self.destination)


class Vehicle(models.Model):
    TIME_CHOICES = (
        ('6.00 AM', '6.00 AM'),
        ('8.00 AM', '8.00 AM'),
        ('10.00 AM', '10.00 AM'),
        ('12.00 PM', '12.00 AM'),
        ('3.00 PM', '3.00 PM'),
        ('4.00 PM', '4.00 PM'),
        ('6.00 PM', '6.00 PM'),
        ('8.00 PM', '8.00 PM'),
        ('10.00 PM', '10.00 PM'),
    )

    VEHICLE_CAT = (
        ('14 Seater', '14 Seater'),
        ('Mini-Bus', 'Mini-Bus'),
        ('Bus', 'Bus')
    )

    route = models.ForeignKey(Routes, )
    plate_no = models.CharField(max_length=20)
    capacity = models.PositiveIntegerField()
    available_capacity = models.PositiveIntegerField(default=0)
    vehicle_model = models.CharField(max_length=30)
    vehicle_category = models.CharField(max_length=20, choices=VEHICLE_CAT)
    image = models.ImageField(upload_to='vehicles/img/', blank=True, null=True)
    is_online = models.BooleanField(default=False)
    is_departed = models.BooleanField(default=False)
    departing_time = models.CharField(max_length=8, choices=TIME_CHOICES)

    def __unicode__(self):
        return "Plate No: {0}, Model: {1}".format(self.plate_no, self.vehicle_model)


class Booking(models.Model):
    passager = models.ForeignKey(Passager, )
    vehicle = models.ForeignKey(Vehicle, )
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    seat_no = models.PositiveIntegerField(default=0)
    ticket_no = models.CharField(max_length=20, blank=True, null=True)
    amount_paid = models.PositiveIntegerField()
    date_booked = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.passager)


class Payment(models.Model):
    PAYMENT_CHOICES = (
        ('Fare', 'Fare'),
        ('Parcel', 'Parcel'),
        ('Other', 'Other'),
    )
    transaction_id = models.CharField(max_length=128)
    phone_no = models.CharField(max_length=13)
    payment_mode = models.CharField(max_length=20)
    payment_for = models.CharField(max_length=32, choices=PAYMENT_CHOICES, default=PAYMENT_CHOICES[0][0])
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=32)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.transaction_id


class ParcelFee(models.Model):
    PARCEL_TYPE = (
        ('Parcel', 'Parcel'),
        ('Luggage', 'Luggage'),
    )
    route = models.ForeignKey(Routes, )
    parcel_type = models.CharField(max_length=32, choices=PARCEL_TYPE)
    parcel_fee = models.DecimalField("Parcel Fee (Ksh)", max_digits=10, decimal_places=2, default=0.00)

    def __unicode__(self):
        return self.parcel_type


class Travelling(models.Model):
    vehicle = models.ForeignKey(Vehicle, )
    source = models.CharField(max_length=128)
    destination = models.CharField(max_length=128)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __unicode__(self):
        return str(self.vehicle)


class Parcel(models.Model):
    sender_full_name = models.CharField(max_length=128)
    sender_phone_no = models.CharField(max_length=13)
    sender_national_id = models.PositiveIntegerField()
    receiver_phone_no = models.CharField(max_length=13)
    receiver_national_id = models.PositiveIntegerField()
    parcel_description = models.TextField(max_length=140)
    route = models.ForeignKey(Routes, )

    def __unicode__(self):
        return "Parcel from {0} to {1}".format(self.sender_full_name, self.receiver_phone_no)

