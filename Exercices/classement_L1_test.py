import unittest
import json
from Exercices.classement_L1 import app


class TestServer(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.app = app.test_client()
        self.assertEqual(app.debug, True)

    def test_interventions(self):
        response = self.app.get('/api/classement/allinterventions', follow_redirects = False)
        inters = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(inters[1]["client"], "gilles")

    def test_classement(self):
        response = self.app.get('/api/classement/', follow_redirects = False)
        s = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(s["titre"], "Classement Ligue 1")


    def test_add_root(self):
        response = self.app.post('/api/classement/add', data= json.dumps({'Equipe':'OL', 'points': '34'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)

