from costUtils import *

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
            self.cost = self.pred.getCost() + \
                        sum(stateDiff(self.state, self.pred.getState()))
        else:
            self.cost = 0

    def __str__(self):
        """
            String method for the SearchNodes
        """
        return str(self.state)

    def __eq__(self, other):
        """
        Return whether two states are the same from a cost viewpoint.
        :return: whether two states are the same cost-wise.
        """
        return

    def __lt__(self, other):
        """
        Return whether the current state is cheaper, cost-wise, than a given state.
        :return: True if current is less than given, false otherwise.
        """
        return

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
