from costUtils import *

DISTANCE_TO_TIME = 10

"""
    Search node class that defines and implements the search nodes used for
    storing particular states, their origin state, and their cost.

    Authors: Mahmud Ahzam*, Tayab Soomro*, Flaviu Vadan*
    Class: CMPT317
    Instructor: Michael Horsch
    Assignment: 1

    * - all authors equally contributed to the implementation 
"""

class SearchNode():
    """
        Class keeps track of the position of the node in a graph.
    """
    state = None
    pred = None
    cost = 0
    vehicleDistances = None # list corresponding to the distances of all the vehicles.

    def __init__(self, _state, _pred):
        """
            Initializes the search nodes class.
            :param _state: the state to construct.
            :param _pred: the predecessor searchNode.
        """
        self.state = _state
        self.pred = _pred
        self.vehicleDistances = [0] * len(_state.getVehicles())
        # adjust the cost only for non-root search nodes
        if self.pred is not None:
            distancesBetweenVehicles = stateDiff(self.state, self.pred.getState())
            for i in range(len(distancesBetweenVehicles)):
                self.vehicleDistances[i] = _pred.vehicleDistances[i] +\
                                            distancesBetweenVehicles[i]
            time = DISTANCE_TO_TIME * max(self.vehicleDistances)
            self.cost = sum(self.vehicleDistances) + time
        else:
            self.cost = 0

    def __eq__(self, other):
        return hash(self.state) == hash(other.state)

    def __str__(self):
        """
            String method for the SearchNodes
        """
        return "State:" + str(self.state) + "\nCost: " + str(self.cost)

    def getState(self):
        """
            Return state
            :return: state
        """
        return self.state

    def getCost(self):
        """
            Return cost of reaching this search node.
            :return: cost
        """
        return self.cost

    def traceBack(self):
        """
            Trace back to initial state:
            :retrn: list containing result and depth
        """
        depth = 0
        cursor = self.pred
        result  = [self.state]
        while cursor is not None:
            depth += 1
            result.insert(0, cursor.getState())
            cursor = cursor.pred
        return result, depth
