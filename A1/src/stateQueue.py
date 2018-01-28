class stateQueue():
    """State queue class that stores the states."""

    q = None

    def __init__(self):
    """
    Constructor that initializes the queue.
    """
        self.q = Queue()

    def dequeue(self):
    """
    Dequeue/remove the next state from the queue.
    :return: next state.
    """
        return self.q.get()

    def enqueue(self, state):
    """
    Enqueue/add the next state to the queue.
    :param state: the state to be added to the queue.
    """
        self.q.put(state)
