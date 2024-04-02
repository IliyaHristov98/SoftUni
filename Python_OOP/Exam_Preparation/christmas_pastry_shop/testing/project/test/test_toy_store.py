from unittest import TestCase, main

from project.toy_store import ToyStore


class TestToyStore(TestCase):

    def setUp(self):
        self.store = ToyStore()

    def test_correct_init(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)

    def test_add_toy_raises_exception_shelf_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("Z", None)
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_raises_exception_toy_is_already_in_shelf(self):
        self.store.toy_shelf = {
            "A": "Puppy",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Puppy")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_raises_exception_toy_is_already_in_shelf(self):
        self.store.toy_shelf = {
            "A": "Puppy",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Kitty")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_works_correctly(self):
        result = self.store.add_toy("A", "Puppy")
        self.assertEqual('Puppy', self.store.toy_shelf['A'])
        self.assertEqual(f"Toy:Puppy placed successfully!", result)

    def test_remove_toy_raises_exception_shelf_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("Z", None)
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_raises_exception_shelf_does_not_exist(self):
        self.store.toy_shelf = {
            "A": "Puppy",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "Kitty")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_works_correctly(self):
        self.store.toy_shelf = {
            "A": "Puppy",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        result = self.store.remove_toy("A", "Puppy")
        self.assertEqual(None, self.store.toy_shelf["A"])
        self.assertEqual("Remove toy:Puppy successfully!", result)


if __name__ == '__main__':
    main()
