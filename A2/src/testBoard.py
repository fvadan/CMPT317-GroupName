import random
from board import Board, Piece
from gamePlay import minimax, alphaBeta
from evaluate import Evaluate
from hashTable import HashTable
from gameController import Game, runGame

def main():
    b = Board()
    b.initialValues()

    """
    print(b)
    print("Queen neighbours:")
    [print(x) for x in (b.neighbours(b.constructBoard(), (0, 2)))]
    print("Dragon 1 neighbours:")
    [print(x) for x in (b.neighbours(b.constructBoard(), (1, 1)))]
    print("Dragon 2 neighbours:")
    [print(x) for x in (b.neighbours(b.constructBoard(), (1, 2)))]
    print("Dragon 3 neighbours:")
    [print(x) for x in (b.neighbours(b.constructBoard(), (1, 3)))]
    for i in range(0, 5):
        print("Neighbour of wight", i, ":")
        [print(x) for x in b.neighbours(b.constructBoard(), (4, i))]
    #print(b1)

    #print("SUCCESSORS\n")
    [print("\n\n##############\n", x, "\n###########\n")\
        for x in b.possiblePieceMoves(b.constructBoard(), "QQ")]
    [print("\n\n##############\n", x, "\n###########\n")\
        for x in b.possiblePieceMoves(b.constructBoard(), "D0")]
    [print("\n\n##############\n", x, "\n###########\n")\
        for x in b.possiblePieceMoves(b.constructBoard(), "W0")]
    """

    # print(minimax(b, "Player 2", 0, 0))

    # Tests for evaluation function
    # Tests for board hashing:
    """
    tab = HashTable()
    tab[b] = Evaluate(b).evaluation()
    s0 = b.successors("Player 1")
    print("#####")
    print("Successors of initial state:")
    print()
    for i in s0:
        print("#####")
        print(i)
        print(Evaluate(i).evaluation())
        print("#####")

    s1 = b.successors("Player 1")[0].successors("Player 2")
    print("#####")
    print("Successors of initial state:")
    print()
    for i in s1:
        print("#####")
        print(i)
        print(Evaluate(i).evaluation())
        print("#####")
    """
    """
    print("Minimax result of initial node: ",\
        minimax(b, "Player 1", 0, 5))
    print("Alpha-Beta result of initial node: ",\
        alphaBeta(b, "Player 1", 0, 5))
    """

    """
    # Minimax value versus alpha-beta value tests:
    test = Board()
    test.initialValues()
    test.pieces["QQ"] = (Piece.Q ,(2, 2))
    test.pieces["D0"] = (Piece.D, (1, 0))
    test.pieces["D1"] = (Piece.D, (1, 2))
    test.pieces["D2"] = (Piece.D, (2, 4))
    test.pieces["W4"] = (Piece.W, (3, 4))
    test.pieces["W2"] = (Piece.W, (3, 1))
    print(test)

    lim = 4
    util = alphaBeta(test, "Player 1", 0, lim)
    print("alpha beta:", util)
    util_minimax1 = minimax(test, "Player 1", 0, lim)
    print("util_minimax 1:", util_minimax1)

    #util_minimax2 = minimax(b, "Player 2", 0, lim)
    #print("util_minimax 2:", util_minimax2)
    #runGame(lim, minimax)
    """

    # Successor tests:
    test = Board()
    test.pieces["QQ"] = (Piece.Q, (1,1))
    test.pieces["D2"] = (Piece.D, (1,3))
    test.pieces["D1"] = (Piece.D, (2,3))
    test.pieces["W3"] = (Piece.W, (2,2))
    test.pieces["W0"] = (Piece.W, (4,0))
    test.pieces["W1"] = (Piece.W, (4,1))
    test.pieces["W4"] = (Piece.W, (4,4))
    print(test)
    for j in test.successors("Player 2"):
        print(j)
        print(Evaluate(j).utility(1))
        print(Evaluate(j).evaluation())

if __name__ == '__main__':
    main()

