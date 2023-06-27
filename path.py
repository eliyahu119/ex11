
class Path:
    """The class describe path as list of coordinates"""
    def __init__(self):
        """Create new path"""
        self.__path = []

    def add_to_path(self,coor):
        """Add new coordinate to path"""
        self.__path.append(coor)


    def get_path(self):
        """Get the path as list"""
        return list(self.__path)
    
    def clear(self):
        """Remove all coordinates of path"""
        self.__path = []




