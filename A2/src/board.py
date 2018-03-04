from copy import deepcopy

class Piece():
    W,Q,D,E = range(1, 5)

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
        """
        String representation of the board.
        """
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

    def isDiag(self, p1, p2):
        """
        Return whether two points are diagonal to each other.
        """
        if p1 == (p2[0]-1, p2[1]-1) \
        or p1 == (p2[0]+1, p2[1]+1) \
        or p1 == (p2[0]+1, p2[1]-1) \
        or p1 == (p2[0]-1, p2[1]+1):
            return True
        return False

    def neighbours(self, pos):
        """
        Return the possible neighbours.
        """
        res = []
        x,y = pos[0], pos[1]
        I = x-1
        J = y-1
        for i in range(I, I+3):
            for j in range(J, J+3):
                if i < 0 or j < 0 or i > 4 or j > 4 or (i,j) == pos:
                    continue
                else:
                    if self.canCapture((x, y), (i,j)) :
                        res.append((i, j))
        return res

    def isOccupied(self, pos):
        """
        If the position is occupied, return what occupies the position.
        Otherwise, return false.
        """
        return self.board[pos[0]][pos[1]] != Piece.E

    def canCapture(self, attacker, defendant):
        """
        Tell whether attacker can capture defendant.
        """
        if self.board[attacker[0]][attacker[1]] == Piece.W:
            if self.isDiag(attacker, defendant):
                if self.isOccupied(defendant):
                    return True
                else:
                    return False
            else:
                if not self.isOccupied(defendant):
                    return True
                else:
                    return False
        else: # attacker is either Queen or Dragon
            if self.isOccupied(attacker) \
               and (self.board[defendant[0]][defendant[1]] == Piece.W \
               or not self.isOccupied(defendant)):
                return True
        return False

    def isTerminal(self, ply):
        """
        Determine if a given board state is a terminal state
        """
        max_ply = 50

        # Queen reaches the Wight's home row
        if self.board.queen[1] == 4:
            return True

        # Queen is captured
        if self.board.queen == None:
            return True

        # Reached max ply
        if ply == max_ply:
            return True

        return False

    def identity(self, pos):
        """
        Tell what piece was given.
        """
        return self.board[pos[0]][pos[1]]

    def possiblePieceMoves(self, piecePos):
        """
        Return the list of all the possible movies of a given piece
        :param: piecePos -- the piece to determine the possible moves of.
        """
        possibleMoves = []
        # All valid neighbours:
        for neighbour in self.neighbours(piecePos):
            newBoard = self.copy()
            newBoard.board[neighbour[0]][neighbour[1]] = piecePos
            if self.identity(neighbour) == Piece.W:
                newBoard.wights.pop( \
                    newBoard.wights.index(neighbour))
            elif self.identity(neighbour) == Piece.Q:
                newBoard.queen = None
            elif self.identity(neighbour) == Piece.D:
                newBoard.dragons.pop(
                    newBoard.dragons.index(neighbour))
            possibleMoves.append(newBoard)
        return possibleMoves

    def successors(self, player):
        """
        Return a list of possible succesors.
        """
        possibleSuccessors = []

        if(player == P1):
            # Queen moves
            possibleSuccessors += self.possiblePieceMoves(self.queen)

            # Dragons' moves
            for dragon in self.dragons:
                possibleSuccessors += self.possiblePieceMoves(dragon)

        else:
            # Wights moves
            for wight in self.wights:
                possibleSuccessors += self.possiblePieceMoves(wight)

        return possibleSuccessors
