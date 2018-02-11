from unique import UniqueHashable

"""
    Problem state file defines the classes that are used for representing all
    the information for the MNKY problem. The file implements class Vehicle,
    Package, and State.

    Authors: Mahmud Ahzam*, Tayab Soomro*, Flaviu Vadan*
    Class: CMPT317
    Instructor: Michael Horsch
    Assignment: 1

    * - all authors equally contributed to the implementation
"""

class Vehicle(UniqueHashable):
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

    def __hash__(self):
        return hash((self.position,self.index,self.room))

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

    def __str__(self):
        """
            Format the position of the vehicle.
        """
        return "---------------\nPosition: " + str(self.position) + "\n" +\
                "Index: " + str(self.index) + "\n" +\
                "Room: " + str(self.room) + "\n"

class Package(UniqueHashable):
    position = None
    destination = None
    carried = None
    index = None

    def __init__(self,pos,dest,i,c):
        """
            Constructor method for Package.
            :param position: position of the package.
            :param destination: destionation of the package.

            :return :Package
        """
        self.position = pos
        self.destination = dest
        self.index = i
        self.carried = c

    def __hash__(self):
        return hash((self.position,self.destination,\
                        self.index,self.carried))

    def getIndex(self):
        """ Get index of the package """
        return self.index

    def getPosition(self):
        """ Get the position of package """
        return self.position

    def getDestination(self):
        """ Get the destination of package """
        return self.destination

    def carrier(self):
        """ Determine if the package is carried """
        return self.carried

    def __str__(self):
        """ String Representation of the Package object """
        return "\n----------\nPosition: " + str(self.position) +\
        "\n" + "Destination: " + str(self.destination) +\
        "\nCarried: " + str(self.carried)

class State(UniqueHashable):
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

    def __hash__(self):
        return hash((self.vehicles,self.packages))

    def __eq__(self, other):
        return hash(self) == hash(other)

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
            result = result + str(i)

        result = result + "\n"

        result = result + "Packages: "

        for k, j in self.packages.items():
            result = result + str(j)

        result = result + "\n###############\n"


        return result
