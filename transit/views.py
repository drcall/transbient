from django.shortcuts import render
import requests, re, os

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

    dev_url = 'https://api.devhub.virginia.edu/v1/transit/vehicles'
    dev_data = {'success': False}
    while not dev_data['success']:
        dev_data = requests.get(dev_url).json()
        print("Got vehicle locations")
    vehicles = dev_data['vehicles']
    for i in range(len(vehicles)):
        vehicles[i]['eta'] = get_eta(vehicles[i]['position'], loc)
    return vehicles

def get_eta(pos1, pos2):
    source = str(pos1)[1:-1]
    dest = str(pos2)[1:-1]
    google_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    google_data = requests.get(
        google_url + 'origins=' + source + '&destinations=' + dest + '&key=' + os.environ.get("GOOGLE_DISTANCE_MATRIX_API_KEY")).json()
    eta_str = google_data['rows'][0]['elements'][0]['duration']['text']
    eta_str2 = re.compile('\d+ min').search(eta_str)[0]
    return int(eta_str2[:-4])  # number of minutes
