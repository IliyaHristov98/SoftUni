from unittest import TestCase, main

from test_cat.cat import Cat


class CatTests(TestCase):

    def setUp(self) -> None:
        self.cat = Cat("Tom")

    def test_init_correct(self):
        self.assertEqual("Tom", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_eat_raises_exception(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_sleep_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_correct_eat_method(self):
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)
        self.assertTrue(self.cat.fed)
        self.assertEqual(1, self.cat.size)

    def test_correct_sleep_method(self):
        self.cat.sleepy = True
        self.cat.fed = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()
