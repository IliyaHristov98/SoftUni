from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("Tom")

    def test_correct_init(self):
        self.assertEqual("Tom", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_enroll_if_course_exists(self):
        self.student.courses = {"Abc": ["a"]}
        result = self.student.enroll("Abc", ["b", "c"])
        self.assertEqual({"Abc": ["a", "b", "c"]}, self.student.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_course_does_not_exist_without_third_param(self):
        result = self.student.enroll("Abc", ["a", "b", "c"])
        self.assertEqual({"Abc": ["a", "b", "c"]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_course_does_not_exist_with_third_param(self):
        result = self.student.enroll("Abc", ["a", "b", "c"], "Y")
        self.assertEqual({"Abc": ["a", "b", "c"]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_last_case(self):
        result = self.student.enroll("Abc", ["a", "b", "c"], "N")
        self.assertEqual({"Abc": []}, self.student.courses)
        self.assertEqual("Course has been added.", result)

    def test_add_notes_updates_notes(self):
        self.student.courses = {"Abc": ["1"]}
        result = self.student.add_notes("Abc", "a")
        self.assertEqual({"Abc": ["1", "a"]}, self.student.courses)
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Abc", "a")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_works_correctly(self):
        self.student.courses = {"abc": [1, 2]}
        result = self.student.leave_course("abc")
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("abc")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
