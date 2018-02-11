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
            :param: problem which contains initialState
            :param: heuristic funciton to use.
        """
        # monitor performance stats
        exp_nodes = 0 # number of nodes expanded
        start_time = time.time() # Time we started the search.
        depth = 0 # the depth of our solution.
        memory = 0 # the max memory in use i.e. size of data structure

        # keep track of the states that were evaluated already
        seen = {}

        # initialize a queue that keeps track of successors that
        # were not evaluted yet
        q = StateHeap(lambda a,b: a.getCost() + h(a.getState()) == \
                                  b.getCost() + h(b.getState()),   \
                      lambda a,b: a.getCost() + h(a.getState()) <  \
                                  b.getCost() + h(b.getState()))

        # add initial state to the queue
        q.enqueue(problem.getInitState())

        # keep getting states from the queue until we find the goal
        while q.isEmpty() is False:

            # search node having the least cost
            curr = q.dequeue()

            # number of expanded nodes increases every time we pop
            exp_nodes += 1

            # mark as seen, issue with hashing was fixed
            seen[curr.getState()] = True

            # return the goal when you find it
            if problem.isGoal(curr.getState()):
                elapsed_time = time.time() - start_time
                trace, depth = curr.traceBack()
                return trace, exp_nodes, depth, round(elapsed_time*1000,2), memory, curr.getCost()
            successors = problem.successors(curr)
            # for each successor of the current search node
            for s in successors:
                # ignore the node which is already evaluated
                if s.getState() in seen:
                    continue
                else:
                    q.enqueue(s)
            if len(q) > memory:
                memory = len(q)
        return []

if __name__ == '__main__':

    if(len(sys.argv) < 2):
        exit()

    heuristics = [h0, h1, h2, h3, h4]
    heuristic = int(sys.argv[1])

    p = Problem.readProblem()

    #bfs_trace, bfs_nodes, bfs_depth, bfs_time, bfs_memory, bfs_cost = Search.bfs(p)
    #dfs_trace, dfs_nodes, dfs_depth, dfs_time, dfs_memory, dfs_cost = Search.dfs(p)
    astar_trace, astar_nodes, astar_depth, astar_time, astar_memory, astar_cost = \
        Search.astar(p, heuristics[heuristic])

    #bfs_overall = bfs_nodes + bfs_depth + bfs_time + bfs_memory + bfs_cost
    #dfs_overall = dfs_nodes + dfs_depth + dfs_time + dfs_memory + dfs_cost
    astar_overall = astar_nodes + astar_depth + astar_time + astar_memory + \
                    astar_cost

    print("\nProblem: ", p, "\n")
    """
    print("BFS results\n--nodes: ", bfs_nodes, "\n--depth: ", bfs_depth, \
           "\n--time: ", bfs_time, "\n--memory: ", bfs_memory, "\n--cost: ", \
           bfs_cost, "\n", "----------overall: ", bfs_overall, "\n")

    print("DFS results\n--nodes: ", dfs_nodes, "\n--depth: ", dfs_depth, \
           "\n--time: ", dfs_time, "\n--memory: ", dfs_memory, "\n--cost: ", \
           dfs_cost, "\n", "----------overall: ", dfs_overall, "\n")
    """
    print("A* results on h", heuristic, "\n--nodes: ", astar_nodes, \
           "\n--depth: ", astar_depth, "\n--time: ", astar_time, "\n--memory: ", \
           astar_memory, "\n--cost: ", astar_cost, "\n", \
           "----------overall: ", astar_overall, "\n")
