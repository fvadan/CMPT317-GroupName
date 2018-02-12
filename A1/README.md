# Assignment 1

Authors: Tayab Soomro, Mahmud Azam, Flaviu Vadan

The M-N-K-Y Problem

Language used: 
	- Python

Package dependencies: 
	- queue
	- heapq	
	- sys
	- copy
	- matplotlib.pyplot
	- random
	- time

The implementation of the MNKY problem may be run in three different ways:

1. Open Terminal and use ./runall.sh
	- this will invoke the search.py file on all the test cases that are hard
	  coded in the test_cases folder. It will iterate over them but not run
	  BFS on 3422. 
2. Open Terminal and use python3 [options] < [input file]
	- here, options may be:  --run-bfs (runs BFS on all test cases);
				 --print-plan (prints the trace of the algorithm).
    Example:
    python3 search.py --run-bfs --print-plan < ../tests/test_cases/2422.txt

    The input format is:
    M
    N
    K
    Y
    P11 P12 ... P1Y D11 D12 ... D1Y
    .
    .
    .
    PN1 PN2 ... PNY DN1 DN2 ... DNY

    Where PAB is the B-th entry of Package A's pickup location vector
    and DAB is the B-th entry of Package A's delivery location vector

3. Open Terminal and use python3 randomProblemGenerator.py
	- this will run random test cases (the same ones as reported) and print
	  performance graphs of the algorithms (the same ones as reported).

