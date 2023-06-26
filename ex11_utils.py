
from typing import List, Tuple, Iterable, Optional
from copy import copy, deepcopy
import math

Board = List[List[str]]
Path = List[Tuple[int, int]]


def distance(coor1, coor2):
    """
    Calculates the Euclidean distance between two points in a two-dimensional space.

    Args:
        coor1 (tuple): A tuple representing the coordinates of the first point (x1, y1).
        coor2 (tuple): A tuple representing the coordinates of the second point (x2, y2).

    Returns:
        float: The Euclidean distance between the two points.

    """
    return math.sqrt((coor1[0]-coor2[0])**2 + (coor1[1]-coor2[1])**2)


def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    """
    Checks if a given path is valid on the board and matches a word from the provided iterable of words.

    Args:
        board (Board): The board represented as a two-dimensional structure.
        path (Path): The path to be checked, represented as a sequence of coordinates.
        words (Iterable[str]): An iterable of words to check against.

    Returns:
        Optional[str]: The word formed by the path if it is valid and matches a word from the iterable.
                       Returns None if the path is invalid or doesn't match any word.

    """
    
    if not path:
        return None
    
    if len(path) == 0:
        return None
    
    if not len(set(path)) == len(path):
        return None
    
    st=""
    
    
    for i,coor in  enumerate(path):
        # check if the coor is in bound
        if not in_bound(coor, board):
            return None
        
        if i != 0:
            before=path[i-1]            
            ds=math.floor(distance(coor,before)) 
            if ds != 1:
                return None
            
        st += board[coor[0]][coor[1]]
        
    if not st in words:
        return None
    return st


def in_bound(coordinate, board):
    """
    Checks if a given coordinate is within the boundaries of the board.

    Args:
        coordinate (tuple): A tuple representing the coordinate to be checked (x, y).
        board (list): A two-dimensional list representing the board.

    Returns:
        bool: True if the coordinate is within the board boundaries, False otherwise.

    """
    if not 0 <= coordinate[0] < len(board):
        return False
    if not 0 <= coordinate[1] < len(board[0]):
        return False
    return True


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    Finds all paths of length n on the board that match words from the provided iterable.

    Args:
        n (int): The length of paths to search for.
        board (Board): The board represented as a two-dimensional structure.
        words (Iterable[str]): An iterable of words to search for.

    Returns:
        List[Path]: A list of paths of length n that match words from the iterable.

    """
    results = []
    words = list(sorted(words))
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            results.extend(find_length_n_paths_helper(
                n, board, words, [(i, j)]))
    return results


def find_length_n_paths_helper(n: int, board: Board, words: list[str], path: list = []):
    """
    Helper function for finding paths of length n on the board that match words from the provided iterable.

    Args:
        n (int): The length of paths to search for.
        board (Board): The board represented as a two-dimensional structure.
        words (list[str]): A list of words to search for.
        path (list): Optional. The current path being explored.

    Yields:
        list: A valid path of length n that matches a word from the iterable.

    """
    if not in_bound(path[-1], board):
        return

    if path[-1] in path[0:-2]:
        return

    word = path_to_word(board, path)
    words = list(filter(lambda x: x.startswith(word), words))

    if len(words) == 0:
        return

    if n == len(path):
        if words[0] == word:
            yield list(path)
        return

    row, col = path[-1]
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            coordinate = (row+i, col+j)
            path.append(coordinate)
            yield from find_length_n_paths_helper(n, board, words, path)
            path.pop()

def path_to_word(board, path):
    """
    Converts a given path on the board to a word.

    Args:
        board (Board): The board represented as a two-dimensional structure.
        path (list): The path represented as a list of coordinate tuples.

    Returns:
        str: The word formed by traversing the path on the board.

    """
    return "".join([board[i][j] for i, j in path])


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    Finds all words of length n on the board that exist in the provided iterable.

    Args:
        n (int): The length of words to search for.
        board (Board): The board represented as a two-dimensional structure.
        words (Iterable[str]): An iterable of words to search for.

    Returns:
        List[Path]: A list of paths representing the locations of the found words.

    """
    results = []
    words = filter(lambda x: len(x) == n, words)
    words = sorted(words)
    words = list(words)
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            results.extend(find_length_n_words_helper(
                n, board, words, [(i, j)]))
    return results


def find_length_n_words_helper(n: int, board: Board, words: list[str], path: list = []):
    """
    Helper function for finding words of length n on the board that exist in the provided iterable.

    Args:
        n (int): The length of words to search for.
        board (Board): The board represented as a two-dimensional structure.
        words (list[str]): A list of words to search for.
        path (list): Optional. The current path being explored.

    Yields:
        list: A valid path representing the location of a found word.

    """
    
    if not in_bound(path[-1], board):
        return

    if path[-1] in path[0:-2]:
        return

    word = "".join([board[i][j] for i, j in path])
    words = list(filter(lambda x: x.startswith(word), words))

    if len(words) == 0:
        return

    if n == len(word):
        if words[0] == word:
            yield list(path)
        return

    row, col = path[-1]
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            coordinate = (row+i, col+j)
            path.append(coordinate)
            yield from find_length_n_words_helper(n, board, words, path)
            path.pop()


def max_score_paths(board,words):
    existed=set()
    
    def not_used_words(paths,board):
        filtered=[]
        for path in paths:
            word = path_to_word(board,path)
            if word in existed:
                continue
            existed.add(word)
            filtered.append(path)
        return filtered    
    
    def filter_words(words,used_words):
        set_used_words = set(used_words)
        new_words=list(filter(lambda x: x in set_used_words,words))
        return new_words

    max_n = max(map(lambda x:len(x),words))
    list_max_paths = []
    for n in range(max_n,0,-1):
        all_paths_len_n = find_length_n_paths(n,board,words)
        filtered_words=not_used_words(all_paths_len_n,board)
        list_max_paths.extend(filtered_words)
        words = filter_words(words,filtered_words)
    
    return list_max_paths

   
    
def load_words(file_location):
    try:
        with open(file_location, "r") as file:
            lines = file.readlines()
            stripped_lines=map(lambda x: x.strip(),lines)
            return set(stripped_lines)
        pass
    except Exception:
        #return default
        return set()

def format_time(time_in_seconds):
        """
        Formats the time in seconds as 'mm:ss'.

        Parameters:
            time_in_seconds (float): The time in seconds.

        Returns:
            str: The formatted time in the format 'mm:ss'.
        """
        minutes = int(time_in_seconds // 60)
        seconds = int(time_in_seconds % 60)
        return f"{minutes:02d}:{seconds:02d}"