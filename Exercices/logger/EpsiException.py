import os
import datetime

class EpsiException(Exception):
    def __init__(self, exc, code_erreur, message_erreur):
        super().__init__(exc)
        self.__inner_exception = exc
        self.__code_erreur = code_erreur
        self.__message_erreur = message_erreur
        os.chdir("c:\\temp")
        self.__log_in_file()

    def __log_in_file(self):
        error_file = open("epsi_error.txt", "a")
        error_file.write(self.__format_error())

    def __format_error(self):
        return str(datetime.datetime.now()) + " " +str(self.__inner_exception) \
               + " - " + str(self.__code_erreur) + " - " \
               + self.__message_erreur + "\n"

try:
    a = 5 / 0
except Exception as exc:
    raise EpsiException(exc, 10, "mon erreur à moi")
