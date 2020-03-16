import unittest
import json
from EasySAV.UserInterfaces.app import app


class TestServer(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.app = app.test_client()
        self.assertEqual(app.debug, True)

    def test_list_interventions(self):
        response = self.app.get('/interventions', follow_redirects = False)
        self.assertEqual(json.loads(response.data)[1]["piece"], "télé")
        self.assertEqual(response.status_code, 200)

    def test_add_intervention(self):
        response = self.app.post('/add', data= json.dumps({'ref_client':123457, 'code': 4455,
                                                           'piece':'robot v3',
                                                           'probleme':'corona ',
                                                           'matricule':22}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)




