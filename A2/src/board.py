from copy import deepcopy

class Piece():
    W,Q,D,E = range(4)

P1 = "Player 1"
P2 = "Player 2"

class Board():
    """
    Defines the Board class that holds all the pieces of the game.
    """
    board = None
    utility = -1
    wights = None
    dragons = None
    queen = None

    def __init__(self):
        """
        Initialize the board.
        """
        self.board = [[Piece.E for i in range(5)] for j in range(5)]
        self.wights = [(-1,-1)] * 5
        self.dragons = [(-1,-1)] * 3
        self.queen = (-1,-1)

    def initialValues(self):
        """
        Default positioning of the pieces.
        """
        self.board[0][2] = Piece.Q
        self.board[1] = [Piece.E] + [Piece.D] * 3 + [Piece.E]
        self.board[4] = [Piece.W for i in range(5)]

        # Initialize the positions of queen, wights and dragons
        self.queen = (0,2)
        self.wights = [(5,i) for i in range(5)]
        self.dragons = [(1, i) for i in range (1,4)]

    def copy(self):
        """
        Return a deep copy of yourself.
        """
        return deepcopy(self)

    def __str__(self):
        """ String representation of the board """
        retVal = "Board:\n"
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == Piece.W:
                    retVal += 'W'
                elif self.board[i][j] == Piece.Q:
                    retVal += 'Q'
                elif self.board[i][j] == Piece.D:
                    retVal += 'D'
                else:
                    retVal += '-'
            retVal += "\n"
        return retVal

    def neighbours(pos):
        def isLeftEdge(p):
            return False
        def isRightEdge(p):
            return False
        def isTop(p):
            return False
        def isBottom(p):
            return False

        top = [(pos[0]-1, pos[1]-1), (pos[0], pos[1]-1), (pos[0]+1, pos[0]+1)]
        mid = [(pos[0], pos[0]-1), (pos[0], pos[0]+1)]
        bottom = [(pos[0]+1, pos[0]-1), (pos[0]+1, pos[0]), (pos[0]+1, pos[0]+1)]

        return top + mid + bottom

    def successors(self, player):
        """
        Return a list of possible succesors.
        """
        possibleSuccessors = []

        if(player == P1):

            # Queen's move
            nb = self.neighbours(self.queen)
            for i in range(neighbours):
                newBoard = self.copy()
                newBoard.queen = nb[i]
                possibleSuccessors.append(newBoard)
        else:
            return 0
