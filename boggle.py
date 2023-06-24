from count_down_timer import CountdownTimer
from boggle_board_randomizer import randomize_board
import ex11_utils
from path import Path
FILE_LOCATION=r"boggle_dict.txt"
GAME_DURATION=3*60

class Boggle:

    def __init__(self) -> None:
        self.__score=0
        self.__init_word_dict()
        self.__timer=CountdownTimer(GAME_DURATION)
        self.__end_game=False
        self.__path:Path=Path()
        self.__used_words=set()

    @property 
    def used_words(self):
        return list(self.__used_words)
    
    @property 
    def score(self):
        return self.__score
    
    def __add_to_score(self,n):
        self.__score+=n
        
    def end_game(self):
        self.__end_game = True
    
    def __init_game_board(self):
        #create a matrix, for the game board
        self.__board=randomize_board()
        
    def __init_word_dict(self):
       self.__ini_words=ex11_utils.load_words(FILE_LOCATION)

        
    def get_value_by_location(self,x,y):
        return self.__board[x][y]
      
    def add_to_current_path(self,x,y):
         #add to path
        self.__path.add_to_path((x,y))


    def is_game_over(self):
        #check if all the conditions are met for the game to be over
        if self.__timer == 0:
            return True
        if self.score == self.__max_score:
            return True
        if self.__end_game:
            return True
        return False

    def get_current_time(self)->str:
        # return timer
        return self.__timer.get_remaining_time()
        
    def current_word_pogress(self)->str:
        pass
    
    def start_game(self)->None:
        self.__timer.start()
        self.__init_game_board()
        self.__score=0 
        self.__max_score=len(ex11_utils.max_score_paths(self.__board,self.__ini_words))
        self.__used_words=set()

    def submit_word(self):
        current=self.__path.get_path()
        self.__path.clear()
        word=ex11_utils.is_valid_path(self.__board,current,self.__ini_words)
        if not word:
            return None
        if word in self.__used_words:
            return None
        self.__used_words.add(word)
        self.__add_to_score(len(current)**2)
        return word
        # __used_words.set()
        # kpass
        

if __name__ == "__main__":
    b=Boggle()
    
