
import random
from board import Board, Piece
from gamePlay import minimax, alphaBeta
from evaluate import Evaluate
from hashTable import HashTable
from gameController import Game, runGame
from time import time
import matplotlib.pyplot as plt

def generatePlot(depth_limit, minimax_vals, alphabeta_vals, y_label, title):
    """
    Generate graph for node count.
    :param depth_limit: depth limit for the search algorithm
    :param minimax_vals, alphabeta_vals: list of values to be plotted for
                                         each algorithm
    :param y_val: titles of the axes
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


    #run for multiple depths of minimax
    for i in range(1, depth_limit+1):
        #stats for minimax
        minimax_size, minimax_count, minimax_t = runGame(i, minimax, False, True)
        avg_table_size_minimax.append(minimax_size)
        avg_node_count_minimax.append(minimax_count)
        times_per_minimax_run.append(minimax_t*1000)

        #stats for alphabeta
        alphabeta_size, alphabeta_nodes, alphabeta_t = \
            runGame(i, alphaBeta, False, True)
        avg_table_size_alphabeta.append(alphabeta_size)
        avg_node_count_alphabeta.append(alphabeta_nodes)
        times_per_alphabeta_run.append(alphabeta_t*1000)

    generatePlot(depth_limit, avg_table_size_minimax, \
                 avg_table_size_alphabeta, "Average Space" +\
                 "(# nodes in transposition table)",\
                 "Memory")
    generatePlot(depth_limit, avg_node_count_minimax, \
                 avg_node_count_alphabeta, "Average Time (# nodes visited)", \
                 "Search nodes")
    generatePlot(depth_limit, times_per_minimax_run, \
                 times_per_alphabeta_run, "Average Runtime Per Ply (ms)", \
                 "Time per ply")

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
        runGame(depth_limit, HUMAN, AI)


if __name__ == '__main__':
    main()
