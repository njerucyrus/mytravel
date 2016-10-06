from django.contrib import admin
from matatu.models import *


class DriverAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'national_id', 'license', 'phone']

    class Meta:
        model = Driver


admin.site.register(Driver, DriverAdmin)


class PassagerAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'national_id', 'phone']

    class Meta:
        model = Passager


admin.site.register(Passager, PassagerAdmin)


class RoutesAdmin(admin.ModelAdmin):
    list_display = ['id', 'source', 'destination', 'fare']

    class Meta:
        model = Routes


admin.site.register(Routes, RoutesAdmin)


class VehicleAdmin(admin.ModelAdmin):
    list_display = ['route', 'plate_no', 'capacity', 'vehicle_model', 'vehicle_category', 'is_online', 'is_departed', 'departing_time', 'image']

    class Meta:
        model = Vehicle


admin.site.register(Vehicle, VehicleAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['transaction_id', 'phone_no', 'payment_mode', 'payment_for', 'amount', 'status', 'transaction_date']

    class Meta:
        model = Payment


admin.site.register(Payment, PaymentAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display = ['ticket_no','passager', 'vehicle', 'source', 'destination', 'amount_paid', 'date_booked']

    class Meta:
        model = Booking

admin.site.register(Booking, BookingAdmin)


class ParcelAdmin(admin.ModelAdmin):
    list_display = ['sender_full_name',
                    'sender_national_id',
                    'sender_phone_no',
                    'receiver_phone_no',
                    'receiver_national_id',
                    'parcel_description',
                    'route',
                    ]

    class Meta:
        model = Parcel
admin.site.register(Parcel, ParcelAdmin)


class ParcelFeeAdmin(admin.ModelAdmin):
    list_display = ['route', 'parcel_type', 'parcel_fee']

    class Meta:
        model = ParcelFee
admin.site.register(ParcelFee, ParcelFeeAdmin)