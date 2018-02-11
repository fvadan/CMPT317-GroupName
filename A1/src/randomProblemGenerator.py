import sys, math
import matplotlib.pyplot as plt
from search import Search as S
import random as r
from costUtils import *
from problem import Problem

"""
    Random problem generator for the MNKY problem. The file defines and
    implements functions to generate random problems for the MNKY problem
    and generate plots of BFS, DFS, and A* performance. Problems range in
    values having M = [1, 2], N = 3, K = [1, 2], and Y = [1, 2].

    Authors: Mahmud Ahzam*, Tayab Soomro*, Flaviu Vadan*
    Class: CMPT317
    Instructor: Michael Horsch
    Assignment: 1

    * - all authors equally contributed to the implementation
"""

def generateRandomProblem():
    """
        Generate and return a problem.
        :return: problem.
    """
    _m = r.randint(1, 2)
    _n = 10
    _k = r.randint(1, 4)
    _y = r.randint(1, 2)

    packages = []
    for i in range(_n):
        src = tuple([r.random() for i in range(_y)])
        des =  tuple([r.random() for i in range(_y)])
        packages.append((src, des))
    return Problem(_m, _n, _k, _y, packages)

def generateDfsBfsPlot(n):
    """
        Generates a plot.
        :param n: # of random problems to test algorithm on.
    """

    plt.figure()
    plt.xlabel("Problem Number")
    plt.ylabel("Complexity")

    X = []
    Y_B = []

    Y_D = []
    for i in range(int(n)):
        p = generateRandomProblem()
        bfs_trace, bfs_nodes, bfs_depth, bfs_time, bfs_memory, bfs_cost = S.bfs(p)
        dfs_trace, dfs_nodes, dfs_depth, dfs_time, dfs_memory, dfs_cost = S.dfs(p)

        y_bfs = bfs_nodes + bfs_depth + bfs_time + bfs_memory + bfs_cost
        y_dfs = dfs_nodes + dfs_depth + dfs_time + dfs_memory + dfs_cost

        Y_B.append(y_bfs)
        Y_D.append(y_dfs)

        X.append(i)

    plt.plot(X,Y_B, marker='o', linestyle='-', color='r')
    plt.plot(X,Y_D, marker='o', linestyle='-', color='g')
    plt.legend(('BFS','DFS'))
    plt.show()

def generateAStarPlot(n):
    """
        Generates a plot.
        :param n: # of random problems to test algorithm on.
    """
    colors = ['r','g','b','m','c']
    heuristics = [h0,h1,h2,h3,h4]

    plt.figure()
    plt.xlabel("Problem number")
    plt.ylabel("Complexity")

    H_Y = [[]]*5
    X = []
    for i in range(int(n)):
        p = generateRandomProblem()
        results = [S.astar(p, h)[1:] for h in heuristics]
        for j in range(len(results)):
            y = sum(results[j])
            #H_Y[j].append(y)
            #X.append(i)
            plt.plot(i, y, marker='o', linestyle='-', color=colors[j])
    plt.legend(('H1','H2','H3','H4','H5'))

    # plt.plot(X, H_Y[1], marker='o', linestyle='-', color='g', label='H2')
    # plt.plot(X, H_Y[2], marker='o', linestyle='-', color='b', label='H3')
    # plt.plot(X, H_Y[3], marker='o', linestyle='-', color='y', label='H4')
    # plt.plot(X, H_Y[4], marker='o', linestyle='-', color='m', label='H5')
    plt.show()

def main(n):
    """
        Main program that generates statstics for M-N-K-Y Problem with plots.
    """
    #generateDfsBfsPlot(n)
    generateAStarPlot(n)
    #generateDfsBfsPlot(n)

if __name__ == '__main__':
    """
        Entry point
    """
    main(sys.argv[1])
