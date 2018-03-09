from board import *
from time import sleep
import math
from evaluate import Evaluate
from hashTable import HashTable
from constants import Constants

def minimax(board, player, ply, depth):
    """
    Minimax algorithm.
    :param board: the board that minimax is performed on;
    :param player: the player whose turn it is;
    :param ply: the turn number;
    :return value: value of the game.
    """

    rec_table = HashTable()
    depth_limit = 10

    ### Internal function begins
    def do_minimax(board, player, ply, depth):


        #sleep(1)
        print("\n##### START PLY: ", ply, " #####")
        print("\nSTATUS:\n--> WIGHTS: ", board.wights, \
                       "\n--> DRAGONS:", board.dragons, \
                       "\n--> QUEEN:", board.queen)

        print("\nSTATUS:\n", len(board.wights), " wights\n", \
                len(board.queen)-1, " queen\n", len(board.dragons), " dragons\n")

        print(board)


        print("Evaluation:")
        print(Evaluate(board).evaluation(), "\n")
        print("##### END PLY: ", ply, " #####\n")


        # if_you_are_at_a_terminal_node/reached ply
            # return utility
        # if depth limit is reached:
            # return evaluation of current node
        # else if you are max player
            # evaluation_val = run minimax on max player successors until
            # depth limit is reached
        # if you are a min PLAYer
            # evaluation_val = run minimax on min player successors until
            # depth limit is reached
        b_eval = Evaluate(board)
        if b_eval.utility(ply) != Constants.NON_TERMINAL: # base case 1
            return b_eval.utility(ply)
        elif depth >= depth_limit: # base case 2
            return b_eval.evaluation()[0]
        else: # recursive case
            successors = board.successors(player)

            # No successors is a draw
            if len(successors) <= 0:
                return Constants.DRAW

            if player == Constants.MAX:
                b_eval_succ = [\
                    do_minimax(succ, Constants.MIN, ply+1, depth+1)\
                          for succ in successors]
                best_value = max(b_eval_succ)
                return best_value
            else: # if player is minimizer
                b_eval_succ = [\
                    do_minimax(succ, Constants.MAX, ply+1, depth+1)\
                           for succ in successors]
                best_value = min(b_eval_succ)
                return best_value
    ### Internal function ends

    return do_minimax(board, player, ply, depth)
