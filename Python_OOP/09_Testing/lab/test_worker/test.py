from unittest import TestCase, main

from test_worker.worker import Worker


class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker("Iliya", 3000, 100)

    def test_correct_init(self):
        self.assertEqual("Iliya", self.worker.name)
        self.assertEqual(3000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_rest_method(self):
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_error_raised_for_negative_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_salary_increase(self):
        self.worker.work()
        self.assertEqual(3000, self.worker.money)

    def test_energy_after_working(self):
        self.worker.work()
        self.assertEqual(99, self.worker.energy)

    def test_get_info(self):
        result = self.worker.get_info()
        self.assertEqual(f'Iliya has saved 0 money.', result)


if __name__ == "__main__":
    main()
