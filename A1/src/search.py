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
        return []

if __name__ == '__main__':

    p = Problem.readProblem()

    if len(sys.argv) > 1 and sys.argv[1] == "--with-bfs":
        bfs_trace, bfs_nodes, bfs_depth, bfs_time, bfs_memory, bfs_cost = Search.bfs(p)
        print("BFS: " + str(bfs_nodes+bfs_depth+bfs_time+bfs_memory) + "; Cost: " + str(bfs_cost))

    dfs_trace, dfs_nodes, dfs_depth, dfs_time, dfs_memory, dfs_cost = Search.dfs(p)
    print("DFS: " + str(dfs_nodes+dfs_depth+dfs_time+dfs_memory) + "; Cost: " + str(dfs_cost))

    h1_trace, h1_nodes, h1_depth, h1_time, h1_memory, h1_cost = Search.astar(p,h1)
    print("H1: " + str(h1_nodes+h1_depth+h1_time+h1_memory) + "; Cost: " + str(h1_cost))
    h2_trace, h2_nodes, h2_depth, h2_time, h2_memory, h2_cost = Search.astar(p,h2)
    print("H2: " + str(h2_nodes+h2_depth+h2_time+h2_memory) + "; Cost: " + str(h2_cost))
    h3_trace, h3_nodes, h3_depth, h3_time, h3_memory, h3_cost = Search.astar(p,h3)
    print("H3: " + str(h3_nodes+h3_depth+h3_time+h3_memory) + "; Cost: " + str(h3_cost))
    h4_trace, h4_nodes, h4_depth, h4_time, h4_memory, h4_cost = Search.astar(p,h4)
    print("H4: " + str(h4_nodes+h4_depth+h4_time+h4_memory) + "; Cost: " + str(h4_cost))
    h5_trace, h5_nodes, h5_depth, h5_time, h5_memory, h5_cost = Search.astar(p,h5)
    print("H5: " + str(h5_nodes+h5_depth+h5_time+h5_memory) + "; Cost: " + str(h5_cost))

