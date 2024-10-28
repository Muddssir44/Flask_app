import unittest
from app import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_welcome_message(self):
        response = self.app.get('/')
        expected_message = "Welcome to my Flask app! Enjoy exploring."
        self.assertEqual(response.data.decode(), expected_message)

if __name__ == '__main__':
    unittest.main()
