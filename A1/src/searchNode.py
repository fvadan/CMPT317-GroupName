from costUtils import *

DISTANCE_TO_TIME = 0

class SearchNode():
    """
        Class keeps track of the position of the node in a graph.
    """
    state = None
    pred = None
    cost = 0

    def __init__(self, _state, _pred):
        """
            Initializes the search nodes class.
            :param _state: the state to construct.
            :param _pred: the predecessor searchNode.
        """
        self.state = _state
        self.pred = _pred
        # adjust the cost only for non-root search nodes
        if self.pred is not None:
            distancesBetweenVehicles = stateDiff(self.state,\
                                                self.pred.getState())
            totalDistanceTravelled = sum(distancesBetweenVehicles)
            time = DISTANCE_TO_TIME * max(distancesBetweenVehicles)
            self.cost = totalDistanceTravelled + time
        else:
            self.cost = 0

    def isEqual(self, other):
        return self.state == other.state

    def __str__(self):
        """
            String method for the SearchNodes
        """
        return str(self.state)

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
