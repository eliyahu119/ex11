from count_down_timer import CountdownTimer

GAME_DURATION=3*60


class Boggel:

    def __init__(self) -> None:
        self.__score=0
        self.__current_path=set()
        self.__timer=CountdownTimer(GAME_DURATION)
    
    @property 
    def score(self):
        return self.__score
    
    def __init_game_board():
        #create a matrix, for the game board
        pass

    def init_word_dict():
        #self.__words=None #create utils, that get the words safely.
        pass

    def get_value_by_location(self,x,y):
        #returns the location value base
        # return matrix[x][y]
        pass

    def add_to_current_path(self,x,y):
        #check if its alright,
        #add to path
        pass

    def is_location_disabled(self,x,y):
        #check if the button is disabled.
        return (x,y) in self.path

    def game_over(self):
        #check if all the conditions are met for the game to be over
        pass

    def get_current_time(self)->str:
        # return timer
        return self.__timer.get_remaining_time()
        
    def current_word(self)->str:
        pass
    
    def current_score(self)->str:
        pass

    def start_game(self)->None:
        #start the game
        #start timer
        #init_path
        #init score
        #init i
        pass
    