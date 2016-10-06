from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register-passager/$', views.register_passager, name='register_passager'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^$', views.index, name='index'),  
    url(r'^my-travel/$', views.my_travel, name='my_travel'),
    url(r'^select-seat/$', views.select_seat, name='select_seat'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^book-seat/(?P<pk>\d+)/$', views.book_seat, name='book_seat'),
    url(r'^my-booking/$', views.my_ticket, name='my_ticket'),
    url(r'^my-booking/ticket/(?P<ticket_no>\d+)$', views.passager_ticket, name='ticket_pdf'),
    url(r'^send-parcel/$', views.send_parcel, name='send_parcel'),
    url(r'^send-parcel/success/$', views.send_parcel_success, name='parcel_success'),
    url(r'^vehicles/$', views.show_vehicles, name='vehicles'),
]
