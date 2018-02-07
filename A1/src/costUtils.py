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
    return math.sqrt(sum([(p1[i] - p2[i]) ** 2 for i in range(len(p1))]))

def h0(state):
    return 0

def h1(state):
    """
        Heuristic:
        total delivery distance + return distance heuristic
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

def h2(state):
    """
        Heuristic:
        distances to mid-points of all delivery lines for all packages
        + return distance
        :param state: a state will vehicles and packages at certain
                      positions.
    """
    origin = [0 for x in range(len(state.getVehicles()[0].getPosition()))]
    numVehiclesAtOrigin = 0
    for k, v in state.getVehicles().items():
        if v.getPosition() == origin:
            numVehiclesAtOrigin+=1
    distance = 0
    distance += 10 * numVehiclesAtOrigin
    for k1, v in state.getVehicles().items():
        for k2, p in state.getPackages().items():
            if p.carrier() is not None and p.carrier() != v.getIndex():
                continue
            src = p.getPosition()
            dest = p.getDestination()
            p_mid = [abs(src[i]-dest[i])/2 for i in range(len(src))]
            distance += euclidean_metric(v.getPosition(), p_mid)
        distance += euclidean_metric(v.getPosition(), origin)
    return distance

def h3(state):
    """
        Heuristic:
        distance to mid-point of minimum delivery line for all packages
        + return distance
        :param state: a state will vehicles and packages at certain
                      positions.
    """
    origin = [0 for x in range(len(state.getVehicles()[0].getPosition()))]
    numVehiclesAtOrigin = 0
    for k,v in state.getVehicles().items():
        if v.getPosition() == origin:
            numVehiclesAtOrigin +=1
    distance = 0
    distance += 10 * numVehiclesAtOrigin
    for k1, v in state.getVehicles().items():
        closest_mid = v.getPosition()
        for k2, p in state.getPackages().items():
            src = p.getPosition()
            dest = p.getDestination()
            p_mid = [abs(src[i]-dest[i])/2 for i in range(len(src))]
            # Only add the minimum distance to a mid position instead of all
            # package destination mid-points:
            if euclidean_metric(p_mid, v.getPosition()) \
                    < euclidean_metric(closest_mid, v.getPosition()):
                closest_mid = p_mid
        distance += euclidean_metric(closest_mid, v.getPosition())
        distance += euclidean_metric(v.getPosition(), origin)
    return distance

def h4(state):
    """
        Heuristic that returns max source and destination distance of all
        the packages.
        :return: distance
    """
    farthest_s = 0
    farthest_d = 0
    origin = [0 for x in range(len(state.getVehicles()[0].getPosition()))]
    for k, p in state.getPackages().items():
        if p.isDelivered() is False:
            if euclidean_metric(origin, p.position) > farthest_s:
                farthest_s = euclidean_metric(origin, p.position) > farthest_s
            if euclidean_metric(origin, p.destination) > farthest_d:
                farthest_d = euclidean_metric(origin, p.destination) > farthest_d
    return farthest_s + farthest_d

def metric(point1, point2):
    """
    Return Manhattan distance.
    :return: distance
    """
    return sum([abs(point1[i] - point2[i]) for i in range(len(point1))])

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
