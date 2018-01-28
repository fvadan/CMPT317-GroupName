"""
    Problem State - defines the structure of the problem state.
"""

from sets import Set

class Vehicle():
    position = None
    packages = None

    def __init__(self, pos):
        """
        Constructor class.
        :param pos: position of the vehicle
        """
        self.position = Set([])
        self.packages = Set([])

    def getPosition():
        """
        Get current position of vehicle.
        :return: position of the vehicle.
        """
        return self.position

    def setPosition(pos):
        """
        Sets the vehicles position to a new one.
        :param pos: the new position.
        """
        self.position = pos

    def getPackages():
        """
        Get list of packages carried by vehicle.
        :return: list of packages.
        """
        return self.packages

    def addPackage(pack):
        """
        Adds a package to the current vehicle.
        :param pack: the package to be added.
        """
        self.packages.union(pack)
        

class Package():
    position = None
    destination = None
    carried = False
    delivered = False

    def __init__(self,position,destination):
        """
            Constructor method for Package
            :param position: position of the package.
            :param destination: destionation of the package.

            :return :Package
        """
        self.position = position
        self.destination = destination
        self.carried = False
        self.delivered = False


        def getPackagePosition(self):
            """ Get the position of package """
            self.position

        def getPackageDestination(self):
            """ Get the destination of package """
            self.destination

        def isCarried(self):
            """ Determine if the package is carried """
            self.carried

        def isDelivered(self):
            """ Determine if the package is delivered """
            self.delivered

class State():
    def __init__(self, vehicles, packages):
        """
            Constructor:
            :param vehicles: set of available Vehicle objects
            :param packages: set of untouched Package objects
        """
        self.vehicles = vehicles
        self.packages = packages

    def getPackages(self):
        """
            Accessor for untouched Packages
            :return Package
        """
        return self.getPackages

    def getVehicles(self):
        """
            Accessor for all vehicles
            :return Vehicle
        """
        return self.vehicles

    def successor(self):
        """
            Set of possible transitions from the current state
            :return State
        """
        return State(self.vehicles, self.packages)

class Single
