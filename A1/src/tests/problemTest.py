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
        self.assertFalse(p.isGoal(p.getCurrentState()))

        # Positive control
        #p.getCurrentState().packages = []
        #self.assertTrue(p.isGoal(p.getCurrentState()))
        print("---* PRINTING SUCCESSORS OF INITIAL STATE *-----")
        state = [p.getCurrentState()]
        for i in range(4):
            print(state[0])
            state = p.successors(state[0])

if __name__ == '__main__':
    unittest.main()
