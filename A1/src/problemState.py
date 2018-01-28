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

    def __str__(self):
        """
        Method that returns the print values of a vehicle.
        :return: formatted output.
        """
        packs = ""
        for i in self.packages:
            packs = packs + str(i) + "\n"
        return "----------\nPosition: " + str(self.position) +\
            "\nPackages on board:\n" + packs


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

    def __str__(self):
        """ String Representation of the Package object """
        return "----------\nPosition: " + str(self.position) +\
        "\n" + "Destination: " + str(self.destination) +\
        "\nCarried: " + str(self.carried) + "\n" + "Delivered: " +\
        str(self.delivered)

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

    def __str__(self):
        """
            String representation of a state for printing:
        """
        result = "Vehicles:\n"
        for i in self.vehicles:
            result = result + str(i) + "\n"

        result = result + "Packages:\n"

        for j in self.packages:
            result = result + str(j) + "\n"

        return result
