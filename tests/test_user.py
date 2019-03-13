import unittest
import json
from app import app, db


class UserTestCase(unittest.TestCase):
    """This class represents the User test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.client = app.test_client
        self.user = {'name': 'test', 'lastname': 'test', 'login': 'test', 'desc': 'test'}

    def test_user_creation(self):
        """Test API can create a User (POST request)"""
        res = self.client().post('/users', json=self.user)
        self.assertEqual(res.status_code, 201)
        
        self.assertIn('test', str(res.data))
        
    def tearDown(self):
        """teardown all initialized variables."""
        with app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()