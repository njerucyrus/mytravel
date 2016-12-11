from django.shortcuts import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from matatu.forms import *
from matatu.models import *
import weasyprint
from django.db.models import Q
from django.conf import settings
from matatu.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

def register_passager(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        passager_form = PassagerForm(request.POST)

        if user_form.is_valid() and passager_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            cd = passager_form.cleaned_data
            passager = Passager.objects.create(
                user=new_user,
                gender=cd['gender'],
                national_id=cd['national_id'],
                age=cd['age'],
                phone=cd['phone']
            )
            passager.save()
            message = "Account created successfully"
            return render_to_response('matatuapp/register_passager_success.html',
                                      {'message': message, })
    else:
        user_form = UserRegistrationForm()
        passager_form = PassagerForm()
    return render(request, 'matatuapp/register.html', {'user_form': user_form, 'passager_form': passager_form})


def user_login(request):
    user = request.user
    next_url = request.GET.get('next', '')
    if user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    request.session['username'] = cd['username']
                    login(request, user)
                    if next_url == '':
                        return HttpResponseRedirect('/')
                    elif next_url:
                        return HttpResponseRedirect(next_url)
            else:

                message = 'Wrong username or password'
                form = LoginForm()
                return render(request, 'matatuapp/login.html', {'form': form, 'message': message, })
    else:
        form = LoginForm()
    return render(request, 'matatuapp/login.html', {'form': form, })


@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    try:
        del request.session['username']
        request.session.modified = True
        return render(request, 'matatuapp/logout_then_login.html', {})
    except KeyError, e:
        pass
    return render(request, 'matatuapp/logout_then_login.html', {})


def index(request):
    return render(request, 'matatuapp/index.html', {})


def my_travel(request):
    vehicle = Vehicle.objects.filter(is_online=True, )
    return render(request, "matatuapp/my_travel.html", {'vehicles': vehicle, })


# this was not fully implemented will implement over the weekend
def vehicle_list_by_route(request, pk=None):
    route = None
    routes = Routes.objects.all()
    vehicles = Vehicle.objects.all()
    if pk:
        route = get_object_or_404(Routes, pk=pk)
        vehicles = vehicles.filter(route=route)
    return render(request, 'matatuapp/vehicle_list.html',
                  {
                      'route': route,
                      'routes': routes,
                      'vehicles': vehicles,
                  })


# search engine
def search(request):
    query = request.GET.get('q', '')
    if query:
        queryset = (
            Q(source__icontains=query) |
            Q(destination__icontains=query) |
            Q(fare__icontains=query)
        )
        route = Routes.objects.filter(queryset).distinct()
        results = Vehicle.objects.filter(route=route)
    else:
        results = []
    return render_to_response('matatuapp/vehicles.html', {
        'results': results,
        'query': query
    })


from random import randint


@login_required(login_url='/login/')
def book_seat(request, pk=None):
    vehicle = get_object_or_404(Vehicle, pk=pk, is_online=True)
    initial = {'amount': str(vehicle.route.fare), }
    if request.method == 'POST':

        form = SeatPaymentForm(request.POST, initial=initial)

        if form.is_valid():
            # create booking model instance and save it

            #create a booking session for  the values

            username = request.session.get('username', '')

            user = get_object_or_404(User, username=username)
            passager = get_object_or_404(
                Passager,
                user=user
            )

            source = vehicle.route.source
            destination = vehicle.route.destination
            amount_paid = form.cleaned_data['amount']
            phoneNumber = form.cleaned_data['phoneNumber']
            range_start = 10 ** (8 - 1)
            range_end = (10 ** 8) - 1
            ticket_no = randint(range_start, range_end)
            try:
                float_amt = float(amount_paid)
                debug = settings.DEBUG
                currencyCode = settings.CURRENCY_CODE
                metadata = settings.METADATA

                if debug:
                    username = str(settings.AT_USERNAME)
                    apiKey = str(settings.API_KEY)
                    productName = settings.PRODUCT_NAME
                    gateway = AfricasTalkingGateway(username, apiKey, "sandbox")

                else:
                    username = settings.AT_USERNAME
                    apiKey = settings.API_KEY
                    gateway = AfricasTalkingGateway(username, apiKey)
                    productName = settings.PRODUCT_NAME

                transactionId = gateway.initiateMobilePaymentCheckout(
                    productName,
                    phoneNumber,
                    currencyCode,
                    float_amt,
                    metadata
                )

                # create payment object

                payment = Payment.objects.create(
                    transaction_id=transactionId,
                    amount=amount_paid,
                    phone_no=phoneNumber,
                    payment_for='Fare',
                    payment_mode='Mpesa',
                    status='PendingConfirmation'
                )
                payment.save()

                #create booking instance
                booking = Booking.objects.create(
                    transaction_id=transactionId,
                    amount_paid=float_amt,
                    passager=passager,
                    vehicle=vehicle,
                    ticket_no=ticket_no,
                    source=source,
                    destination=destination,

                )
                booking.save()

                # booking_data = {'username': username, 'source': source, 'destination': destination,
                #                 'amount': float_amt, 'ticket_no': ticket_no, 'vehicle_pk': pk,
                #                 }
                #
                # request.session['booking'] = booking_data
                # #request.session.modified = True
                # encoded = json.dumps(json.dumps(request.session.get('booking')))
                # decoded = json.loads(encoded)
                # print "decoded first ", decoded

                message = "Transaction initiated successfully, please complete the payment on your mobile phone"
                return render(request, 'matatuapp/payment_success.html', {'message': message, })

            except AfricasTalkingGatewayException, e:
                print str(e)
                return HttpResponse('error occured:  {}'.format(str(e)))

    else:
        form = SeatPaymentForm(initial=initial)
    return render(request, 'matatuapp/book_seat.html', {'form': form, })


def my_ticket(request):
    username = request.session.get('username')
    user = get_object_or_404(User, username=username)
    passager = get_object_or_404(Passager, user=user)
    booking = get_object_or_404(Booking, passager=passager)
    return render(request, 'matatuapp/my_ticket.html', {'booking': booking, })


def passager_ticket(request, ticket_no=None):
    booking = get_object_or_404(Booking, ticket_no=ticket_no)
    html = render_to_string('matatuapp/ticket-pdf.html', {'booking': booking, })
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=myTravelTicket_{}.pdf'.format(booking.ticket_no)
    weasyprint.HTML(string=html).write_pdf(response,
                                           # stylesheets=[weasyprint.CSS(
                                           # settings.STATIC_ROOT + '/css/bootstrap.min.css',
                                           # )]
                                           )
    return response


@login_required(login_url='/login/')
def send_parcel(request):
    if request.method == 'POST':
        form = SendParcelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/payment/parcel/')

    else:
        form = SendParcelForm()
    return render(request, 'matatuapp/send_parcel.html', {'form': form, })


def send_parcel_success(request):
    message = "Your parcel details was recorded successfully" \
              "Its set ready for delivery. You will be contacted" \
              "to inform you of the delivery."
    return render_to_response('matatuapp/send_parcel_success.html', {'message': message, })


# for testing
def select_seat(request):
    return render(request, 'matatuapp/select_seat.html', {})


def show_vehicles(request):
    vehicles = Vehicle.objects.filter(is_online=True)
    return render(request, 'matatuapp/vehicles.html', {'vehicles': vehicles, })