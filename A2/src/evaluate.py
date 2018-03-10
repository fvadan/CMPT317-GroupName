from board import Board, Piece, BoardAdapter
from constants import Constants

def manhattan_dist(p1,p2):
    """
    Return Manhattan distnace between two points.
    :return: distance
    """
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

class Evaluate():
    board = None
    def __init__(self, board):
        self.board = BoardAdapter(board)

    def numWights(self):
        if len(self.board.wights) == 0:
            return Constant.INF
        return 1/len(self.board.wights)

    def numDragons(self):
        return len(self.board.dragons)

    def queenPresent(self):
        return 0 if self.board.queen == None else 1

    def queenPosition(self):
        return self.board.queen[0] if self.board.queen != None else 0

    def wightPositions(self):
        return sum([1/w[0] if w[0] != 0 else 1/5 for w in self.board.wights])

    def dragonPositions(self):
        return sum([d[0] for d in self.board.dragons])

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

        all_functions = [(250, self.numDragons()), \
                         (200, self.numWights()), \
                         (250, self.queenPresent()), \
                         (50, self.dragonPositions()), \
                         (-30, self.wightPositions()), \
                         (100, self.queenPosition())]

        return int(sum([x[0] * x[1] for x in all_functions]) * 10)

    def utility(self, ply):
        """
        Return the utility of a board.
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
