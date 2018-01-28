from problemState import State, Vehicle, Package

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
            [Vehicle(tuple([0 for i in range(_y)])) for i in range(len(packs))],
            [Package(i,j) for (i,j) in packs])

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

    def getCurrentState(self):
        """
        Return the current state of the problem.
        :return: current state.
        """
        return self.currentState

    def successor(self, state):
        """
        Set of possible transitions from the current state.
        :return: list of all possible states.
        """

        # vehicles
        #    1. New Package
        #    2. Deliver
        #    3. Return

        possible_states = []

        for v in states.getVehicles():
            # v can carry more:
            list_possible_vehicles = []
            if len(v.getPackages()) < self.k:
                for p in self.state.getPackages():
                    # v moves to p:
                    v_changed = Vehicle(p.getPosition())
                    # v picks up p:
                    v_changed_packages = list(v.getPackages()).append(p)
                    for i in v_changed_packages:
                        v_changed.addPackage(i)
                    # add the v_changed to list of possible vehicles.
                    list_possible_vehicles.append(v_changed)
                    new_vehicles = [Vehicle]

        return State(state.vehicles, state.packages)

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
