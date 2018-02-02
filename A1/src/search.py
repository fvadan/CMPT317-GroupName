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
            if p.isGoal(curr.getState()):
                return curr.traceBack()
            else:
                succ = p.successors(curr)
                for s in succ:
                    q.enqueue(s)
        return []


if __name__ == '__main__':
    p = Problem.readProblem()
    for i in Search.search(p):
        print(i)
