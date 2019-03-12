import unittest
import json
from . import create_app, db


class UserTestCase(unittest.TestCase):
    """This class represents the User test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.user = {'name': 'test', 'lastname': 'test', 'login': 'test', 'desc': 'test'}

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_bucketlist_creation(self):
        """Test API can create a User (POST request)"""
        res = self.client().post('/users', json=self.user)
        self.assertEqual(res.status_code, 201)

if __name__ == "__main__":
    unittest.main()