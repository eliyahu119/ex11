import copy
class Path:
    def __init__(self):
        self.__path = []
        self.__path_word = ""

    def add_char(self, coordinate, board):
        if not self.is_location_disabled(coordinate):
            self.__path.append(coordinate)
            self.__path_word += board[coordinate[0]][coordinate[1]]

    def is_location_disabled(self, coordinate):
        # check if the button is disabled.
        return coordinate in self.__path

    def get_path(self):
        return copy.deepcopy(self.__path)

    def get_path_word(self):
        return copy.deepcopy(self.__path_word)

    def clear_word(self):
        self.__path = []
        self.__path_word= ""


