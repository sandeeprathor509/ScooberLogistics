from faker import Faker

fake = Faker()


def GenerateBooking():
    firstname = fake.first_name()
    lastname = fake.last_name()
    total_price = fake.random.choice([230, 450, 670, 120, 500, 800])
    deposit_paid = fake.random.choice([True, False])
    checkin = fake.random.choice(['2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01', '2023-06-10'])
    checkout = fake.random.choice(['2023-02-5', '2023-03-05', '2023-04-05', '2023-05-05', '2023-06-20'])
    additional_needs = fake.random.choice(['Breakfast', 'Lunch', 'Water', 'Dinner'])

    return (
        {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": total_price,
            "depositpaid": deposit_paid,
            "bookingdates": {
                "checkin": checkin,
                "checkout": checkout
            },
            "additionalneeds": additional_needs
        }
    )
