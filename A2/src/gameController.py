
from constants import Constants
from board import Board
from evaluate import Evaluate
from gamePlay import minimax, alphaBeta

class Game():
    """
    Class to control The Dragon Queen game.
    """
    ply = None
    player = None
    board = None
    successors = None

    def __init__(self):
        """
        Constructor that initializes a board and starts a game.
        """
        self.ply = 0
        self.player = Constants.MAX
        self.board = Board()
        self.board.initialValues()
        self.successors = self.board.successors(self.player)

    def isAtEndGame(self):
        return len(self.successors) == 0 or\
            Evaluate(self.board).utility(self.ply) != Constants.NON_TERMINAL

    def advanceWithAI(self, utility):
        if self.isAtEndGame():
            return
        moves = self.successors
        minimum = Constants.INF
        maximum = Constants.NEGINF
        opponent = Constants.MIN if self.player == Constants.MAX else\
            Constants.MAX
        for i in moves:
            # Utility values for opponent's moves:
            util = utility(self.board, opponent, self.ply + 1, 3)
            if util > maximum:
                maxMove = i
                maximum = util
            elif util < minimum:
                minMove = i
                minimum = util
        # Update Game:
        self.board = maxMove if self.player == Constants.MAX else minMove
        self.ply += 1
        self.player = opponent
        self.successors = self.board.successors(self.player)

    def advanceWithPerson(self):
        pass

game = Game()
while not game.isAtEndGame():
    print("Current Board at ply: " + str(game.ply), "; Player:", game.player)
    print(game.board)
    print("Successors:")
    [print(x.encode()) for x in game.successors]
    print("Advance?\n>")
    input()
    game.advanceWithAI(alphaBeta)



