from gameController import *
from gamePlay import alphaBeta, minimax
from time import time

for i in range(1,8):
    game = Game(i)
    start = time()
    game.advanceWithAI(alphaBeta)
    end = time()
    print("Time for depth",i, ":", (end-start))

