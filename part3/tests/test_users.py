import unittest
from app import create_app  # Make sure to import your app factory

class UserAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        response = self.client.post('/api/v1/users/', json={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com'
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
