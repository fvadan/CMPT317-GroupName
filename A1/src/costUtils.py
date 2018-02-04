import math
"""
File that defines all static methods that are required for cost computation
and other metrics.
"""

def euclidean_metric(p1, p2):
    """
        Returns the euclidean distance between two points
        :param: p1 -- point 1
        :param: p2 -- point 2
    """
    return math.sqrt(sum([\
                    (p1[i] - p2[i]) ** 2 for i in range(len(p1))\
                    ]))

def h2(state):
    origin = [0 for x in range(len(state.getVehicles()[0].getPosition()))]
    distance = 0
    for k1, v in state.getVehicles().items():

        for k2, p in state.getPackages().items():
            src = p.getPosition()
            dest = p.getDestination()
            p_mid = [abs(src[i]-dest[i])/2 for i in range(len(src))]
            distance += euclidean_metric(v.getPosition(), p_mid)
        distance += euclidean_metric(v.getPosition(), origin)
    return distance


def h3(state):
    origin = [0 for x in range(len(state.getVehicles()[0].getPosition()))]
    distance = 0
    for k1, v in state.getVehicles().items():
        closest_mid = v.getPosition()
        for k2, p in state.getPackages().items():
            src = p.getPosition()
            dest = p.getDestination()
            p_mid = [abs(src[i]-dest[i])/2 for i in range(len(src))]
            if euclidean_metric(p_mid, v.getPosition())\
                    < euclidean_metric(closest_mid, v.getPosition()):
                closest_mid = p_mid
        distance += euclidean_metric(closest_mid, v.getPosition())
        distance += euclidean_metric(v.getPosition(), origin)
    return distance

def h(state):
    """
        Heuristic function for the M-N-K-Y problem.
        :param state: a state will vehicles and packages at certain
                      positions.
    """
    delivery_distance = 0
    max_distance = 0
    origin = [0 for x in range(len(state.getVehicles()[0].getPosition()))]
    for key, pack in state.getPackages().items():
        # compute the delivery distance between each package and its destination
        delivery_distance += euclidean_metric(pack.getPosition(), pack.getDestination())
        # get the max single delivery distance a vehicle will have to travel
        if max_distance < euclidean_metric(pack.getDestination(), origin):
            max_distance = euclidean_metric(pack.getDestination(), origin)

    return max_distance + delivery_distance

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
