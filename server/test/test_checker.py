
import unittest

from Utils.checker import Checker

checker = Checker()


class TestChecker(unittest.TestCase):

    def test_correct_service(self):
        self.assertTrue(checker.is_service_type_ok("timer"))

    def test_incorrect_service(self):
        self.assertFalse(checker.is_service_type_ok("facebook"))


if __name__ == "__main__":
    unittest.main()
