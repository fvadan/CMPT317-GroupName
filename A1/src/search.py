from dataStructures import StateStack, StateQueue, StateHeap
from problem import Problem
import problem
from costUtils import *
import time, math, sys

class Search():
    """
        Class deals with the search functionality.
    """

    def bfs(problem):
        """
            Search algorithm
            :param initialState: the initial state that is passed to the
                                    algorithm.
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
            if p.isGoal(curr.getState()):
                trace, depth = curr.traceBack()
                elapsed_time = time.time() - start_time
                print("BSF search results:", \
                      "\n---Expanded nodes: ", exp_nodes, \
                      "\n---Depth: ", depth, " nodes" \
                      "\n---Time: " , round(elapsed_time*1000,2), "ms"\
                      "\n---Memory: ", memory, " nodes"
                      "\n---Cost: ", curr.getCost(), \
                      "\n")
                return trace
            else:
                succ = p.successors(curr)
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
                print("DFS search results:", \
                      "\n---Expanded nodes: ", exp_nodes, \
                      "\n---Depth: ", depth, " nodes" \
                      "\n---Time: " , round(elapsed_time*1000,2), "ms"\
                      "\n---Memory: ", memory, " nodes", \
                      "\n---Cost: ", curr.getCost(), \
                      "\n")
                return trace
            else:
                succ = p.successors(curr)
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

        # Priority queue with the right priority evaluation function:
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
                print("A* search results:", \
                      "\n---Expanded nodes: ", exp_nodes, \
                      "\n---Depth: ", depth, " nodes" \
                      "\n---Time: " , round(elapsed_time*1000,2), "ms"\
                      "\n---Memory: ", memory, " nodes", \
                      "\n---Cost: ", curr.getCost(), \
                      "\n")

                return trace, curr.getCost()

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

    if(len(sys.argv) < 2):
        exit()
    h0 = lambda a: 0
    heuristics = [h0, h1, h2, h3, h4]
    p = Problem.readProblem()
    print(p)
    #bfs_result = Search.bfs(p)
    dfs_result = Search.dfs(p)
    A_star_trace, A_star_cost = Search.astar(p, heuristics[int(sys.argv[1])])

    #for i in A_star_trace:
    #    print(i)
