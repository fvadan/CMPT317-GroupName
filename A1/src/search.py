from stateQueue import StateQueue
from problem import Problem

class Search():
    """
        Class deals with the search functionality.
    """

    def search(problem):
        """
            Search algorithm
            :param initialState: the initial state that is passed to the algorithm.
        """
        q = StateQueue()
        q.enqueue(problem.getInitState())
        while q.isEmpty() is False:
            curr = q.dequeue()
            print(curr.getState())
            if p.isGoal(curr.getState()):
                return curr.traceBack()
            else:
                succ = p.successors(curr.getState())
                for s in succ:
                    q.enqueue(s)
        print("NOT FOUND")
        return []


if __name__ == '__main__':
    p = Problem.readProblem()
    for i in Search.search(p):
        print(i)
