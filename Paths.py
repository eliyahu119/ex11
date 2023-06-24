class Paths:

    def __init__(self):
        self.__paths = []
        self.__used_words = []
    def add_path(self,path):
        if not path.get_path_word() in self.__used_words:
            self.__paths.append(path)
            self.__used_words.append(path.get_path_word())

    def remove_last_path(self):
        self.__paths.pop()

    def clear_paths(self):
        self.__paths = []
        self.__used_words = []



