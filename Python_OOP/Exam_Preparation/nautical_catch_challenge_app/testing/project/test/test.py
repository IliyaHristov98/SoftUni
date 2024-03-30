from unittest import TestCase, main
from collections import deque

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.station = RailwayStation("Elin Pelin")
        self.arrival_trains = deque()
        self.departure_trains = deque()

    def test_check_init(self):
        self.assertEqual("Elin Pelin", self.station.name)
        self.assertEqual(deque([]), self.station.arrival_trains)
        self.assertEqual(deque([]), self.station.departure_trains)

    def test_name_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "Bov"
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_name_setter_works_correctly(self):
        self.station.name = "Poduyane"
        self.assertEqual("Poduyane", self.station.name)

    def test_new_arrival_on_board_method(self):
        self.station.new_arrival_on_board("Plovdiv")
        self.assertEqual(self.station.arrival_trains, deque(["Plovdiv"]))

    def test_train_has_arrived_train_before_case(self):
        self.station.new_arrival_on_board("Plovdiv")
        result = self.station.train_has_arrived("Varna")
        self.assertEqual(f"There are other trains to arrive before Varna.", result)

    def test_train_has_arrived_there_is_arrival_before_but_is_the_same(self):
        self.station.new_arrival_on_board("Plovdiv")
        result = self.station.train_has_arrived("Plovdiv")
        self.assertEqual(f"Plovdiv is on the platform and will leave in 5 minutes.", result)

    def test_train_has_left_test_true(self):
        self.station.departure_trains.append("Varna")
        self.assertTrue(self.station.train_has_left("Varna"))

    def test_train_has_left_test_false_no_departures(self):
        self.assertFalse(self.station.train_has_left("Varna"))

    def test_train_has_left_test_false_not_first_in_line(self):
        self.station.departure_trains.append("Varna")
        self.assertFalse(self.station.train_has_left("Plovdiv"))


if __name__ == '__main__':
    main()
