
from typing import List, Tuple, Iterable, Optional
from copy import copy,deepcopy

Board = List[List[str]]
Path = List[Tuple[int, int]]


def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    pass

def in_bound(coordinate,board):
    return 0 <= coordinate[0] < len(board) and 0 <= coordinate[1] < len(board[0])

def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
        results=[]
        memo={}
        hashed_words=set(words)
        
        def all_possible_words(coor,n,has_been:set=None)->List[Tuple[str,Path]]:
                if has_been == None:
                    has_been=set()

                nonlocal board
                if n <= 0:
                    return []
                if not in_bound(coor,board):
                    return [] 
                if coor in  has_been:
                    return []
                has_been.add(coor)

                if n == 1:
                    string=board[coor[0]][coor[1]]
                    result=[(string,[coor])]
                    return result
                
                if (coor,n) in memo:
                    return  deepcopy(memo[(coor,n)])
                
                results=[]
                for dir in get_possible_directions(coor):
                    n_1_results=deepcopy(all_possible_words(dir,n-1,has_been))
                    for result in n_1_results:
                        st,path=result
                        path=[coor,*path]
                        st=board[coor[0]][coor[1]]+st
                        results.append((st,path))
                memo[(coor,n)]=results
                return results
  


        possible_results=[]
        height = len(board)
        width = len(board[0]) if board[0] else 0
    
        for col in range(height):
            for row in range(width):
                result=all_possible_words((col,row),n)
                possible_results.extend(result)
    
        results = []
        for (word,path) in possible_results:
            if word in hashed_words:
                results.append(path)

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




# def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
#     pass
