import math

class Constants():
    """
        Class that keeps track of all the constants used throughout the program.
    """

    PLAYER_1_WIN = 9999999 # Player 1 is maximizer
    PLAYER_2_WIN =  -1 * 9999999 # Player 2 is minimizer
    DRAW = 0
    NON_TERMINAL = 404
    MAX_PLY = 50
    MAX = "Player 1"
    MIN = "Player 2"
    QUEEN_DESTINATION = 4
    INF = 9999999
    NEGINF = (-1) * 9999999
