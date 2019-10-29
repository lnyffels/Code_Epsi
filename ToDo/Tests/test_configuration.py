from unittest import TestCase
from ..configuration import FlaskConfig, Configuration

class TestConfiguration(TestCase):
    def test__get_value(self):
        # Arrange
        conf = FlaskConfig()
        add_url= "http://127.0.0.1:5000/add"
        root_url= "http://127.0.0.1:5000/"
        api_url= "http://127.0.0.1:5000/api"
        list_url= "http://127.0.0.1:5000/items"
        log_directory= "c:\\temp"

        # Act
        s_add_url = conf.url_add
        s_root_url = conf.url_root
        s_api_url = conf.url_api
        s_list_url = conf.url_list
        s_log_directory = conf.log_directory

        # Assert
        self.assertEqual(add_url, s_add_url)
        self.assertEqual(root_url, s_root_url)
        self.assertEqual(api_url, s_api_url)
        self.assertEqual(list_url, s_list_url)
        self.assertEqual(log_directory, s_log_directory)

    def test_bad_property_name(self):
        conf = FlaskConfig()
        bad_url = "http://mauvaise_url"

        with self.assertRaises(Exception) as cm:
            conf._get_value(bad_url)
        the_exception = cm.exception
        self.assertEqual(the_exception.args[0], "Nom de propriété inconnu" )