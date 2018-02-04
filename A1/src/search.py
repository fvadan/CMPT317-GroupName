from dataStructures import StateStack
from dataStructures import StateQueue
from problem import Problem
import problem
import time, math

class Search():
    """
        Class deals with the search functionality.
    """

    def costFunction(trace):
        """
            Computes the cost of a path through the state space
            :param: trace is the list of states in the path
        """
        # Store distance travelled by each vehicle:
        totalDists = [0 for x in range(len(trace[0].getVehicles()))]
        for i in range(1, len(trace)): # loop through the trace
            diff = Search.stateDiff(trace[i], trace[i-1]) # get the cost difference of
                                                    # the i'th and i-1'th state.
            for j in range(len(diff)): # Add to each vehicle's total distance
                totalDists[j] += diff[j]
        return (sum(totalDists) + max(totalDists))

    def stateDiff(state1, state2):
        """
            Returns list of distances of all the vehicles in both states passed
            in as parameters.
            :param: state1 comparate
            :param: state2 comparate
        """
        v1 = state1.getVehicles() # list of all the vehicles in state1
        v2 = state2.getVehicles() # list of all the vehicles in state2
        costs = [0 for x in range(len(v1))]
        for i in range(len(v1)): # loop through all vehicles
            distForI = problem.metric(v1[i].getPosition(), v2[i].getPosition())
            costs[i] += distForI
        return costs

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
                      "\n---Cost Function: ", Search.costFunction(trace), \
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
                      "\n---Cost Function: ", Search.costFunction(trace), \
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
                      "\n---Cost Function: ", Search.costFunction(trace), \
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

if __name__ == '__main__':

    bfsFile = open('bfs.txt','+w')
    dfsFile = open('dfs.txt','+w')

    p = Problem.readProblem()
    print(p.getValues())

    bfsResult = Search.bfs(p)
    dfsResult = Search.dfs(p)

    for i in range(len(bfsResult)):
        bfsFile.write(str(bfsResult[i]))

    for i in range(len(dfsResult)):
        dfsFile.write(str(dfsResult[i]))
