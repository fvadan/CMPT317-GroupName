
import random
from board import Board, Piece
from gamePlay import minimax, alphaBeta
from evaluate import Evaluate
from hashTable import HashTable
from gameController import Game, runGame
from time import time
import matplotlib.pyplot as plt
import sys

_print = print
def print(*args, **kwargs):
    kwargs['flush'] = True
    return _print(*args, **kwargs)

def generatePlot(depth_limit, minimax_vals, alphabeta_vals, y_label, title):
    """
    Generate graph for node count.
    :param depth_limit: depth limit for the search algorithm
    :param minimax_vals, alphabeta_vals: list of values to be plotted for
                                         each algorithm
    :param y_val: titles of the axes on the graph to be generated
    :param title: title of the graph to be generated
    """
    plt.figure()
    x_vals = [i for i in range(1, depth_limit+1)]
    plt.plot(x_vals, minimax_vals, marker='o', linestyle='-', \
              color='r', label='Minimax')
    plt.plot(x_vals, alphabeta_vals, marker='o', linestyle='-', \
              color='b', label='Alphabeta')
    plt.legend(loc='upper left')
    plt.xlabel("Depth Limit")
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig('../plots/' + title + '.png')

def parseInput():
    print("---------- Options ----------\n", \
          "\tW -> Wights\n\tD -> Dragons\n\tAI -> all AI\n\tSTATS -> statistics")
    SELECT_PLAYER = False
    HUMAN, ALL_AI, STATS = False, False, False
    print("> ", end='')
    while not SELECT_PLAYER:
        line = input()
        if line == 'W':
            HUMAN = True
            ALL_AI = False
        elif line == 'D':
            HUMAN = False
            ALL_AI = False
        elif line == 'AI':
            HUMAN = False
            ALL_AI = True
        elif line == "STATS":
            HUMAN = False
            ALL_AI = False
            STATS = True
        else:
            print("Please enter again...")
            continue
        break
    return HUMAN, ALL_AI, STATS

def getStats(depth_limit):
    """
    Generate graphs for the statistics returned by a game.
    :param depth_limit: depth limit for the search algorithm
    :return: generated plot
    """

    avg_table_size_minimax = []
    avg_table_size_alphabeta = []
    avg_node_count_minimax = []
    avg_node_count_alphabeta = []
    times_per_minimax_run = []
    times_per_alphabeta_run = []

    print("######")
    print("Statistics Output Format:")
    print("ALGORITHM: SPACE TIME EXEC_TIME_S THR")
    print("######", end="\n\n\n")

    #run for multiple depths of minimax
    for i in range(1, depth_limit+1):
        print("-----\nDEPTH:", i, "\n")
        #stats for minimax
        minimax_size, minimax_count, minimax_t, minimax_thr =\
            runGame(i, minimax, False, True)
        avg_table_size_minimax.append(minimax_size/1000)
        avg_node_count_minimax.append(minimax_count/1000000)
        times_per_minimax_run.append(minimax_t)

        print("MINIMAX GAME: ", end='')
        print(minimax_size, minimax_count, minimax_t, minimax_thr)

        #stats for alphabeta
        alphabeta_size, alphabeta_nodes, alphabeta_t, alphabeta_thr = \
            runGame(i, alphaBeta, False, True)
        avg_table_size_alphabeta.append(alphabeta_size/1000)
        avg_node_count_alphabeta.append(alphabeta_nodes/1000000)
        times_per_alphabeta_run.append(alphabeta_t)

        print("ALPHA_BETA GAME: ", end='')
        print(alphabeta_size, alphabeta_nodes, alphabeta_t, alphabeta_thr)

        print("\nFinished Minimax and AlphaBeta for depth:", i, "\n-----\n\n")

        generatePlot(i, avg_table_size_minimax, \
                     avg_table_size_alphabeta,\
                     "Transposition table size (1000 nodes)",\
                     "Memory_d" + str(i))
        generatePlot(i, avg_node_count_minimax, \
                     avg_node_count_alphabeta, "Average Time (mil. nodes visited)",\
                     "Search nodes_d" + str(i))
        generatePlot(i, times_per_minimax_run, \
                     times_per_alphabeta_run, "Average Runtime Per Ply (s)", \
                     "Time per ply_d" + str(i))

def main():
    """
    Main program that runs the game.
    """
    input_result = parseInput()
    HUMAN, ALL_AI, STATS = input_result[0], input_result[1], input_result[2]
    if STATS:
        print("Maximum depth?")
        print("> ", end='')
        gotDepth = False
        while not gotDepth:
            try:
                depth_limit = int(input())
                if depth_limit <= 0:
                    print("!!Depth must be at least 1!!")
                    continue
                gotDepth = True
            except Exception:
                print("!!Bad input!!")
        getStats(depth_limit)
    else:
        depth_limit = 4
        for j in sys.argv:
            if(j[0:2] == "-d"):
                depth_limit = int(j[2:len(j)])
        print("Using Depth:", depth_limit)
        runGame(depth_limit, alphaBeta, HUMAN, ALL_AI)

if __name__ == '__main__':
    main()
