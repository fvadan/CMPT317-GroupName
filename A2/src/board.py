from copy import deepcopy
from constants import Constants

# Types of pieces:
class Piece():
    W,Q,D,E = range(1, 5)

class Board():
    """
    Defines the Board class that holds all the pieces of the game.
    """
    board = None
    utility = -1
    pieces = None

    def __init__(self):
        """
        Empty board.
        """
        self.pieces = dict()

    def constructBoard(self):
        ret = [["--" for i in range(5)] for j in range(5)]
        for k,v in self.pieces.items():
            ret[v[1][0]][v[1][1]] = k
        return ret

    def initialValues(self):
        """
        Default positioning of the pieces.
        """
        # Initialize the positions of queen, wights and dragons
        for i in range(0,5):
            self.pieces["W" + str(i)] = (Piece.W, (4,i))
        for i in range(0,3):
            self.pieces["D" + str(i)] = (Piece.D, (1,i+1))
        self.pieces["QQ"] = (Piece.Q, (0,2))

    def copy(self):
        """
        Return a deep copy of yourself.
        """
        return deepcopy(self)

    def __str__(self):
        """
        String representation of the board.
        """
        retVal = "Board:\n" + "+--+" * 5 + "\n"
        board = self.constructBoard()
        for i in range(len(board)):
            for j in range(len(board)):
                val = board[i][j]
                retVal += "|" + val + "|"
            retVal += '\n' + "+--+" * 5 + "\n"
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

    def isOccupied(self, board, pos):
        """
        If the position is occupied, return what occupies the position.
        Otherwise, return false.
        """
        return board[pos[0]][pos[1]] != "--"

    def canCapture(self, board, attacker, defendant):
        """
        Tell whether attacker can capture defendant.
        """
        if board[attacker[0]][attacker[1]][0] == "W":
            if self.isDiag(attacker, defendant) and\
                    board[defendant[0]][defendant[1]][0] != "W":
                if self.isOccupied(board, defendant):
                    return True
                else:
                    return False
            else:
                if not self.isOccupied(board, defendant):
                    return True
                else:
                    return False
        else: # attacker is either Queen or Dragon
            if self.isOccupied(board, attacker) \
               and (board[defendant[0]][defendant[1]][0] == "W" \
               or not self.isOccupied(board, defendant)):
                return True
        return False

    def neighbours(self, board, pos):
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
                    if self.canCapture(board, (x, y), (i,j)) :
                        res.append((i, j))
        return res


    def possiblePieceMoves(self, board, piece_id):
        """
        Return the list of all the possible movies of a given piece
        :param: piecePos -- the piece to determine the possible moves of.
        """
        possibleSuccessors = []
        pos = self.pieces[piece_id][1]
        p_type = self.pieces[piece_id][0]
        Ns = self.neighbours(board, pos)
        for dest in Ns:
            dest_piece = board[dest[0]][dest[1]]
            new_board = self.copy()
            if dest_piece != "--":
                # Capture in progress:
                new_board.pieces.pop(board[dest[0]][dest[1]])
            new_board.pieces[piece_id] = (p_type, dest)
            possibleSuccessors.append(new_board)
        return possibleSuccessors

    def __hash__(self):
        return hash(tuple([v[1] for k,v in self.pieces.items()]))

