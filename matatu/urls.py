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
    url(r'^send-parcel/$', views.send_parcel, name='send_parcel'),
    url(r'^send-parcel/success/$', views.send_parcel_success, name='parcel_success'),
]
