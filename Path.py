import ex11_utils

class Path:
    def __init__(self):
        self.__path = []

    def add_to_path(self,coor):
        self.__path.append(coor)

    def valid_path(self,board,words):
        ex11_utils.is_valid_path(board,self.__path,words)

    def get_path(self):
        return list(self.__path)
    
    def clear(self):
        self.__path = []




