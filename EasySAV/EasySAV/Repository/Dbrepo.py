import sqlite3
from ..Domain.Intervention import Intervention
from ..Domain.Technicien import Technicien

class Dbrepo:
    def __init__(self, connection_string):
        self.__conn = sqlite3.connect(connection_string)
        self.__cursor = self.__conn.cursor()


    def create_table(self, sqlCmd):
        self.__execute_commande(sqlCmd)
        return True

    def __execute_commande(self, sqlCommand):
        self.__cursor.execute(sqlCommand)

    def __commit(self):
        self.__conn.commit()

    def get_all_interventions(self):
        lst = []
        self.__execute_commande("SELECT * FROM INTERVENTION")
        for row in self.__cursor:
            lst.append(Intervention(row[1], row[0], row[2], row[3]).to_dict())
        return lst

    def save(self, interv_to_save):
        insertCmd = f"INSERT INTO INTERVENTION(ref_client," \
                    f"                 code," \
                    f"                 piece," \
                    f"                 probleme," \
                    f"                  matricule) " \
                    f"VALUES('{interv_to_save.ref_client}'," \
                    f"       '{interv_to_save.code}',"\
                    f"       '{interv_to_save.piece}'," \
                    f"       '{interv_to_save.probleme}',"\
                    f"       '22')"
        self.__execute_commande(insertCmd)
        self.__commit()
        return True
