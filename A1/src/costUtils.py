
"""
Class that defines all static methods that are required for cost computation
and other metrics.
"""

def h(state):
    """
        Heuristic function for the M-N-K-Y problem.
    """
    return 100

def metric(point1, point2):
    """
    Return Manhattan distance.
    :return: distance
    """
    return sum([abs(point1[i] - point2[i]) for i in range(len(point1))])

def costFunction(trace):
    """
        Computes the cost of a path through the state space
        :param: trace is the list of states in the path
    """
    # Store distance travelled by each vehicle:
    totalDists = [0 for x in range(len(trace[0].getVehicles()))]
    for i in range(1, len(trace)): # loop through the trace
        diff = stateDiff(trace[i], trace[i-1]) # get the cost difference of
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
        distForI = metric(v1[i].getPosition(), v2[i].getPosition())
        costs[i] += distForI
    return costs
