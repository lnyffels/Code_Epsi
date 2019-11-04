class ToDoSaveRequestObject:
    def __init__(self, description):
        if not description:
            self.__description = "pas de description"
        else:
            self.__description = description

    @property
    def description(self):
        return self.__description

