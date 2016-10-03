from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^payment/parcel/$', views.pay_parcel_fee, name='parcel_fee'),
]
