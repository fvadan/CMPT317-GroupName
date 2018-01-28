"""
    Problem State - defines the structure of the problem state.
"""

class Vehicle():
    position = None
    packages = None

    def __init__(self, pos):
        """
        Constructor class.
        :param pos: position of the vehicle.
        """
        self.position = pos
        self.packages = set([])

    def getPosition(self):
        """
        Get current position of vehicle.
        :return: position of the vehicle.
        """
        return self.position

    def setPosition(self, pos):
        """
        Sets the vehicles position to a new one.
        :param pos: the new position.
        """
        self.position = pos

    def getPackages(self):
        """
        Get list of packages carried by vehicle.
        :return: set of packages.
        """
        return self.packages

    def addPackage(self, pack):
        """
        Adds a package to the current vehicle.
        :param pack: the package to be added.
        """
        self.packages = self.packages.union([pack])


class Package():
    position = None
    destination = None
    carried = False
    delivered = False

    def __init__(self,pos,dest):
        """
            Constructor method for Package.
            :param position: position of the package.
            :param destination: destionation of the package.

            :return :Package
        """
        self.position = pos
        self.destination = dest
        self.carried = False
        self.delivered = False



    def getPosition(self):
        """ Get the position of package """
        return self.position

    def getDestination(self):
        """ Get the destination of package """
        return self.destination

    def setPosition(self,pos):
        """ Set the position of package """
        self.position = pos

    def setDestination(self,dest):
        """ Set the destination of package """
        self.destination = dest

    def isCarried(self):
        """ Determine if the package is carried """
        return self.carried

    def isDelivered(self):
        """ Determine if the package is delivered """
        return self.delivered

    def setCarried(self):
        """ Set the carried to be True """
        self.carried = True

    def setDelivered(self):
        """ Set the delivered to be True """
        self.delivered = True

    def setUnCarried(self):
        """ Set the carried to be False """
        self.carried = False

    def setUnDelivered(self):
        """ Set the delivered to be False """
        self.delivered = False

class State():
    vehicles = None
    packages = None

    def __init__(self, v, p):
        """
            Constructor:
            :param vehicles: set of available Vehicle objects
            :param packages: set of untouched Package objects
        """
        self.vehicles = set(v)
        self.packages = set(p)

    def getPackages(self):
        """
            Accessor for untouched Packages
            :return Package
        """
        return self.packages

    def getVehicles(self):
        """
            Accessor for all vehicles
            :return Vehicle
        """
        return self.vehicles


class SimpleState(State):
    """
        Problem state where (M,N,K,Y)=(1,1,1,1)
    """
    def __init__(self):
        i = "lol"
