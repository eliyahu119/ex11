from count_down_timer import CountdownTimer
import sys,boggle_board_randomizer
import ex11_utils
GAME_DURATION=3*60

class Boggle:

    def __init__(self) -> None:
        self.__score=0
        self.__current_path=[]
        self.__current_word = ""
        self.__timer=CountdownTimer(GAME_DURATION)
        self.__board = self.__init_game_board()
        self.__words_set = self.init_words_set()
        self.__max_score = self.get_max_possible_score()
    @property 
    def score(self):
        return self.__score
    
    def init_game_board(self):
        return boggle_board_randomizer.randomize_board()

    def init_words_set(self): #load words set
        try:
            words_set = {}
            file = open(sys.argv[1], "r")
            index_list = file.read().split('\n')
            file.close()
            for word in index_list:
                words_set.add(word)
            return words_set
        except:
            return {}

    def get_value_by_location(self,x,y):
        #returns the location value base
        # return matrix[x][y]
        return self.__board[x][y]


    def add_to_current_path(self,x,y):
        #check if its alright,
        #add to path
        if not self.is_location_disabled(x,y):
            self.__current_path.append((x,y))
            self.__current_word += self.__board[x][y]

    def is_location_disabled(self,x,y):
        #check if the button is disabled.
        return (x,y) in self.__current_path

    def is_game_over(self):
        #check if all the conditions are met for the game to be over
        return self.__timer.get_remaining_time() == 0 or self.__score == self.__max_score

    def get_current_time(self)->str:
        # return timer
        return self.__timer.get_remaining_time()
        
    def current_word(self)->str:
        return self.__current_word

    def current_score(self)->str:
        return self.__score


    def start_game(self)->None:
        #start the game
        #start timer
        #init_path
        #init score
        #init i
        pass

    def get_max_possible_score(self):
        paths_list = ex11_utils.max_score_paths(self.__board,self.__words_set)
        max_score = 0
        for path in paths_list:
            max_score += len(path)**2
        return max_score


    