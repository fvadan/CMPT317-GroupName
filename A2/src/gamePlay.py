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
"""
def minimax(board, player, ply):

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
"""
def minimax(board, player, ply):
    """
    Minimax algorithm.
    :param board: the board that minimax is performed on;
    :param player: the player whose turn it is;
    :param ply: the turn number;
    :return value: value of the game.
    """

    rec_table = dict()

    def do_minimax(board, player, ply):
        sleep(1)
        print("\n##### START PLY: ", ply, " #####")
        print("\nSTATUS:\n", len(board.wights), " wights\n", \
                len(board.queen)-1, " queen\n", len(board.dragons), " dragons\n")
        print(board)
        print("##### END PLY: ", ply, " #####\n")
        s = board.__str__()
        u = board.utility(ply)
        if s in rec_table:
            print("\n\nRETURNED FROM TRANSPOSITION TABLE!\n\n")
            return rec_table[s]
        if u == PLAYER_1_WIN or u == PLAYER_2_WIN or u == DRAW:
            return u
        else:
            nextP = MIN if player == MAX else MAX
            val = [do_minimax(x, nextP, ply+1) for x in board.successors(player)]
            if not val:
                return DRAW
            else:
                return max(val) if player == MAX else min(val)

    return do_minimax(board, player, ply)
