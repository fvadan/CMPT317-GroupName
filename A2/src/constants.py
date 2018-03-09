import math

class Constants():
    """
        Class that keeps track of all the constants used throughout the program.
    """

    MAX_SCORE = 200
    MIN_SCORE = -200
    PLAYER_1_WIN = math.inf # Player 1 is maximizer
    PLAYER_2_WIN =  -1 * math.inf # Player 2 is minimizer
    DRAW = 0
    NON_TERMINAL = 404
    MAX_PLY = 50
    MAX = "Player 1"
    MIN = "Player 2"
    QUEEN_DESTINATION = 4
