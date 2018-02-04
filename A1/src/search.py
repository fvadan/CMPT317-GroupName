from dataStructures import StateStack
from dataStructures import StateQueue
from dataStructures import StateHeap
from problem import Problem
import problem
from costUtils import *
import time, math

class Search():
    """
        Class deals with the search functionality.
    """

    def bfs(problem):
        """
            Search algorithm
            :param initialState: the initial state that is passed to the algorithm.
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
                      "\n---Memory: ", memory, " nodes", \
                      "\n---Total cost: ", costFunction(trace), \
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
            :param initialState: the initial state that is passed to the algorithm.
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
            if p.isGoal(curr.getState()):
                trace, depth = curr.traceBack()
                elapsed_time = time.time() - start_time
                print("DFS search results:", \
                      "\n---Expanded nodes: ", exp_nodes, \
                      "\n---Depth: ", depth, " nodes" \
                      "\n---Time: " , round(elapsed_time*1000,2), "ms"\
                      "\n---Memory: ", memory, " nodes", \
                      "\n---Total costn: ", costFunction(trace), \
                      "\n")
                return trace
            else:
                succ = p.successors(curr)
                for successor in succ:
                    s.push(successor)
                # adjust memory used if memory use larger than previous record
                if memory < s.getNumEl():
                    memory = s.getNumEl()
        return []

    def ucs(problem):
        """
            Search algorithm
            :param initialState: the initial state that is passed to the algorithm.
        """

        # keep track of the states that were seen before
        seen = {}

        # monitor performance stats
        exp_nodes = 0 # number of nodes expanded
        start_time = time.time() # Time we started the search.
        depth = 0 # the depth of our solution.
        memory = 0 # the max height of the stack for the entire problem

        q = StateHeap(lambda a,b: a.getCost() == b.getCost(), \
                      lambda a,b: a.getCost() < b.getCost())
        q.enqueue(problem.getInitState())
        while q.isEmpty() is False:
            curr = q.dequeue()
            # number of expanded nodes increases every time we pop
            exp_nodes += 1
            if p.isGoal(curr.getState()):
                trace, depth = curr.traceBack()
                elapsed_time = time.time() - start_time
                print("UCS search results:", \
                      "\n---Expanded nodes: ", exp_nodes, \
                      "\n---Depth: ", depth, " nodes" \
                      "\n---Time: " , round(elapsed_time*1000,2), "ms"\
                      "\n---Memory: ", memory, " nodes", \
                      "\n---Total cost: ", costFunction(trace), \
                      "\n")
                return trace
            else:
                succ = p.successors(curr)
                for successor in succ:
                    if successor.getState() not in seen:
                        seen[successor.getState()] = True
                        q.enqueue(successor)
                # adjust memory used if memory use larger than previous record
                if memory < q.getNumEl():
                    memory = q.getNumEl()
        return []

    def astar(problem):
        """
            Search algorithm
            :param initialState: the initial state that is passed to the algorithm.
        """

        # keep track of the states that were seen before
        seen = {}

        # monitor performance stats
        exp_nodes = 0 # number of nodes expanded
        start_time = time.time() # Time we started the search.
        depth = 0 # the depth of our solution.
        memory = 0 # the max height of the stack for the entire problem

        q = StateHeap(lambda a,b: a.getCost() + h(a.getState()) == \
                                  b.getCost() + h(b.getState()), \
                      lambda a,b: a.getCost() + h(a.getState()) < \
                                  b.getCost() + h(b.getState()))
        q.enqueue(problem.getInitState())
        while q.isEmpty() is False:
            curr = q.dequeue()
            # number of expanded nodes increases every time we pop
            exp_nodes += 1
            if p.isGoal(curr.getState()):
                trace, depth = curr.traceBack()
                elapsed_time = time.time() - start_time
                print("A* search results:", \
                      "\n---Expanded nodes: ", exp_nodes, \
                      "\n---Depth: ", depth, " nodes" \
                      "\n---Time: " , round(elapsed_time*1000,2), "ms"\
                      "\n---Memory: ", memory, " nodes", \
                      "\n---Total cost: ", costFunction(trace), \
                      "\n")
                return trace
            else:
                succ = p.successors(curr)
                for successor in succ:
                    if successor.getState() not in seen and \
                       h(successor.getState()) + successor.getCost():
                        seen[successor.getState()] = True
                        q.enqueue(successor)
                # adjust memory used if memory use larger than previous record
                if memory < q.getNumEl():
                    memory = q.getNumEl()
        return []

if __name__ == '__main__':

    #bfsFile = open('bfs.txt','+w')
    #dfsFile = open('dfs.txt','+w')

    p = Problem.readProblem()

    print(p.getValues())
    Search.bfs(p)
    Search.dfs(p)
    Search.ucs(p)
    for i in Search.astar(p):
        print(i)
"""
    for i in range(len(bfsResult)):
        bfsFile.write(str(bfsResult[i]))

    for i in range(len(dfsResult)):
        dfsFile.write(str(dfsResult[i]))
"""
