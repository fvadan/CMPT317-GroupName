from board import Board

def main():
    b1 = Board()
    assert(b1.board != None)
    print(b1)
    b1.initialValues()
    print(b1)
    print(b1.successors("Player 1"))
    print(b1.successors("Player 2"))
if __name__ == '__main__':
    main()
