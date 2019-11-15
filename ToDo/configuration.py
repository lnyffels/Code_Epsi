conf = {
    'url_root' : "http://127.0.0.1:5000/",
    'url_api': "http://127.0.0.1:5000/api",
    'url_add' : "http://127.0.0.1:5000/add",
    'url_list' : "http://127.0.0.1:5000/items",
    'log_directory' : "c:\\temp"
}

class Configuration:
    def __init__(self):
        self.__config = conf

    def _get_value(self, property_name):
        if property_name not in self.__config.keys():
            raise Exception("Nom de propriété inconnu")
        else:
            return self.__config[property_name]


class FlaskConfig(Configuration):
    def __init__(self):
        super().__init__()


    @property
    def url_root(self):
        return self._get_value("url_root")

    @property
    def url_api(self):
        return self._get_value("url_api")

    @property
    def url_add(self):
        return self._get_value("url_add")

    @property
    def url_list(self):
        return self._get_value("url_list")

    @property
    def log_directory(self):
        return self._get_value("log_directory")