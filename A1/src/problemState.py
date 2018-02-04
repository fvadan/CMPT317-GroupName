"""
    Problem State - defines the structure of the problem state.
"""

class Vehicle():
    index = None
    position = None
    room = None

    def __init__(self, pos, i, r):
        """
        Constructor class.
        :param pos: position of the vehicle.
        :param i: index of the vehicle.
        :param r: room available, initially k.
        """
        self.position = pos
        self.index = i
        self.room = r

    def setRoom(self, r):
        """
        Set number of spaces left for packages.
        :param r: the leftover room
        """
        self.room = r

    def getRoom(self):
        """
        Return leftover room for packages.
        :return: room available.
        """
        return self.room

    def getIndex(self):
        """
        Return the index of the vehicle.
        :return: index.
        """
        return self.index

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

    def __str__(self):
        """
        Format the position of the vehicle.
        """
        return "---------------\nPosition: " + str(self.position) + "\n"

class Package():
    position = None
    destination = None
    carried = None
    index = None

    def __init__(self,pos,dest,i):
        """
            Constructor method for Package.
            :param position: position of the package.
            :param destination: destionation of the package.

            :return :Package
        """
        self.position = pos
        self.destination = dest
        self.carried = None
        self.index = i

    def getIndex(self):
        """ Get index of the package """
        return self.index

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
        return (self.position == self.destination)

    def setCarried(self, c):
        """ Set the carried to be True """
        self.carried = c

    def __str__(self):
        """ String Representation of the Package object """
        return "\n----------\nPosition: " + str(self.position) +\
        "\n" + "Destination: " + str(self.destination) +\
        "\nCarried: " + str(self.carried)

class State():
    vehicles = None
    packages = None

    def __init__(self, v, p):
        """
            Constructor:
            :param vehicles: array of available Vehicle objects
            :param packages: set of untouched Package objects
        """
        self.vehicles = v
        self.packages = p

    def getPackages(self):
        """
            Accessor for untouched Packages
            :return: Package
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
        result = "###############\n"
        result += "Vehicles:\n"
        for k, i in self.vehicles.items():
            result = result + str(i) + " "

        result = result + "\n"

        result = result + "Packages: "

        for k, j in self.packages.items():
            result = result + str(j)

        result = result + "\n###############\n"


        return result
