# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MatatuBooking(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    amount_paid = models.PositiveIntegerField()
    date_booked = models.DateTimeField()
    passager = models.ForeignKey('MatatuPassager', models.DO_NOTHING)
    vehicle = models.ForeignKey('MatatuVehicle', models.DO_NOTHING)
    seat_no = models.PositiveIntegerField()
    ticket_no = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matatu_booking'


class MatatuDriver(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    gender = models.CharField(max_length=10)
    national_id = models.PositiveIntegerField()
    license = models.CharField(unique=True, max_length=100)
    phone = models.CharField(max_length=13)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'matatu_driver'


class MatatuParcel(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sender_full_name = models.CharField(max_length=128)
    sender_phone_no = models.CharField(max_length=13)
    sender_national_id = models.PositiveIntegerField()
    receiver_phone_no = models.CharField(max_length=13)
    receiver_national_id = models.PositiveIntegerField()
    parcel_description = models.TextField()
    route = models.ForeignKey('MatatuRoutes', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'matatu_parcel'


class MatatuParcelfee(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    parcel_type = models.CharField(max_length=32)
    parcel_fee = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    route = models.ForeignKey('MatatuRoutes', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'matatu_parcelfee'


class MatatuPassager(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    gender = models.CharField(max_length=10)
    national_id = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=13)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'matatu_passager'


class MatatuPayment(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    transaction_id = models.CharField(max_length=128)
    phone_no = models.CharField(max_length=13)
    payment_mode = models.CharField(max_length=20)
    payment_for = models.CharField(max_length=32)
    amount = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    status = models.CharField(max_length=32)
    transaction_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'matatu_payment'


class MatatuRoutes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    fare = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'matatu_routes'


class MatatuTravelling(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    source = models.CharField(max_length=128)
    destination = models.CharField(max_length=128)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    vehicle = models.ForeignKey('MatatuVehicle', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'matatu_travelling'


class MatatuVehicle(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    plate_no = models.CharField(max_length=20)
    capacity = models.PositiveIntegerField()
    available_capacity = models.PositiveIntegerField()
    vehicle_model = models.CharField(max_length=30)
    vehicle_category = models.CharField(max_length=20)
    is_online = models.BooleanField()
    is_departed = models.BooleanField()
    departing_time = models.CharField(max_length=8)
    route = models.ForeignKey(MatatuRoutes, models.DO_NOTHING)
    image = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matatu_vehicle'
