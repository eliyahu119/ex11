from count_down_timer import CountdownTimer
from boggle_board_randomizer import randomize_board
import ex11_utils

FILE_LOCATION=r"boggle_dict.txt"
GAME_DURATION=3*60

class Boggle:

    def __init__(self) -> None:
        self.__score=0
        self.__init_word_dict()
        self.__timer=CountdownTimer(GAME_DURATION)
        self.__end_game=False
         
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
        value=self.__board[x][y]
        # #check if its alright,
        # #add to path
        pass

    def is_location_disabled(self,x,y):
        pass
        #check if the button is disabled.
        # return (x,y) in self.path

    def is_game_over(self):
        #check if all the conditions are met for the game to be over
        if self.__timer == 0:
            return True
        if self.score == self.__max_score:
            return True

        # pass

    def get_current_formmated_time(self)->str:
        # return timer
        return CountdownTimer.format_time(self.__timer.get_remaining_time())
        
    def current_word_pogress(self)->str:
        pass
    
    def start_game(self)->None:
        self.__timer.start()
        self.__init_game_board()
        self.__score=0
        # self.__path.clear()
        
        #start the game
        #start timer
        #init_path
        #init score
        #init i
   
    def check_word():
        pass
        #checks if the word is ok
        # and if it is add it to score
        
    