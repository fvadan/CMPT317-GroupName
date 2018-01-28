from ProblemState import State, Vehicles, Packages

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
            src = tuple([0:len(interm)/2])
            des =  tuple([len(interm)/2:len(interm)])
            packages.append((src, dest))

        return Problem(m, n, k, y, packages)


    def successor(self, state):
    """
        Set of possible transitions from the current state
        :return [State]
    """
        return State(state.vehicles, state.packages)



    def isGoal(self, state):
        return False
