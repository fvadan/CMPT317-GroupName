import random
from board import Board, Piece
from gamePlay import minimax
from evaluate import Evaluate
from hashTable import HashTable

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



    """
    # print(minimax(b, "Player 2", 0, 0))

    # Tests for evaluation function
    # Tests for board hashing:
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

    s1 = b.successors("Player 2")
    print("#####")
    print("Successors of initial state:")
    print()
    for i in s1:
        print("#####")
        print(i)
        print(Evaluate(i).evaluation())
        print("#####")
    """

    print(minimax(b, "Player 1", 0, 0))

if __name__ == '__main__':
    main()
