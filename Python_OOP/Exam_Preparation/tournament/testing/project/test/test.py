from unittest import TestCase, main

from project.trip import Trip


class TestTrip(TestCase):

    def setUp(self):
        self.trip = Trip(5000, 5, False)

    def test_correct_init(self):
        self.assertEqual(5000, self.trip.budget)
        self.assertEqual(5, self.trip.travelers)
        self.assertFalse(self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_travelers_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0
        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_is_family_setter_false(self):
        is_family = Trip(1000, 1, True)
        self.assertFalse(is_family.is_family)

    def test_is_family_setter_gets_value(self):
        self.trip.is_family = "abc"
        self.assertEqual("abc", self.trip.is_family)

    def test_book_a_trip_destination_unknown(self):
        result = self.trip.book_a_trip("Spain")
        expected = 'This destination is not in our offers, please choose a new one!'
        self.assertEqual(expected, result)

    def test_book_a_trip_budget_not_enough(self):
        result = self.trip.book_a_trip("Australia")
        self.assertEqual('Your budget is not enough!', result)

    def test_book_a_trip_not_family_correct_price(self):
        result = self.trip.book_a_trip("Bulgaria")
        expected = f'Successfully booked destination Bulgaria! Your budget left is 2500.00'
        self.assertEqual(2500, self.trip.budget)
        self.assertEqual({"Bulgaria": 2500}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(expected, result)

    def test_book_a_trip_is_family_correct_price(self):
        self.trip.is_family = True
        self.trip.travelers = 2
        result = self.trip.book_a_trip("Bulgaria")
        expected = f'Successfully booked destination Bulgaria! Your budget left is 4100.00'
        self.assertEqual(4100, self.trip.budget)
        self.assertEqual({"Bulgaria": 900}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(expected, result)

    def test_book_a_trip_with_exact_budget(self):
        self.trip.budget = 2500
        result = self.trip.book_a_trip("Bulgaria")
        expected = f'Successfully booked destination Bulgaria! Your budget left is 0.00'
        self.assertEqual(expected, result)

    def test_booking_status_no_bookings(self):
        result = self.trip.booking_status()
        self.assertEqual(f'No bookings yet. Budget: {self.trip.budget:.2f}', result)

    def test_booking_status_correct_result(self):
        self.trip.book_a_trip("Bulgaria")
        result = self.trip.booking_status()
        expected = [
            f"""Booked Destination: Bulgaria\nPaid Amount: 2500.00""",
            f"""Number of Travelers: 5\nBudget Left: 2500.00""",
        ]
        self.assertEqual("\n".join(expected), result)


if __name__ == '__main__':
    main()
