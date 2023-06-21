
from typing import List, Tuple, Iterable, Optional
from copy import copy, deepcopy
import math

Board = List[List[str]]
Path = List[Tuple[int, int]]


def distance(coor1, coor2):
    return math.sqrt((coor1[0]-coor2[0])**2 + (coor1[1]-coor2[1])**2)


def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
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
    if not 0 <= coordinate[0] < len(board):
        return False
    if not 0 <= coordinate[1] < len(board[0]):
        return False
    return True


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    results = []
    words = list(sorted(words))
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            results.extend(find_length_n_paths_helper(
                n, board, words, [(i, j)]))
    return results


def find_length_n_paths_helper(n: int, board: Board, words: list[str], path: list = []):
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
    return "".join([board[i][j] for i, j in path])


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
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
        unique=[]
        for path in paths:
            word = path_to_word(board,path)
            if word in existed:
                continue
            unique.append(path)
        return unique    
    
    def add_to_memo(paths):
        for path in paths:
            word = path_to_word(board,path)
            existed.add(word)
          
    list_max_paths = []
    n=math.inf
    while True:
        max_n = max(map(lambda x:len(x),words)) if words else 0
        n = min(max_n,n-1) 
        if n <= 0 :
            break
        all_paths_len_n = find_length_n_paths(n,board,words)
        add_to_memo(all_paths_len_n)
        filtered_words=not_used_words(all_paths_len_n,board)
        list_max_paths.extend(all_paths_len_n)
        words = filtered_words
    return list_max_paths

   
    

    