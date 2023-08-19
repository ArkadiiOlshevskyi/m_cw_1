import task_3
import unittest


class TestTask3(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(task_3.greet(""), "Welcome")

    def test_known_language(self):
        self.assertEqual(task_3.greet("french"), "Bienvenue")

    def test_unknown_language(self):
        self.assertEqual(task_3.greet("molusque"), "Welcome")

    def test_case_sensitivity(self):
        self.assertEqual(task_3.greet("FRENCH"), "Bienvenue")

    def test_invalid_input(self):
        self.assertEqual(task_3.greet("IP_ADDRESS_INVALID"), "Welcome")
        self.assertEqual(task_3.greet("IP_ADDRESS_NOT_FOUND"), "Welcome")
        self.assertEqual(task_3.greet("IP_ADDRESS_REQUIRED"), "Welcome")


if __name__ == 'main':
    unittest.main()