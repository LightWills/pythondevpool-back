import unittest
import json
from ..app import create_app, db


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

    def test_user_creation(self):
        """Test API can create a User (POST request)"""
        res = self.client().post('/users', json=self.user)
        self.assertEqual(res.status_code, 201)
        
        self.assertIn('test', str(res.data))
        
    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

