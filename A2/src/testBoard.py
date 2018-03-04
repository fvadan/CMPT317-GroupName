from board import Board

def main():
    b1 = Board()
    #assert(b1.board != None)
    #print(b1)
    b1.initialValues()
    print(b1)

    print("Queen neighbours:")
    [print(x) for x in (b1.neighbours((0, 2)))]
    print("Dragon 1 neighbours:")
    [print(x) for x in (b1.neighbours((1, 1)))]
    print("Dragon 2 neighbours:")
    [print(x) for x in (b1.neighbours((1, 2)))]
    print("Dragon 3 neighbours:")
    [print(x) for x in (b1.neighbours((1, 3)))]
    for i in range(0, 5):
        print("Neighbour of wight", i, ":")
        [print(x) for x in b1.neighbours((4, i))]
    #print(b1)
    #[print(x) for x in b1.successors("Player 1")]
if __name__ == '__main__':
    main()
