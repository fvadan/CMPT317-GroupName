import sys, math
from search import Search as S
import random as r
from costUtils import *
from problem import Problem


def generateRandomProblem(_m, _n, _k, _y):
    """
        Return Problem
    """
    packages = []
    for i in range(_n):
        src = tuple([r.random() for i in range(_y)])
        des =  tuple([r.random() for i in range(_y)])
        packages.append((src, des))
    return Problem(_m, _n, _k, _y, packages)

def main(_m,_n,_k,_y):
    """
        Main program that generates n random test cases and generates the plots.
    """
    heuristics = [h0, h1, h2, h3, h4]

    p = generateRandomProblem(_m, _n, _k, _y)

    h0_trace, h0_cost = S.astar(p,h0)
    h1_trace, h1_cost = S.astar(p,h1)
    h2_trace, h2_cost = S.astar(p,h2)
    h3_trace, h3_cost = S.astar(p,h3)
    h4_trace, h4_cost = S.astar(p,h4)

if __name__ == '__main__':
    _m = 0
    _n = 0
    _k = 0
    _y = 0
    if len(sys.argv) < 5:
        _m = 1 # std is 10
        _n = 1
        _k = 1
        _y = 1
    else:
        _m = int(sys.argv[1]) # std is 10
        _n = int(sys.argv[2])
        _k = int(sys.argv[3])
        _y = int(sys.argv[4])
        if len(sys.argv) > 5:
            for i in range(int(sys.argv[5])):
                main(_m, _n, _k, _y)
                print("Complete ", i + 1, file=sys.stderr)
        else:
            main(_m,_n,_k,_y)

