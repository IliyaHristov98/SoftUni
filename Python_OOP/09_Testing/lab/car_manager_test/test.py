from unittest import TestCase, main

from car_manager_test.car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car("BMW", "M5", 20, 60)

    def test_init_correct(self):
        self.assertEqual("BMW", self.car.make)
        self.assertEqual("M5", self.car.model)
        self.assertEqual(20, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -5

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_method_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_method_correct(self):
        self.car.refuel(70)
        self.assertEqual(60, self.car.fuel_amount)

    def test_drive_method_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_method_works_correctly(self):
        self.car.fuel_amount = 60
        self.car.drive(100)
        self.assertEqual(40, self.car.fuel_amount)


if __name__ == "__main__":
    main()
