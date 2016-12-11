from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^payment/parcel/$', views.pay_parcel_fee, name='parcel_fee'),
    url(r'^notifications/$', views.get_mpesa_ipn, name='notifications'),
]
