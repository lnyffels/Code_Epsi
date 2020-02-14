import os
import datetime

TXT = "epsi_error.txt"
PATH = "c:\\temp"


class EpsiException(Exception):
    def __init__(self, exc, code_erreur, message_erreur):
        super().__init__(exc)
        self.__inner_exception = exc
        self.__code_erreur = code_erreur
        self.__message_erreur = message_erreur
        os.chdir(PATH)
        self.__log_in_file()

    def __log_in_file(self):
        error_file = open(TXT, "a")
        error_file.write(self.__format_error())
        error_file.close()


    def __format_error(self):
        return f"{datetime.datetime.now()};{self.__inner_exception};{self.__code_erreur};{self.__message_erreur}"





try:
    print("hello")
    a = 5 / 0
except Exception as exc:
    raise EpsiException(exc, 10, "attention à la division par zéro")
