import unittest
import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from problemState import Vehicle, Package, State
from problem import *

class ProblemTestCase(unittest.TestCase):
    def test_all(self):

        p = Problem.readProblem()
        print("Read problem:")
        print(p)
        # Negative control
        self.assertFalse(p.isGoal(p.getInitState().getState()))

        # Positive control
        #p.getInitState().packages = []
        #self.assertTrue(p.isGoal(p.getInitState()))
        print("---* PRINTING SUCCESSORS OF INITIAL STATE *-----")
        states = [p.getInitState()]
        for i in range(6):
            print("---Successors: ", len(states))
            for s in states:
                print(s)
            states = p.successors(states[0].getState())
            print("----------------------------------------------------------")

if __name__ == '__main__':
    unittest.main()
