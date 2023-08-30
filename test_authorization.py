import unittest
import authorization

class TestAuthorization(unittest.TestCase):
    
    def test_creating_new_user(self):
        self.assertEqual(authorization.creating_new_user("Nikigasdta", "123325"))


if __name__ == "__main__":
    unittest.main()