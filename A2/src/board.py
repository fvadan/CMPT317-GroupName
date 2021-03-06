from constants import Constants

class Piece():
    """
    Types of pieces on the board.
    """
    W,Q,D,E = range(1, 5)
    keyList = ["W" + str(i) for i in range(0,5)] +\
            ["D" + str(i) for i in range(0,4)] + ["QQ"]

class Board():
    """
    Defines the Board class that holds all the pieces of the game.
    """
    pieces = None

    def __init__(self):
        """
        Empty board.
        """
        self.pieces = dict()

    def constructBoard(self):
        """
        Construct the board according to what pieces are on the board.
        """
        ret = [["--" for i in range(5)] for j in range(5)]
        for k,v in self.pieces.items():
            ret[v[1][0]][v[1][1]] = k
        return ret

    def pieceIdentity(self, ident):
        """
        Return the identity of the given piece.
        :param ident: the piece to be identified
        :return: identity of the piece (W, Q, D, or E)
        """
        if ident in self.pieces:
            return self.pieces[ident][0]
        else:
            return Piece.E

    def move(self, key, to_p):
        """
        Move the given piece.
        :param key: key of the piece to be moved
        :param to_p: destination of the piece to be moved
        """
        board_rep = self.constructBoard()
        if key not in self.pieces:
            return None
        from_p = self.pieces[key][1]
        Ns = self.neighbours(board_rep, from_p)
        if to_p in Ns and self.canCapture(board_rep, from_p, to_p):
            newBoard = self.copy()
            attacker = board_rep[from_p[0]][from_p[1]]
            defendant = board_rep[to_p[0]][to_p[1]]
            if attacker in newBoard.pieces:
                newBoard.pieces[attacker] = (self.pieces[attacker][0], to_p)
                if defendant in self.pieces:
                    newBoard.pieces.pop(defendant)
                return newBoard
        return None

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
        newBoard = Board()
        newBoard.pieces = self.pieces.copy()
        return newBoard

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
        Return the list of all the possible moves of a given piece
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

    def successors(self, player):
        """
        Return the list of possible successors of a given board, according
        to the player.
        :param - player: MAX or MIN player
        :return: list of successors of player
        """
        b = self.constructBoard()
        possibleSuccessors = []
        for k,v in self.pieces.items():
            if player == "Player 1" and v[0] == Piece.W:
                # Player 1 does not play Wights:
                continue
            if player == "Player 2" and v[0] != Piece.W:
                # Player 2 plays only wights:
                continue
            possibleSuccessors += self.possiblePieceMoves(b, k)
        return possibleSuccessors

    def encode(self):
        """
        Encode function that returns a list of position tuples.
        :return: position tuples.
        """
        res = tuple([])
        for k in Piece.keyList:
            if k in self.pieces:
                res += self.pieces[k]
        return res

class BoardAdapter():
    """
    Adapter for previous implementation
    """
    board = None
    queen = None
    dragons = None
    wights = None

    def __init__(self, b):
        self.new_scheme = b
        self.board = b.constructBoard()
        self.queen = b.pieces["QQ"][1] if "QQ" in b.pieces else None
        self.dragons = []
        self.wights = []
        for i in ["D0", "D1", "D2"]:
            if i in b.pieces:
                self.dragons.append(b.pieces[i][1])
        for i in ["W0", "W1", "W2", "W3", "W4"]:
            if i in b.pieces:
                self.wights.append(b.pieces[i][1])
