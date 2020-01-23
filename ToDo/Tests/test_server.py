import unittest
import json
from ..server import app


class TestServer(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.app = app.test_client()
        self.assertEqual(app.debug, True)

    def test_home_root(self):
        response = self.app.get('/', follow_redirects = False)
        self.assertEqual(response.status_code, 200)

    def test_add_root(self):
        response = self.app.post('/add', data= json.dumps({'description':'ecrire scenarios python 3', 'status': 'ToDo'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)

