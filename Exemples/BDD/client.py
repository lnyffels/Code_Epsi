from Exemples.BDD.api_banque import APIBanque

class Client:
    def __init__(self, login, password, num_client):
        self.__login = login
        self.__password = password
        self.__num_client = num_client
        self.__comptes = []

    @property
    def Comptes(self):
        # Appel API Banque
        api = APIBanque()
        self.__comptes = api.get_liste_comptes(self.__num_client)
        return  self.__comptes








