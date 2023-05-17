import logging

import json
import Conf.httpresponses as http_response
from utilities.custom_logger import LogGen
from requestmodule import apis as API
from faker import Faker

fake = Faker()


class TestRest:
    """Each method is a test case"""
    # __test__ = False

    logger = LogGen.log_gen()
    logger.info("********** API Automation **********")

    def test_read_booking(self):
        """Verify the bookingid for already created person"""
        response = API.describe_booking(4)
        assert response.status_code == http_response.HTTP_OK, f"Booking id is not exist"

    def test_create_booking(self):
        """Verify the booking id for a random generated person"""
        response = API.add_random_booking()
        assert response.status_code == http_response.HTTP_OK, f"New randomly booking id generated"

    def test_update_booking(self):
        """Update the booking id for randomly generated person"""
        auth_token = API.get_authtoken()
        new_booking = API.add_random_booking().json()['bookingid']
        update_dict = dict(firstname=fake.first_name(),
                           lastname=fake.last_name(),
                           totalprice=fake.random.choice([120, 130, 140]),
                           depositpaid=fake.random.choice([True, False]),
                           checkin='2023-01-01',
                           checkout='2023-01-02',
                           additionalneeds=fake.random.choice(['Breakfast', 'Lunch', 'Water', 'Dinner']))
        response = API.update_booking(new_booking, auth_token, update_dict)
        assert response.status_code == http_response.HTTP_OK, f"Booking id is not updated"

    def test_delete_booking(self):
        """Remove the bookingid for a randomly generated person"""
        auth_token = API.get_authtoken()
        new_booking = API.add_random_booking().json()['bookingid']
        response = API.remove_booking(new_booking, auth_token)
        assert response.status_code == http_response.HTTP_CREATED, f"Bookingid not deleted"
