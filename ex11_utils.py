
from typing import List, Tuple, Iterable, Optional
from copy import copy,deepcopy
import math

Board = List[List[str]]
Path = List[Tuple[int, int]]

def distance(coor1,coor2):
    return math.sqrt((coor1[0]-coor2[0])**2 + (coor1[1]-coor2[1])**2)

def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    if not len(set(path)) == len(path): return None
    str = ""
    if not in_bound(path[0],board): return None
    before = path[0]
    str += board[before[0]][before[1]]
    for i in range(1,len(path)):
        coor = path[i]
            #check if the coor is in bound
        if not in_bound(coor,board): return None
            #checking if the distance is bigger then 1
        if not distance(before,coor) == 1: return None
        str += board[coor[0]][coor[1]]
        before = coor
    if not str in words: return None
    return str

def in_bound(coordinate,board):
    if not  0 <= coordinate[0] < len(board):
        return False
    if not 0 <= coordinate[1] < len(board[0]):
        return False
    return True


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    valid_paths = []
    def check_words(row: int, col: int, word: str, current_path: Path,visited:set):
        # Base case: If the current path length exceeds n or the word does not match, stop the search
        if len(current_path) > n or not word.startswith(board[row][col]):
            return

        # Update the word and current path
        word = word[len(board[row][col]):]
        current_path.append((row, col))

        # Base case: If the current path length is n and the word is empty, add the current path to valid_paths
        if len(current_path) == n and len(word) == 0:
            valid_paths.append(list(current_path))

        # Explore all possible neighbors
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
        
                new_row, new_col = row + i, col + j

                # Make sure the neighbor is within the board bounds
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
                    if  (new_row, new_col) not in visited:
                        
                        # Add the neighbor to the visited set
                        visited.add((new_row, new_col))

                        # Recursive call to explore the neighbor
                        check_words(new_row, new_col, word, current_path, visited)

                        # Remove the neighbor from the visited set after the recursive call
                        visited.remove((new_row, new_col))


        # Remove the last cell from the current path to backtrack
        current_path.pop()

    # Iterate over each word and each cell on the board
    for word in words:
        for row in range(len(board)):
            for col in range(len(board[0])):
                # Perform check words starting from each cell
                check_words(row, col, word, [],set())

    return valid_paths

      
def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    result=[]
    cleaned_words=filter(lambda x:len(x)==n,words)
    for word in cleaned_words:
       result.extend(find_length_n_word(n,board,word))
    return result


def find_length_n_word(n:int,board:Board,word:str)->List[Path]:
    
    def dfs(coor,word:str,path:set=set()): 
        nonlocal board        
        if not in_bound(coor,board):
            return []
        
        if coor in path:
            return []
        
        inner=board[coor[0]][coor[1]]

        if not word.startswith(inner):
            return []
        
        updated_word=word[len(inner):]
        #base case
        if updated_word == "":
            return [list(path)]
        
    
        #dfs algorithim
        path.add(coor)
        result=[]
        #will return [] in coor
        for i in range(-1,2):
             for j in range(-1,2):
                new_coor = coor[0] + i, coor[1] + j
                result_from=dfs(new_coor,path)
                result.extend(result_from)          
        path.remove(coor)
        return result_from

         
    
    
    result=[]
    cols = len(board)
    rows = len(board[0])
    for col in range(cols):
        for row in range(rows):
            # current=board[col][row]
           result.extend(dfs((col,row),word))
    return result 


    
        


        


# # def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
# #     pass

