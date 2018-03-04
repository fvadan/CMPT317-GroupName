from board import Board
from gamePlay import minimax

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

    print(minimax(b, "Player 2", 0))


if __name__ == '__main__':
    main()
