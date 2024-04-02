from unittest import TestCase, main

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):

    def setUp(self):
        self.car = SecondHandCar("VW", "Golf", 100000, 5000)

    def test_correct_init(self):
        self.assertEqual("VW", self.car.model)
        self.assertEqual("Golf", self.car.car_type)
        self.assertEqual(100000, self.car.mileage)
        self.assertEqual(5000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1.0
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_promotional_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(5000)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_work_correctly(self):
        result = self.car.set_promotional_price(4500)
        self.assertEqual(4500, self.car.price)
        self.assertEqual('The promotional price has been successfully set.', result)

    def test_need_repair_price_too_high(self):
        result = self.car.need_repair(2501, "Brakes")
        self.assertEqual('Repair is impossible!', result)

    def test_need_repair_works_correctly(self):
        result = self.car.need_repair(500, "Brakes")
        self.assertEqual(5500, self.car.price)
        self.assertEqual(["Brakes"], self.car.repairs)
        self.assertEqual('Price has been increased due to repair charges.', result)

    def test_gt_type_mismatch(self):
        self.other = SecondHandCar("VW", "Bora", 100000, 6000)
        result = self.car.__gt__(self.other)
        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test_gt_same_types(self):
        self.other = SecondHandCar("VW", "Golf", 100000, 6000)
        result = self.car.__gt__(self.other)
        self.assertFalse(result)

    def test_str_returns_correct_result(self):
        expected = f"""Model {self.car.model} | Type {self.car.car_type} | Milage {self.car.mileage}km
Current price: {self.car.price:.2f} | Number of Repairs: {len(self.car.repairs)}"""
        self.assertEqual(expected, self.car.__str__())


if __name__ == '__main__':
    main()
