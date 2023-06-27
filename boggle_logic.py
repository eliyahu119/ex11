from count_down_timer import CountdownTimer
from boggle_board_randomizer import randomize_board
import ex11_utils
from path import Path
FILE_LOCATION=r"boggle_dict.txt"
GAME_DURATION=180



class Boggle:
    """
    The Boggle class represents a game of Boggle.
    Properties:
        used_words (list): Returns a list of used words in the game.
        score (int): Returns the current score of the game.

    Methods:
        start_game(): Starts the game by initializing the board, score, and timer.
        end_game(): Ends the game.
        get_value_by_location(x, y): Retrieves the value (word) at the specified location on the board.
        add_to_current_path(x, y): Adds a given location to the current path being formed.
        is_game_over(): Checks if the game is over based on certain conditions.
        get_current_time(): Returns the remaining time on the countdown timer.
        submit_word(): Submits the current path as a word, calculates score, and updates used words.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the Boggle class.
        """
        self.__score=0
        self.__init_word_dict()
        self.__timer=CountdownTimer(GAME_DURATION)
        self.__end_game=False
        self.__path:Path=Path()
        self.__used_words=set()
        self.__max_score = float("inf")
    @property 
    def used_words(self):
        """
        Returns a list of used words in the game.

        Returns:
            list: A list of used words.

        """
        return list(self.__used_words)
    
    @property 
    def score(self):
        """
        Returns the current score of the game.

        Returns:
            int: The current score.

        """
        return self.__score
    
    def __add_to_score(self,n):
        """
        Adds a given value to the current score.

        Args:
            n (int): The value to be added to the score.

        """
        if not self.__score :
            self.__score = 0
        self.__score+=n
        
    def end_game(self):
        """
        Ends the game.

        """
        self.__end_game = True
    
    def __init_game_board(self):
        """
        Initializes the game board by randomizing letters.

        """
        self.__board=randomize_board()
        
    def __init_word_dict(self):
        """
        Initializes the set of valid words from a dictionary file.

        """ 
        self.__ini_words=ex11_utils.load_words(FILE_LOCATION)

        
    def get_value_by_location(self,x,y):
        """
        Retrieves the value (letter) at the specified location on the board.

        Args:
            x (int): The row index.
            y (int): The column index.

        Returns:
            str: The letter at the specified location.

        """
        return self.__board[x][y]
      
    def add_to_current_path(self,x,y):
        """
        Adds a given location to the current path being formed.

        Args:
            x (int): The row index.
            y (int): The column index.

        """
        #add to path
        self.__path.add_to_path((x,y))


    def is_game_over(self)->bool:
        """
        Checks if the game is over based on certain conditions.

        Returns:
            bool: True if the game is over, False otherwise.

        """
        
        #check if all the conditions are met for the game to be over
        if self.__timer == 0:
            return True
        if self.score == self.__max_score:
            return True
        if self.__end_game:
            return True
        return False

    def get_current_time(self)->int:
        """
        Returns the remaining time on the countdown timer.

        Returns:
            int: The remaining time in seconds.

        """
        # return timer
        return self.__timer.get_remaining_time()
            
    def start_game(self)->None:
        """
        Starts the game by initializing the board, score, and timer.

        """
        self.__init_game_board()
        self.__score=0 
        # self.__max_score=len(ex11_utils.max_score_paths(self.__board,self.__ini_words))
        self.__used_words=set()
        self.__timer.start()

    def submit_word(self):
        """
        Submits the current path as a word, calculates the score, and updates used words.

        Returns:
            str or None: The submitted word if valid and not already used, None otherwise.

        """
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

    def used_words_to_string(self,i):
        """Returns the string of used words,i words in line"""
        string, counter = "", 0
        lst = list(self.__used_words)
        for word in lst:
            if counter % i == 0:  # more than 5 words in line
                string += "\n"
            string += (word + " ")
            counter += 1
        return string
        

if __name__ == "__main__":
    b=Boggle()
    
