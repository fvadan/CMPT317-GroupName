# Assignment 2

## The Dragon Queen
The Dragon Queen is a game played on a board with 5 columns and 5 rows. One player (Player 1) controls the Queen, who has three Dragon protectors.  The other player (Player 2) controls 5 wights (a.k.a zombies).  (This game, as far as I know, is a completely unique invention; I don't think you'll find anything quite like it anywhere, which is the whole point).  

The Dragon Queen could be a Mad King, with a King's Guard.  Or the Wights could be Daleks.  Or the Wights could be Sith-Lords, with the Queen as a Fleeing Senator, guarded by Jedi Protectors.  

### Initial Position

The initial position is as follows.

```
. . Q . .
. D D D .
. . . . .
. . . . .
W W W W W
```

Traditionally, the Wights move first (Player 2).
End of Game

Win for Player 1: the Queen reaches the Wight's home row (the bottom of the board in the above diagram).  
Win for Player 2: the Queen is captured.  
Draw:
One player cannot move.
No win for either player after 50 ply (25 complete turns).
Movement of pieces:

Wights can move forward, backward, left, or right, by one square if it is not occupied, but not diagonally.  
(wights' movement is somewhat similar to pawns in Chess)
The Queen and the Dragons can move to any adjacent empty square, vertically, horizontally, or diagonally.  
(the Queen's and the dragons' movement is similar to the king in Chess)
Capture:

A Wight can capture by moving diagonally (in any diagonal direction) into the square occupied by an opposing piece (a Dragon or the Queen).  
(wights' capture is somewhat similar to pawns in chess)
A Dragon or the Queen can capture by normal movement into a square occupied by a Wight.  
(Dragons' and Queen's capture is similar to the king in Chess)
Capture is not forced.
Other rules:

A player must move if a move is possible.
Written Document Requirements
You will submit a written document addressing the following points.

### Identification
- Your name, and student number and NSID.
- The names of everyone in your group.
- An assessment of the balance of effort among your group members.
- Who did what, generally?
- Was the balance even, more or less?

### Implementation:
- Describe how you represented the game state.
  Objects, classes, structs, etc..
- Data stored, assumptions made
- Describe your heuristic evaluation function.
- What are you doing to assess the state of the game?
- Give some examples.

### Results:
Describe the performance of your implementation in terms of:
- Wins/losses vs humans, or vs itself, or other implementations.
- search nodes created/expanded,
- depth of search in the game tree,
- time to find moves,
- memory used (perhaps the maximum size of your Queue).

If you had slightly different implementations for some of these, explain the differences, and give results as appropriate.

Compare your results using MiniMax (only) and MiniMax (with alpha-beta pruning).
search nodes, depth of search, time to find moves, memory used, etc.

### Discussion:
Assess the quality of your results.
Just be fair; results don't have to be good.
- What is the limiting factor for your implementation?
- Assess short-comings, strengths.
Other comments:
- Did something in this task surprise you?
- Did you have any good ideas you didn't have time to implement?
- Anything else?

### Implementation Submission Requirements.
Your zip file will be submitted by every member of your group.  It will contain:
- All the source code
- A README file containing a description of how to get your implementation to run, including:
- language used
- package dependencies
- compile instructions (if appropriate; a shell script or makefile would be better)
- how to run your implementation

### Grading:
**3 marks: Indentification**
- Complete / Incomplete
- If group members report strikingly imbalanced workload, we will look into the situation immediately, and perhaps apply an adjustment to A1 total grade before April submission of grades.  Your Moodle grade will not reflect any such adjustment.  If you worked solo, a slight adjustment to your grade may be applied in your favour.

**21 marks: Implementation Description**
- 9 marks: The state representation,
- 9 marks: The heuristic evaluation function?
- 3 marks: presentation was good, fairly good grammar, clarity, etc.

**24 marks: Results Description**
- 12 marks: Your results looked at depth of search, nodes searched, time, space.
- 9 marks: Your results compares Minimax (alone) against Minimax (with alpha-beta pruning).
- 3 marks: presentation was good, fairly good grammar, clarity, etc.

**9 marks: Discussion**
- 3 marks: You discussed the quality of play.
- 3 marks: You discussed the effectiveness of your evaluation function.
- 3 marks: presentation was good, fairly good grammar, clarity, etc.

**3 marks: Implementation Quality**

- Is the code reasonably well documented?
- Does the implementation seem to do anything weird or unhealthy?
- Does it look like your code do what your description says?
