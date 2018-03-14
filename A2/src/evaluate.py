from board import Board, Piece, BoardAdapter
from constants import Constants

def manhattan_dist(p1,p2):
    """
    Return Manhattan distnace between two points.
    :return: distance
    """
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

class Evaluate():
    """
    Evaluation class used to obtain evaluation values and utility for
    given boards.
    """
    board = None
    def __init__(self, board):
        self.board = BoardAdapter(board)

    def numWights(self):
        """
        Return number of wights.
        :return: number of wights
        """
        if len(self.board.wights) == 0:
            return Constants.INF
        return len(self.board.wights)

    def numDragons(self):
        """
        Return number of dragons left.
        :return: number of dragons left
        """
        return len(self.board.dragons)

    def queenPresent(self):
        """
        Tell whether queen is still on the board
        :return: True if on board, False otherwise
        """
        return -1 if self.board.queen == None else 1

    def queenPosition(self):
        """
        Tell the queen position if on board.
        :return: position of the queen
        """
        return self.board.queen[0] if self.board.queen != None else 0

    def wightPositions(self):
        """
        Return a list of wight positions left on the board
        :return: list of wight positions
        """
        return sum([1/w[0] if w[0] != 0 else 9999 for w in self.board.wights])

    def dragonPositions(self):
        """
        Return a list of dragon positions left on the board
        :return: list of dragon positions
        """
        return sum([d[0] for d in self.board.dragons])

    def wightDistsToQueen(self):
        """
        Return a value representing the distance of wights to the queen.
        :return: sum of wights distances to the queen
        """
        if self.queenPresent() == 1:
            return sum([manhattan_dist(w, self.board.queen) for w in\
                self.board.wights])
        return 9999

    def evaluation(self):
        """
        Return the evaluation of the current state/board.
        Evaluation is determined by following factors:
            1. Displacement of queen * (W1 = 10)
            2. Dislacement of wights * (W2 = -5)
            3. Displacement of dragon * (W3 = 5)
            4. Number of wights * (W4 = -2)
            5. Number of dragons * (W5 = 3)
            6. Queen under attack * (W6 = -50)  <-- (0 or 1) * wights
        :return: evaluation value.
        """
        # Weights for different evalution features.

        all_functions = [
                            (10, self.numDragons()), \
                            (-5, self.numWights()), \
                            (20, self.queenPresent()), \
                            (2, self.dragonPositions()), \
                            (5, self.queenPosition()), \
                            (-2, self.wightDistsToQueen())
                        ]

        return int(sum([x[0] * x[1] for x in all_functions]) * 10)

    def utility(self, ply):
        """
        Return the utility of a board.
        :param ply: current ply (turn)
        :return: utility of the board (NEGINF = Player 2 win
                                          INF = Player 1 win
                                          0   = Draw)
        """

        # Queen is captured
        if self.board.queen == None:
            return Constants.PLAYER_2_WIN

        # Queen reaches the Wight's home row
        if self.board.queen[0] == Constants.QUEEN_DESTINATION:
            return Constants.PLAYER_1_WIN

        # Reached max ply
        if ply == Constants.MAX_PLY:
            return Constants.DRAW

        return Constants.NON_TERMINAL

    def queenUnderAttack(self):
        """
        Determine whether queen is under attack.
        :return: 1 if under attack, 0 otherwise.
        """
        if self.board.queen == None:
            return 0
        x, y = self.board.queen[0], self.board.queen[1]
        I, J = x - 1, y - 1

        for i in range(I, I+3):
            for j in range(J, J+3):
                if i < 0 or j < 0 or i > 4 or j > 4 or (i,j) == self.board.queen:
                    continue
                elif self.board.board[i][j] == Piece.W:
                    return 1
        return 0
