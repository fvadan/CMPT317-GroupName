from problemState import State, Vehicle, Package
import copy

class Problem():
    """ Problem Class """
    m = None
    n = None
    k = None
    y = None
    currentState = None

    def __init__(self, _m, _n, _k, _y, packs):
        """
        Initializes a problem.
        :param _m: number of vehicles.
        :param _n: number of packages.
        :param _k: capacity of each vehicle.
        :param _y: dimension of the space.
        """
        self.m = _m
        self.n = _n
        self.k = _k
        self.y = _y
        self.currentState = State(
            [Vehicle(tuple([0 for i in range(_y)]), i, _k) for i in range(_m)],
            [Package(packs[i][0], packs[i][1], i) for i in range(len(packs))])

    def getCurrentState(self):
        """
        Return current state.
        :return: state.
        """
        return self.currentState

    def readProblem():
        """
        Reads a problem from standard input.
        Input format: <m>
                      <n>
                      <k>
                      <y>
                      s11 s12 s13 ... s1y | d11 d12 d13 ... d1y
                      s21 s22 s23 ... s2y | d21 d22 d23 ... d2y
                      ...
                      ...
                      sn1 sn2 sn3 ... sny | dn1 dn2 dn3 ... dny
        """
        m = int(input())
        n = int(input())
        k = int(input())
        y = int(input())
        packages = []
        for i in range(n):
            interm = list(map(int,input().strip().split(' ')))
            src = tuple(interm[0:int(len(interm)/2)])
            des =  tuple(interm[int(len(interm)/2):len(interm)])
            packages.append((src, des))

        return Problem(m, n, k, y, packages)

    def successors(self, state):
        """
        Set of possible transitions from the current state.
        :return: list of all possible states.
        """

        possibleSuccessors = []



        for v in state.getVehicles():
            for p in state.getPackages():

                # Vehicle is not carrying this package and it has no more room:
                if p.getPosition() != v.getPosition() and v.getRoom() <= 0:
                    # it can neither pickup this package nor deliver it:
                    continue

                # First, cover the case when you can deliver something
                # For each package picked up by/moving with v:
                else:
                    # Generate a new state:
                    newState = copy.deepcopy(state)

                    if p.getPosition() == v.getPosition():
                        # Change copied state to reflect a delivery:
                        newState.getVehicles()[v.getIndex()].setPosition(p.getDestination())
                        newState.getVehicles()[v.getIndex()].setRoom(v.getRoom() + 1)
                        # a delivered package is no longer under consideration:
                        newState.getPackages().pop(p.getIndex()) # removed

                        # Append to list of possible states:
                        possibleSuccessors.append(newState)

                    # If the vehicle can pick up more packages:
                    elif v.getRoom() > 0:
                        # Change copied state to reflect
                        # a pick up of package p by v:
                        newState.getVehicles()[v.getIndex()].setPosition(p.getPosition())
                        newState.getVehicles()[v.getIndex()].setRoom(v.getRoom() - 1)
                        newState.getPackages()[p.getIndex()].setCarried(v.getIndex())

                        # Append to the list of possible states:
                        possibleSuccessors.append(newState)

            # Vehicle is empty, an option is to go back to origin:
            if v.getRoom() == self.k\
                    and v.getPosition() != tuple([0 for x in range(self.y)]):
                newState = copy.deepcopy(state)
                newState.getVehicles()[v.getIndex()].setPosition(\
                    tuple([0 for i in range(self.y)]))
                possibleSuccessors.append(newState)

        return possibleSuccessors

    def isGoal(self, state):
        """
        Returns whether the given state is the goal state.
        :param state: a State.
        :return: true if goal state, false otherwise.
        """
        origin = tuple([0 for i in range(self.y)])
        for v in state.getVehicles():
            if v.getPosition() != origin:
                return False
        if state.getPackages() != []:
            return False

        return True

    def __str__(self):
        """  String representation of Problem """
        return "(M, N, K, Y) := " + str((self.m, self.n, self.k, self.y)) +\
            "\n" + "Current State:\n" + str(self.currentState)
