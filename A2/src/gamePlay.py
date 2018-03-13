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
    node_count = [0]

    ### Internal function begins
    def do_minimax(board, player, ply, depth):
        """
        For memoization.
        """
        # Stats:
        node_count[0] += 1

        # Transposition:
        board_hash = board.encode()
        if board_hash in rec_table and depth < rec_table[board_hash][1]:
            return rec_table[board_hash][0]

        # evaluate board
        b_eval = Evaluate(board)

        if b_eval.utility(ply) != Constants.NON_TERMINAL: # End game
            ret = b_eval.utility(ply)
        elif depth <= 0: # max search depth hit
            ret = b_eval.evaluation()
        else: # recursive case
            successors = board.successors(player)

            # No successors is a draw
            if len(successors) <= 0:
                ret = Constants.DRAW
            elif player == Constants.MAX:
                best_value = Constants.NEGINF
                for succ in successors:
                    v = do_minimax(succ, Constants.MIN, ply+1, depth-1)
                    best_value = max(best_value, v)
                ret = best_value
            else: # if player is minimizer
                best_value = Constants.INF
                for succ in successors:
                    v = do_minimax(succ, Constants.MAX, ply+1, depth-1)
                    best_value = min(best_value, v)
                ret = best_value

        # Transposition:
        rec_table[board_hash] = (ret, depth)
        return ret
    ### Internal function ends

    return do_minimax(board, player, ply, depth), \
           len(rec_table), \
           node_count[0]

def alphaBeta(board, player, ply, depth):
    """
    Alpha-Beta pruning algorithm.
    :param board: the board that minimax is performed on;
    :param player: the player whose turn it is;
    :param ply: the turn number
    :param - alpha: alpha value
    :param - beta: beta value
    :return value: value of the game.
    """

    rec_table = HashTable()
    node_count = [0]

    def do_alphaBeta(board, player, ply, alpha, beta, depth):
        """
        For memoization.
        """

        # update stats
        node_count[0] += 1

        # Transposition:
        board_hash = board.encode()
        if board_hash in rec_table and depth < rec_table[board_hash][1]:
            return rec_table[board_hash][0]

        # evaluate board
        b_eval = Evaluate(board)

        if b_eval.utility(ply) != Constants.NON_TERMINAL: # terminal node
            ret = b_eval.utility(ply)
        elif depth <= 0:
            ret = b_eval.evaluation()
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

        # Transposition:
        rec_table[board_hash] = (ret, depth)

        return ret

    return do_alphaBeta(board, player, ply, \
                        Constants.NEGINF, \
                        Constants.INF, depth), \
           len(rec_table), \
           node_count[0]
