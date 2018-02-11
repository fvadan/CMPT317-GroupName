import unittest
import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from problemState import Vehicle, Package, State

class PackageTestCase(unittest.TestCase):

    def test_init(self):
        package = Package(0,0)
        self.assertTrue(package.position == 0)
        self.assertTrue(package.destination == 0)
        self.assertFalse(package.carried == True)
        self.assertFalse(package.delivered == True)

    def test_getPosition(self):
        package = Package(0,0)
        self.assertTrue(package.getPosition() == 0)

    def test_getDestination(self):
        package = Package(0,0)
        self.assertTrue(package.getDestination() == 0)

    def test_setPosition(self):
        package = Package(0,0)
        package.setPosition(1)
        self.assertTrue(package.getPosition() == 1)

    def test_setDestination(self):
        package = Package(0,0)
        package.setDestination(1)
        self.assertTrue(package.getDestination() == 1)

    def test_isCarried(self):
        package = Package(0,0)
        self.assertTrue(package.isCarried() == False)

    def test_isDelivered(self):
        package = Package(0,0)
        self.assertTrue(package.isDelivered() == False)

    def test_setCarried(self):
        package = Package(0,0)
        package.setCarried()
        self.assertTrue(package.isCarried())

    def test_setDelivered(self):
        package = Package(0,0)
        package.setDelivered()
        self.assertTrue(package.isDelivered())

    def test_setUnCarried(self):
        package = Package(0,0)
        package.setUnCarried()
        self.assertTrue(package.isCarried() == False)

    def test_setUnDelivered(self):
        package = Package(0,0)
        package.setUnDelivered()
        self.assertTrue(package.isDelivered() == False)



class VehicleTestCase(unittest.TestCase):

    def test_init(self):
        veh = Vehicle(0)
        self.assertTrue(veh.position == 0)
        self.assertTrue(veh.packages == set([]))

    def test_getPosition(self):
        veh = Vehicle(0)
        self.assertTrue(veh.getPosition() == 0)
        self.assertTrue(veh.packages == set([]))

    def test_setPosition(self):
        veh = Vehicle(0)
        veh.setPosition(1)
        self.assertTrue(veh.getPosition() == 1)

    def test_getPackages(self):
        veh = Vehicle(0)
        self.assertTrue(veh.getPackages() == set([]))

    def test_addPackages(self):
        veh = Vehicle(0)
        p = Package(1, 2)
        veh.addPackage(p)
        self.assertTrue(veh.getPackages() == set([p]))

class StateTestCase(unittest.TestCase):

    state = None
    vehicles = None
    packages = None

    def test_init(self):
        vehicles = [Vehicle(0)]
        packages = [Package(2, 1)]
        state = State(vehicles, packages)
        self.assertTrue(set(vehicles) == state.vehicles)
        self.assertTrue(set(packages) == state.packages)

    def test_getVehicles(self):
        vehicles = [Vehicle(0)]
        packages = [Package(2, 1)]
        state = State(vehicles, packages)
        self.assertTrue(set(vehicles) == state.getVehicles())

    def test_getPackages(self):
        vehicles = [Vehicle(0)]
        packages = [Package(2, 1)]
        state = State(vehicles, packages)
        self.assertTrue(set(packages) == state.getPackages())


class ProblemTestCase(unittest.TestCase):

    def test_successor_1(self):
        vehicles = [Vehicle(0)]
        packages = [Package(2, 1)]
        state = State(vehicles, packages)

        # Travel to package at position 2:
        p1 = Package(2,1)
        p1.setCarried()
        p1.setUnDelivered()
        v1 = Vehicle(2)
        v1.addPackage(p1)
        n1 = State([v1],[])

        self.assertTrue([n1] == state.successor())


if __name__ == '__main__':
    unittest.main()
