import requests
from Conf.configurationtest import TestData
from utilities.generate_bookings import GenerateBooking


def _url(path):
    return TestData.BASE_URI + path


def get_bookings(firstname="", lastname="", checkin="", checkout=""):
    payload = {}
    if firstname:
        payload['firstname'] = firstname
    if lastname:
        payload['lastname'] = lastname
    if checkin:
        payload['checkin'] = checkin
    if checkout:
        payload['checkout'] = checkout

    if payload:
        return requests.get(_url('/booking/'), params=payload)
    else:
        return requests.get(_url('/booking/'))


def describe_booking(booking_id):
    return requests.get(_url('/booking/{:d}/'.format(booking_id)))


def add_random_booking():
    return add_booking(GenerateBooking())


def add_booking(booking):
    return requests.post(_url('/booking/'), json=booking)


def remove_booking(booking_id, auth_token):
    return requests.delete(_url('/booking/{:d}/'.format(booking_id)), cookies={
        "token": auth_token
    })


def update_booking(booking_id, auth_token, request_dict):
    return requests.put(_url('/booking/{:d}/'.format(booking_id)), json={
        "firstname": request_dict['firstname'],
        "lastname": request_dict['lastname'],
        "totalprice": request_dict['totalprice'],
        "depositpaid": request_dict['depositpaid'],
        "bookingdates": {
            "checkin": request_dict['checkin'],
            "checkout": request_dict['checkout']
        },
        "additionalneeds": request_dict['additionalneeds']
    }, cookies={
        "token": auth_token
    })


def get_authtoken(username=TestData.USERNAME, password=TestData.PASSWORD):
    url = _url('/auth')
    return requests.post(url, json={
        "username": username,
        "password": password
    }).json()['token']
