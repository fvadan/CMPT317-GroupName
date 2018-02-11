from dataStructures import StateStack, StateQueue, StateHeap
from problem import Problem
import problem
from costUtils import *
import time, math, sys

"""
    Search class that implements the search algorithms used in the MNKY problem.
    The class defined BFS, DFS, and A* search.

    Authors: Mahmud Ahzam*, Tayab Soomro*, Flaviu Vadan*
    Class: CMPT317
    Instructor: Michael Horsch
    Assignment: 1

    * - all authors equally contributed to the implementation
"""

class Search():
    """
        Class deals with the search functionality.
    """

    def bfs(problem):
        """
            Search algorithm
            :param initialState: the initial state that is passed to the
                                    algorithm.
            :return:

        """
        # monitor performance stats
        exp_nodes = 0 # number of nodes expanded
        start_time = time.time() # Time we started the search.
        depth = 0 # the depth of our solution.
        memory = 0 # the max width of the queue for the entire problem run

        q = StateQueue()
        q.enqueue(problem.getInitState())
        while q.isEmpty() is False:
            curr = q.dequeue()
            # number of expanded nodes increases every time we dequeue
            exp_nodes += 1
            if problem.isGoal(curr.getState()):
                trace, depth = curr.traceBack()
                elapsed_time = time.time() - start_time
                return trace, exp_nodes, depth, round(elapsed_time*1000,2), memory, curr.getCost()
            else:
                succ = problem.successors(curr)
                for successor in succ:
                    q.enqueue(successor)
                # adjust memory used if memory use larger than previous record
                if memory < q.getNumEl():
                    memory = q.getNumEl()
        return []

    def dfs(problem):
        """
            Search algorithm
            :param initialState: the initial state that is passed to the
                                    algorithm.
            :return:
                list containing following items:
                - Trace, expanded_nodes, depth, clock time, memory and cost
        """

        # monitor performance stats
        exp_nodes = 0 # number of nodes expanded
        start_time = time.time() # Time we started the search.
        depth = 0 # the depth of our solution.
        memory = 0 # the max height of the stack for the entire problem

        s = StateStack()
        s.push(problem.getInitState())
        while s.isEmpty() is False:
            curr = s.pop()
            # number of expanded nodes increases every time we pop
            exp_nodes += 1
            if problem.isGoal(curr.getState()):
                trace, depth = curr.traceBack()
                elapsed_time = time.time() - start_time
                return trace, exp_nodes, depth, round(elapsed_time*1000,2), memory, curr.getCost()
            else:
                succ = problem.successors(curr)
                memory += len(succ)
                for successor in succ:
                    s.push(successor)
                # adjust memory used if memory use larger than previous record
                if memory < s.getNumEl():
                    memory = s.getNumEl()
        return []

    def astar(problem, h):
        """
            Covers uniform cost search if h == lambda a: 0
            :param: problem which contains initialState
            :param: heuristic funciton to use.
        """
        # monitor performance stats
        exp_nodes = 0 # number of nodes expanded
        start_time = time.time() # Time we started the search.
        depth = 0 # the depth of our solution.
        memory = 0 # the max memory in use i.e. size of data structure

        seen = {}
        q = StateHeap(lambda a,b: a.getCost() + h(a.getState()) == \
                                  b.getCost() + h(b.getState()),   \
                      lambda a,b: a.getCost() + h(a.getState()) <  \
                                  b.getCost() + h(b.getState()))

        q.enqueue(problem.getInitState())

        while q.isEmpty() is False:
            curr = q.dequeue()
            exp_nodes += 1
            # This reduces hash conflicts but increases time:
            # seen[(curr.getState(), curr.getPlanStep())] = True
            seen[curr.getState()] = True
            if problem.isGoal(curr.getState()):
                elapsed_time = time.time() - start_time
                trace, depth = curr.traceBack()
                return trace, exp_nodes, depth, round(elapsed_time*1000,2), memory, curr.getCost()
            successors = problem.successors(curr)
            for s in successors:
                if s.getState() in seen:
                    continue
                else:
                    q.enqueue(s) # Handles cost modification as well
            if len(q) > memory:
                memory = len(q)
        # Search failed:
        return [],-1,-1,-1,-1,-1

def readPlan(trace):
    result = "##########\nPlan:\n"
    for i in trace:
        result += i[1]
    return result + "##########"

if __name__ == '__main__':

    p = Problem.readProblem()

    heuristics = [h1,h2,h3,h4,h5]

    runBFS = False
    printPlan = False
    for i in sys.argv:
        if i == "--run-bfs":
            runBFS = True
        if i == "--print-plan":
            printPlan = True

    if runBFS:
        bfs_trace, bfs_nodes, bfs_depth, bfs_time, bfs_memory, bfs_cost = Search.bfs(p)
        print("----------")
        print("BFS: " + str(bfs_nodes+bfs_depth+bfs_time+bfs_memory) + "; Cost: " + str(bfs_cost))
        if printPlan:
            print(readPlan(bfs_trace))

    dfs_trace, dfs_nodes, dfs_depth, dfs_time, dfs_memory, dfs_cost = Search.dfs(p)
    print("----------")
    print("DFS: " + str(dfs_nodes+dfs_depth+dfs_time+dfs_memory) + "; Cost: " + str(dfs_cost))
    if printPlan:
        print(readPlan(dfs_trace))

    i = 1
    for h in heuristics:
        result = list(Search.astar(p, h))
        trace = result[0]
        load_count = sum(result[1:5])
        cost = result[5]
        print("----------")
        print("H" + str(i) + ": Load: " + str(load_count) + "; Cost: " +\
                str(cost))
        if printPlan:
            print(readPlan(trace))
        i += 1

