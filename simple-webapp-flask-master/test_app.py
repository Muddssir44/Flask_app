import unittest
from app import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_welcome_message(self):
        response = self.app.get('/')
        expected_message = app.view_functions['welcome']()  # Dynamically retrieve the message
        self.assertEqual(response.data, expected_message.encode())

if __name__ == '__main__':
    unittest.main()
