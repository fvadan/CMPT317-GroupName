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

    ### Internal function begins
    def do_minimax(board, player, ply, depth):

        if board.encode() in rec_table:
            return rec_table[board.encode()]

        old_board = BoardAdapter(board)

        b_eval = Evaluate(board)
        if b_eval.utility(ply) != Constants.NON_TERMINAL: # base case 1
            ret = b_eval.utility(ply)
        elif depth <= 0: # base case 2
            ret = b_eval.evaluation()[0]
        else: # recursive case
            successors = board.successors(player)

            # No successors is a draw
            if len(successors) <= 0:
                ret = Constants.DRAW
            elif player == Constants.MAX:
                b_eval_succ = [\
                    do_minimax(succ, Constants.MIN, ply+1, depth-1)\
                          for succ in successors]
                best_value = max(b_eval_succ)
                ret = best_value
            else: # if player is minimizer
                b_eval_succ = [\
                    do_minimax(succ, Constants.MAX, ply+1, depth-1)\
                           for succ in successors]
                best_value = min(b_eval_succ)
                ret = best_value
        rec_table[board.encode()] = ret
        return ret
    ### Internal function ends

    result = do_minimax(board, player, ply, depth)
    return result

def alphaBeta(board, player, ply, depth):
    """
    Alpha-Beta pruning algorithm.
    :param board: the board that minimax is performed on;
    :param player: the player whose turn it is;
    :param ply: the turn number;
    :return value: value of the game.
    """

    rec_table = HashTable()

    def do_alphaBeta(board, player, ply, alpha, beta, depth):
        """
        :param - alpha: alpha value
        :param - beta: beta value
        """
        # check if board is already in the table
        if board.encode() in rec_table:
            return rec_table[board.encode()]

        old_board = BoardAdapter(board)

        b_eval = Evaluate(board)
        if b_eval.utility(ply) != Constants.NON_TERMINAL:
            ret = b_eval.utility(ply)
        elif depth <= 0:
            ret = b_eval.evaluation()[0]
        else:
            successors = board.successors(player)

            if len(successors) <= 0:
                ret = Constants.DRAW
            elif player == Constants.MAX:
                v = Constants.NEGINF
                for child in successors:
                    v = max(v, do_alphaBeta(child, Constants.MIN, ply+1, \
                                         alpha, beta, depth-1))
                    alpha = max(alpha, v)
                    if beta <= alpha:
                        break # beta cut-off
                ret = v
            else:
                v = Constants.INF
                for child in successors:
                    v = min(v, do_alphaBeta(child, Constants.MAX, ply+1, \
                                         alpha, beta, depth-1))
                    beta = min(beta, v)
                    if beta <= alpha:
                        break # alpha cut-off
                ret = v
        rec_table[board.encode()] = ret
        return ret

    result = do_alphaBeta(board, player, ply, Constants.NEGINF, \
                          Constants.INF, depth)
    return result
