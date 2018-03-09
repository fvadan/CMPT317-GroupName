from board import Board, Piece

MAX_SCORE = 100
MIN_SCORE = -100
# Status Constants:
PLAYER_1_WIN = 1
PLAYER_2_WIN = -1
DRAW = 0
NON_TERMINAL = 404
MAX_PLY = 50
P1 = "Player 1"
P2 = "Player 2"

class Evaluate():
    board = None
    def __init__(self, board):
        self.board = board

    def evaluation(self):
        """
        Return the evaluation of the current state/board.
        Evaluation is determined by following factors:
            1. Displacement of queen * (W1 = 20)
            2. Dislacement of wights * (W2 = 5)
            3. Displacement of dragon * (W3 = 6)
            4. Number of wights * (W4 = -3)
            5. Number of dragons * (W5 = 4)
            6. Queen under attack * (W6 = -40)  <-- (0 or 1) * wights
        :return: evaluation value.
        """
        # Weights for different evalution features.
        W1, W2, W3, W4, W5, W6 = 20, 5, 6, -3, 4, -40
        evaulation_value = 0

        # Displacement of queen
        dest_queen_pos_y = 4
        displacement_queen = abs(dest_queen_pos_y  - self.board.queen[0]) * W1

        # Queen under attack?
        queen_attacked = self.queenUnderAttack() * W6

        # Displacement of wights
        initial_wight_position = 4
        disp_w = sum([abs(w[0] - initial_wight_position) for w in self.board.wights]) * W2
        
        # Displacement of dragons
        num_d = len(self.board.dragons) * W5
        evaluation_value = disp_w + num_d + queen_attacked

        # Normalize
        norm_eval = ((evaluation_value - MIN_SCORE)/(MAX_SCORE - MIN_SCORE)) * MAX_SCORE

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
