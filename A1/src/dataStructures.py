import queue as Queue
import heapq

class StateStack():
    """
        State stack class that stores the states.
    """

    s = None
    num_el = 0

    def __init__(self):
        """
        Constructor that initializes the stack.
        """
        self.s = []

    def push(self,state):
        """
        Pushes a state onto the stack.
        :param state: the state to be pushed.
        """
        self.num_el += 1
        self.s.append(state)

    def pop(self):
        """"
        Pops a state from the stack
        """
        self.num_el -= 1
        return self.s.pop()

    def getNumEl(self):
        """
        Return the number of elements in the stack.
        :return: number of elements.
        """
        return self.num_el

    def isEmpty(self):
        """
        Tell whether the stack is empty.
        :return: true if empty, false otherwise.
        """
        return self.num_el == 0

class StateQueue():
    """
        State queue class that stores the states.
    """

    q = None
    num_el = 0

    def __init__(self):
        """
            Constructor that initializes the queue.
        """
        self.q = Queue.Queue()

    def dequeue(self):
        """
            Dequeue/remove the next state from the queue.
            :return: next state.
        """
        self.num_el -= 1
        return self.q.get()

    def enqueue(self, state):
        """
        Enqueue/add the next state to the queue.
        :param state: the state to be added to the queue.
        """
        self.q.put(state)
        self.num_el += 1

    def isEmpty(self):
        """
        Determine if queue is empty.
        :return: Boolean -- indicating whether or not if the queue is empty.
        """
        return self.q.empty()

    def getNumEl(self):
        """
        Return the number of elements in the queue.
        :return: num elements
        """
        return self.num_el

class StateHeap():
    """
        A heap based priority queue:
    """
    heapList = None
    num_el = 0

    def __init__(self):
        """
        Constructor that initializes the heap.
        """
        heapList = []

    def enqueue(self, item):
        """
            Enqueue the given item.
        """
        heapq.heappush(self.heapList, item)

    def dequeue(self, item):
        """
            Dequeue the minimum element in the heap
        """
        heapq.heappop(self.heapList, item)

    def getNumEl(self):
        """
        Return the number of elements in the heap.
        :return: number of elements in the heap.
        """
        return self.num_el

    def isEmpty(self):
        """
        Return whether the heap is empty or not.
        :return: true if empty, false otherwise.
        """
        return self.num_el == 0
