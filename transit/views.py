from django.shortcuts import render
import requests, re, os
from .models import UserSettings, UserSettingsForm, Route, Vehicle, Stop
from django.http import HttpResponseRedirect
from twilio.rest import Client
from django.conf import settings
from decimal import Decimal

def get_long_lat():
    dev_url = "https://www.googleapis.com/geolocation/v1/geolocate?"
    ans = requests.post(dev_url+"key="+os.environ.get("GOOGLE_GEOLOCATION_API_KEY")).json()
    return ans['location']['lat'], ans['location']['lng']

def etas_to():
    return etas_to_loc(get_long_lat())
def etas_to_loc(loc):
    '''

    :param loc: (lat, long)
    :return: list of vehicles with fields from Devhub API + eta (number of minutes until bus reaches loc)
    '''

    create_or_update_vehicles()
    vehicles = []
    v_set = Vehicle.objects.all()
    for v in v_set:
        eta = get_eta((v.lat,v.long),loc)
        vehicles.append((v,eta))
    vehicles.sort(key=lambda k: k[1]) # sort by min to max eta
    return vehicles

def get_eta(pos1, pos2):
    get_str = lambda k: str(float(k[0]))+','+str(float(k[1]))
    source = get_str(pos1)
    dest = get_str(pos2)
    google_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    real_url = google_url + 'origins=' + source + '&destinations=' + dest + '&key=' + os.environ.get("GOOGLE_DISTANCE_MATRIX_API_KEY")
    # print(real_url)
    google_data = requests.get(real_url).json()
    # print(google_data)
    eta_str = google_data['rows'][0]['elements'][0]['duration']['text']
    eta_str2 = re.compile('\d+ min').search(eta_str)[0]
    return int(eta_str2[:-4])  # number of minutes

def dashboard_view(request):
    stops = Stop.objects.all().order_by('name')

    for stop in stops:
        stop.route_str = stop.format_routes()
        stop.save()
        
    return render(request, "transit/dashboard.html", {'stops': stops})

def settings_view(request):
    form = UserSettingsForm()
    return render(request, "transit/settings.html", {'form': form})

def change_settings(request):
    msg = "You have just added your phone number to your Transbient account! Stay updated on UTS here: https://transbient.herokuapp.com/"
    if request.method == 'POST':
        form = UserSettingsForm(request.POST)
        if form.is_valid():
            existing = UserSettings.objects.filter(user=request.user)
            for item in existing:
                item.delete()
            p_number = form.cleaned_data.get('phone')
            min_eta = form.cleaned_data.get('start')

            profile = UserSettings(user = request.user, phone = p_number, start = min_eta)
            profile.save()
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            client.messages.create(to=p_number.as_e164,
                                   from_=settings.TWILIO_NUMBER,
                                   body=msg)
            return HttpResponseRedirect('/transit')
        else:
            form = UserSettingsForm()
    return render(request, 'transit/settings.html', {'form': form, 'error_message': 'Something went wrong.'})


def create_routes():
    devhub_url = 'https://api.devhub.virginia.edu/v1/transit/routes'
    devhub_data = {'success': False}

    while not devhub_data['success']:
        devhub_data = requests.get(devhub_url).json()

    for route in devhub_data['routes']:
        r = Route(id=route['id'], is_active=route['is_active'], long_name=route['long_name'],
                  short_name=route['short_name'])
        r.save()

<<<<<<< HEAD
def update_stop_locations():
    devhub_url = 'https://api.devhub.virginia.edu/v1/transit/bus-stops'
    devhub_data = {'success': False}
    while not devhub_data['success']:
        devhub_data = requests.get(devhub_url).json()
    for stop in devhub_data['stops']:
        lat = Decimal("%.15f" % stop["position"][0])
        long = Decimal("%.15f" % stop["position"][1])
        s = Stop.objects.filter(id=stop['id'])[0]
        s.lat = lat
        s.long = long
        s.save()

=======
>>>>>>> 35a4d53 (Dashboard)
def create_stops():
    devhub_url = 'https://api.devhub.virginia.edu/v1/transit/bus-stops'
    devhub_data = {'success': False}

    while not devhub_data['success']:
        devhub_data = requests.get(devhub_url).json()

    for stop in devhub_data['stops']:
<<<<<<< HEAD
        lat = Decimal("%.15f" % stop["position"][0])
        long = Decimal("%.15f" % stop["position"][1])
        s = Stop(id=stop['id'],name=stop['name'],lat=lat,long=long,code=int(stop["code"]))
        s.save()


    for route in devhub_data['routes']:
        r = Route.objects.filter(id=route['id'])[0]
        for stop_id in route['stops']:
            try:
                s = Stop.objects.filter(id=stop_id)[0]
                s.routes.add(r)
            except IndexError:
                continue


def create_or_update_vehicles():
    devhub_url = 'https://api.devhub.virginia.edu/v1/transit/vehicles'
    devhub_data = {'success': False}

    while not devhub_data['success']:
        devhub_data = requests.get(devhub_url).json()

    for veh in devhub_data['vehicles']:
        veh_set = Vehicle.objects.filter(id=veh['id'])
        lat = Decimal("%.15f" % veh["position"][0])
        long = Decimal("%.15f" % veh["position"][1])
        r = Route.objects.filter(id=veh['route_id'])[0]
        if len(veh_set) == 0:
            v = Vehicle(id=veh['id'],call_name=veh['call_name'],long=long,lat=lat,service_status=veh['service_status'],route_id=r)
            v.save()
        else:
            v = veh_set[0]
            v.lat = lat
            v.long = long
            v.route_id = r
            v.service_status = veh['service_status']
            v.save()

def buses_near_stop(stop_id):
    s = Stop.objects.filter(id=stop_id)[0]
    vehicles = etas_to_loc((s.lat,s.long))
    route_vehicles = []
    routes = s.routes.all()
    for v,eta in vehicles:
        if v.route_id in routes:
            route_vehicles.append((v,eta))
    return vehicles
=======
        s = Stop(id=stop['id'],name=stop['name'],lat=stop["position"][0],long=stop["position"][1],code=int(stop["code"]))
        s.save()

    for route in devhub_data['routes']:
        continue

>>>>>>> 35a4d53 (Dashboard)
