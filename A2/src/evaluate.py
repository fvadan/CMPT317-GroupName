from board import Board, Piece

MAX_SCORE = 200
MIN_SCORE = -200
# Status Constants:
PLAYER_1_WIN = MAX_SCORE
PLAYER_2_WIN = MIN_SCORE
DRAW = 0
NON_TERMINAL = 404
MAX_PLY = 50
P1 = "Player 1"
P2 = "Player 2"


def manhattan_dist(p1,p2):
    """
    Return Manhattan distnace between two points.
    :return: distance
    """
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

class Evaluate():
    board = None
    def __init__(self, board):
        self.board = board

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
        W1, W2, W3, W4, W5, W6 = 20, -5, 10, -10, 15, MIN_SCORE
        evaulation_value = 0

        # Displacement of queen
        dest_queen_pos_y = 4
        disp_q = abs(dest_queen_pos_y  - self.board.queen[0]) * W1

        # Queen under attack?
        queen_attacked = self.queenUnderAttack() * W6

        # Displacement of wights, Manhattan distance
        disp_w = ((sum([manhattan_dist(w, self.board.queen) for w in self.board.wights]))\
                    /len(self.board.wights)) * W2

        # Number of wights
        num_w = len(self.board.wights) * W4

        # Number of dragons
        num_d = len(self.board.dragons) * W5

        # Displacement dragons
        dest_dragon_pos = 4
        disp_d = (sum([abs(d[0] - dest_dragon_pos) for d in self.board.dragons])) * W3

        print("Values: ", disp_w, num_w, disp_d, num_d, disp_q, queen_attacked)
        # Actuall Evalution Value
        evaluation_value = disp_w + num_w + disp_d + num_d + disp_q + queen_attacked

        """
        # if evaluate_value > 100:
        #     evaluate_value = 100
        # elif evaluate_value < 100:
        #       evaluate_value = -100
        """
        # Normalize
        norm_eval = ((evaluation_value - MIN_SCORE)/(MAX_SCORE - MIN_SCORE)) * 100

        return norm_eval, evaluation_value

    def utility(self, ply):
        """
        Return the utility of a board.
        """

        # Queen reaches the Wight's home row
        if self.board.queen[0] == 4:
            return PLAYER_1_WIN

        # Queen is captured
        if self.board.queen == None:
            return PLAYER_2_WIN

        # Reached max ply
        if ply == MAX_PLY:
            return DRAW

        return NON_TERMINAL

    def queenUnderAttack(self):
        """
        Determine whether queen is under attack.
        :return: 1 if under attack, 0 otherwise.
        """
        x, y = self.board.queen[0], self.board.queen[1]
        I, J = x - 1, y - 1

        for i in range(I, I+3):
            for j in range(J, J+3):
                if i < 0 or j < 0 or i > 4 or j > 4 or (i,j) == self.board.queen:
                    continue
                elif self.board.board[i][j] == Piece.W:
                    return 1
        return 0
