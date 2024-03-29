from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("Tom", "Cat", "Meow")

    def test_correct_init(self):
        self.assertEqual("Tom", self.mammal.name)
        self.assertEqual("Cat", self.mammal.type)
        self.assertEqual("Meow", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_correct_make_sound_method(self):
        self.assertEqual(f"Tom makes Meow", self.mammal.make_sound())

    def test_correct_get_kingdom_method(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_method(self):
        self.assertEqual(f"Tom is of type Cat", self.mammal.info())


if __name__ == "__main__":
    main()
