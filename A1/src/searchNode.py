class SearchNode():
    """
        Class keeps track of the position of the node in a graph.
    """
    state = None
    pred = None

    def __init__(self, _state, _pred):
        """
            Initializes the search nodes class.
            :param _state: the state to construct.
            :param _pred: the predecessor state.
        """
        self.state = _state
        self.pred = _pred

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

    def traceBack():
        """
            Trace back to initial state:
        """
        return []
