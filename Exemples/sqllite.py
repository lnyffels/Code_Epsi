import sqlite3

class ManageSqlLite:
    def __init__(self, baseName):
        self.conn = sqlite3.connect(baseName)
        self.cursor = self.conn.cursor()

    def create_table(self, tableName):
        sqlCmd = f"CREATE TABLE IF NOT EXISTS {tableName}(" \
                 f" id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE," \
                 f" name TEXT," \
                 f" age INTEGER)"
        self.execute_commande(sqlCmd)

    def execute_commande(self, sqlCommand):
        self.cursor.execute(sqlCommand)

    def return_liste_record(self, sqlSelectCommand):
        lstRecords = []
        self.execute_commande(sqlSelectCommand)
        for row in self.cursor:
            lstRecords.append('{0} : {1}'.format(row[0], row[1]))
        return lstRecords

    def commit(self):
        self.conn.commit()

    def insert_person_in_database(self, pers):
        self.cursor.execute("""INSERT INTO users(name, age) VALUES(:name, :age)""", pers)


bdd = ManageSqlLite("ma_base.db")
bdd.create_table("users")
list_person = []
list_person.append({"name": "Laurent", "age": 46})
list_person.append({"name": "Greg", "age": 42})
list_person.append({"name": "Clément", "age": 28})
for pers in list_person:
    bdd.insert_person_in_database(pers)
bdd.commit()
lst = bdd.return_liste_record("SELECT * FROM users")
print(lst)

#
# cursor.execute("""
# DROP TABLE users
# """)
# conn.commit()
