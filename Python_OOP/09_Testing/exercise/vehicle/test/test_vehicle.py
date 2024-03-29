from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(100.0, 300.0)

    def test_init(self):
        self.assertEqual(100.0, self.vehicle.fuel)
        self.assertEqual(100.0, self.vehicle.capacity)
        self.assertEqual(300.0, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_method_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_method_correct(self):
        self.vehicle.drive(8)
        self.assertEqual(90, self.vehicle.fuel)

    def test_refuel_method_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_method_works_correct(self):
        self.vehicle.fuel = 50
        self.vehicle.refuel(40)
        self.assertEqual(90, self.vehicle.fuel)

    def test_str_method_works_correct(self):
        expected_result = f"The vehicle has 300.0 horse power with 100.0 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_result, str(self.vehicle))


if __name__ == "__main__":
    main()
