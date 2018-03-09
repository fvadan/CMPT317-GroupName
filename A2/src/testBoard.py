import random
from board import Board, Piece
from gamePlay import minimax
from evaluate import Evaluate
from hashTable import HashTable

def main():
    b = Board()
    #assert(b1.board != None)
    #print(b1)
    b.initialValues()
    #print(b1)
    """
    print("Queen neighbours:")
    [print(x) for x in (b.neighbours((0, 2)))]
    print("Dragon 1 neighbours:")
    [print(x) for x in (b.neighbours((1, 1)))]
    print("Dragon 2 neighbours:")
    [print(x) for x in (b.neighbours((1, 2)))]
    print("Dragon 3 neighbours:")
    [print(x) for x in (b.neighbours((1, 3)))]
    for i in range(0, 5):
        print("Neighbour of wight", i, ":")
        [print(x) for x in b.neighbours((4, i))]
    #print(b1)
    """
    #print("SUCCESSORS\n")
    #[print("\n\n##############\n", x, "\n###########\n") for x in b.successors("Player 1")]

    #print(minimax(b, "Player 2", 0))

    # Tests for evaluation function

    # Tests for board hashing:
    tab = HashTable()
    tab[b] = Evaluate(b).evaluation()

    print(b)
    print(Evaluate(b).evaluation(), "\n\n")
    b.queen = (2, 2)
    b.board[2][2] = Piece.Q
    b.board[0][2] = Piece.E
    tab[b] = Evaluate(b).evaluation()

    print(b)
    print(Evaluate(b).evaluation(), "\n\n")
    b.wights[0] = (3, 1)
    b.board[4][0] = Piece.E
    b.board[3][1] = Piece.W
    tab[b] = Evaluate(b).evaluation()

    print(b)
    print(Evaluate(b).evaluation(), "\n\n")
    b.dragons[0] = (2, 1)
    b.board[2][1] = Piece.D
    b.board[1][1] = Piece.E
    tab[b] = Evaluate(b).evaluation()

    print(b)
    print(Evaluate(b).evaluation(), "\n\n")

    for k, v in tab.items():
        print("Board:\n", k)
        print("Eval:", str(v))


if __name__ == '__main__':
    main()
