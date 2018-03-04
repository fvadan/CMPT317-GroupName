from board import *
from time import sleep

# Status Constants:
PLAYER_1_WIN = 1
PLAYER_2_WIN = -1
DRAW = 0
NON_TERMINAL = 404
MAX_PLY = 50
MAX = "Player 1"
MIN = "Player 2"

def minimax(board, player, ply):
    """
    Minimax.
    """
    sleep(10)
    util = board.utility(ply)
    print("\n\n############ Playing ply:", ply, "############\n")
    print(board)
    print("\n############ Done ############\n\n")
    if util == PLAYER_1_WIN or util == PLAYER_2_WIN or util == DRAW:
        return util
    else:
        nextP = MIN if player == MAX else MAX
        succ = board.successors(nextP)
        [print(x) for x in succ]
        val = [minimax(s, nextP, ply + 1) for s in board.successors(player)]
        if val == []: # No successors/no moves left
            return DRAW
        else:
            return max(val) if player == MAX else min(val)
