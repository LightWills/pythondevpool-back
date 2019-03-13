import unittest
import json
from app import app, db


class UserTestCase(unittest.TestCase):
    """This class represents the User test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.client = app.test_client
        self.user = {'name': 'my_name', 'lastname': 'my_lastname', 'login': 'my_login', 'desc': 'my_desc'}
        with app.app_context():
            db.create_all()

    def test_user_creation(self):
        """Test API can create a User (POST request)"""
        res = self.client().post('/users', json=self.user)
        data = str(res.data)
        self.assertEqual(res.status_code, 201)
        self.assertIn('"name": "my_name"', data)
        self.assertIn('"lastname": "my_lastname"', data)
        self.assertIn('"login": "my_login"', data)
        self.assertIn('"desc": "my_desc"', data)
        
    def tearDown(self):
        """teardown all initialized variables."""
        with app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()