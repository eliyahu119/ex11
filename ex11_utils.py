
from typing import List, Tuple, Iterable, Optional
from copy import copy

Board = List[List[str]]
Path = List[Tuple[int, int]]


def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    pass

def if_bound(coordinate,board):
    return 0 <= coordinate[0] < len(board) and 0 <= coordinate[1] < len(board[0])

def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    results=[]
    memo={}

    
    def find_words(coor,n,path:list=[],word="",has_been:set=set())->List[Path]:
        nonlocal words
        nonlocal board
        nonlocal results

        if n <= 0:
            if word in words:
                results.append(copy(path))
            return 
        
        if not if_bound(coor,board):
            return 
        
        if coor  in has_been:
            return 
        
        has_been.add(coor)
        path.append(coor)
        word+=board[coor[0]][coor[1]]
        all_possible_dirs=get_possible_directions(coor)
        for dir in all_possible_dirs:
             find_words(dir,n-1,path,word,has_been)


    height = len(board)
    width = len(board[0]) if board[0] else 0
    for col in range(height):
        for row in range(width):
            find_words((col,row),n-1)

    return results


    
        

      
def get_possible_directions(coor):
    x, y= coor
    directions = []
    directions.append((x + 1, y))      # Right
    directions.append((x - 1, y))      # Left
    directions.append((x, y + 1))      # Up
    directions.append((x, y - 1))      # Down
    directions.append((x + 1, y + 1))  # Top right
    directions.append((x - 1, y + 1))  # Top left
    directions.append((x + 1, y - 1))  # Bottom right
    directions.append((x - 1, y - 1))  # Bottom left
    return directions

    
      









# def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
#     result=[]
#     for word in words:
#        result.extend(find_length_n_word(n,board,word,i=0,x=0))



#  def find_length_n_word(n:int,board:Board,word:str)->List[Path]:




def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    pass
