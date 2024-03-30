from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestRobot(TestCase):

    def setUp(self):
        self.robot = ClimbingRobot("Mountain", "Test", 100, 100)
        self.robot_with_software = ClimbingRobot("Alpine", "Test", 100, 100)
        self.robot_with_software.installed_software = [
            {'name': 'AMD', 'memory_consumption': 20, 'capacity_consumption': 30},
            {'name': 'NVIDIA', 'memory_consumption': 10, 'capacity_consumption': 20}
        ]

    def test_climbing_robot_structure(self):
        self.assertEqual(ClimbingRobot.__base__.__name__, "object")
        self.assertTrue(hasattr(ClimbingRobot, "get_used_capacity"))
        self.assertTrue(hasattr(ClimbingRobot, "get_available_capacity"))
        self.assertTrue(hasattr(ClimbingRobot, "get_used_memory"))
        self.assertTrue(hasattr(ClimbingRobot, "get_available_memory"))
        self.assertTrue(hasattr(ClimbingRobot, "install_software"))
        self.assertTrue(isinstance(getattr(ClimbingRobot, "category"), property))

    def test_correct_init(self):
        self.assertEqual("Mountain", self.robot.category)
        self.assertEqual("Test", self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(100, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_category_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Invalid"

        self.assertEqual(f"Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']", str(ve.exception))

    def test_category_setter_works_correctly(self):
        self.robot_test_two = ClimbingRobot("Indoor", "Test", 100, 100)
        self.assertEqual("Indoor", self.robot_test_two.category)

    def test_get_used_capacity_method(self):
        self.assertEqual(50, self.robot_with_software.get_used_capacity())

    def test_get_available_capacity_method(self):
        self.assertEqual(50, self.robot_with_software.get_available_capacity())

    def test_get_used_memory_method(self):
        self.assertEqual(30, self.robot_with_software.get_used_memory())

    def test_get_available_memory_method(self):
        self.assertEqual(70, self.robot_with_software.get_available_memory())

    def test_install_software_method_works_correctly(self):
        software = {'name': 'AMD', "memory_consumption": 40, "capacity_consumption": 30}
        result = self.robot.install_software(software)
        expected_result = f"Software '{software['name']}' successfully installed on {self.robot.category} part."
        self.assertEqual([software], self.robot.installed_software)
        self.assertEqual(expected_result, result)

    def test_install_software_method_works_correctly_exact_numbers(self):
        software = {'name': 'AMD', "memory_consumption": 100, "capacity_consumption": 100}
        result = self.robot.install_software(software)
        expected_result = f"Software '{software['name']}' successfully installed on {self.robot.category} part."
        self.assertEqual([software], self.robot.installed_software)
        self.assertEqual(expected_result, result)

    def test_install_software_method_fails_too_much_memory_used(self):
        software = {'name': 'AMD', "memory_consumption": 140, "capacity_consumption": 30}
        result = self.robot.install_software(software)
        expected_result = f"Software '{software['name']}' cannot be installed on {self.robot.category} part."
        self.assertEqual([], self.robot.installed_software)
        self.assertEqual(expected_result, result)

    def test_install_software_method_fails_too_much_consumption_used(self):
        software = {'name': 'AMD', "memory_consumption": 40, "capacity_consumption": 130}
        result = self.robot.install_software(software)
        expected_result = f"Software '{software['name']}' cannot be installed on {self.robot.category} part."
        self.assertEqual([], self.robot.installed_software)
        self.assertEqual(expected_result, result)

    def test_install_software_method_fails_for_both_conditions(self):
        software = {'name': 'AMD', "memory_consumption": 140, "capacity_consumption": 130}
        result = self.robot.install_software(software)
        expected_result = f"Software '{software['name']}' cannot be installed on {self.robot.category} part."
        self.assertEqual([], self.robot.installed_software)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
