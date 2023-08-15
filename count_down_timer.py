import time

class CountdownTimer:
    def __init__(self, duration):
        """
        Creates a countdown timer with the specified duration.

        Parameters:
            duration (int): The duration of the countdown timer in seconds.
        """
        self.__duration = duration
        self.__start_time = None

    def start(self):
        """
        Starts the countdown timer.
        """
        # if self.__start_time is not None:
        #     raise ValueError("Timer is already running.")
        self.__start_time = time.time()

    def stop(self):
        """
        Stops the countdown timer and returns the remaining time.

        Returns:
            str: The remaining time in the format 'mm:ss'.
        """
        if self.__start_time is None:
            raise ValueError("Timer is not running.")
        elapsed_time = time.time() - self.__start_time
        self.__start_time = None
        remaining_time = max(self.__duration - elapsed_time, 0)
        return remaining_time

    def is_running(self):
        """
        Returns True if the timer is currently running, False otherwise.

        Returns:
            bool: True if the timer is running, False otherwise.
        """
        return self.__start_time is not None

    def reset(self):
        """
        Resets the countdown timer.
        """
        self.__start_time = None

    def get_remaining_time(self):
        """
        Returns the remaining time in the format 'mm:ss'.

        Returns:
            str: The remaining time in the format 'mm:ss'.
        """
        if self.__start_time is None:
            return self.__duration
        elapsed_time = time.time() - self.__start_time
        remaining_time = max(self.__duration - elapsed_time, 0)
        return remaining_time
    

