import queue as Queue
import heapq

class HashableDictionary():
    table = None
    name = None
    def __init__(self, n):
        self.table = {}
        self.name = n

    def __hash__(self):
        ret = hash((self.name, *((k,v) for k,v in self.table.items())))
        return ret

    def __getitem__(self, index):
        return self.table[index]

    def __setitem__(self, index, item):
        self.table[index] = item

    def __len__(self):
        return len(self.table)

    def clone(self):
        copy = HashableDictionary(self.name)
        for k,v in self.table.items():
            copy[k] = v
        return copy

    def items(self):
        return self.table.items()

    def pop(self, index):
        self.table.pop(index)

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
    equality = None
    comparator = None

    class HeapElement():

        item = None
        parent = None

        def __init__(self, _item, _parent):
            self.item = _item
            self.parent = _parent

        def __eq__(self, other):
            return self.parent.equality(self.item, other.item)

        def __lt__(self, other):
            return self.parent.comparator(self.item, other.item)

    def __init__(self, _equality, _comparator):
        """
        Constructor that initializes the heap.
        """
        self.heapList = []
        self.equality = _equality
        self.comparator = _comparator

    def enqueue(self, item):
        """
            Enqueue the given item.
        """
        self.num_el += 1
        heapq.heappush(self.heapList, StateHeap.HeapElement(item,self))

    def dequeue(self):
        """
            Dequeue the minimum element in the heap
        """
        self.num_el -= 1
        return heapq.heappop(self.heapList).item

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
