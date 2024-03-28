from unittest import TestCase, main

from list_test.list import IntegerList


class TestList(TestCase):

    def setUp(self) -> None:
        self.list = IntegerList(1, 2, 3)

    def test_init(self):
        self.assertEqual([1, 2, 3], self.list.get_data())

    def test_add_element_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.list.add(2.2)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_adding_element_correctly(self):
        self.list.add(9)
        self.assertEqual([1, 2, 3, 9], self.list.get_data())

    def test_remove_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.list.remove_index(4)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_correct_remove_index(self):
        self.list.remove_index(1)
        self.assertEqual([1, 3], self.list.get_data())

    def test_get_method_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.list.get(4)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_method_correct_outcome(self):
        self.assertEqual(2, self.list.get(1))

    def test_insert_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.list.insert(4, 2)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.list.insert(1, 3.5)
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_method_works_correctly(self):
        self.list.insert(0, 10)
        self.assertEqual([10, 1, 2, 3], self.list.get_data())

    def test_get_biggest_method(self):
        self.assertEqual(3, self.list.get_biggest())

    def test_get_index_method(self):
        self.assertEqual(1, self.list.get_index(2))


if __name__ == "__main__":
    main()
