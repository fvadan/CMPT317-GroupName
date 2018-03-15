# Assignment 2

## The Dragon Queen
The Dragon Queen is a game played on a board with 5 columns and 5 rows. One 
player (Player 1) controls the Queen, who has three Dragon protectors.  The 
other player (Player 2) controls 5 wights (a.k.a zombies).  

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

Authors: Tayab Soomro, Mahmud Azam, Flaviu Vadan

Language used:
	- Python
	
Package dependencies:
	- math
	- sys
	- time
	- matplotlib.pyplot (2.1.2)
	- random

The implementation of the Dragon Queen Problem may be run in the following ways:
	1. python3 main.py 
		- Parameters:
			- --cache = use transposition tables
			- -dn = use search depth <n> for AI
			- --print-boards = print the board after each ply 

When the program is run, the following text appears:

---------- Options ----------
 	W -> Wights
	D -> Dragons
	AI -> all AI
	STATS -> statistics

W - human plays as wights
D - human plays as dragons
AI - run an AI vs. AI game
STATS - gather and print statistics of the gameplay with depths up to maximum
	depth as specified on the command line (after STATS is selected)

Instruction for moving pieces:
	- when asked for a move, specify: 
		D0 2 1 
		- move D0 (Dragon 0) to row 2 column 1 where indices start at 0 
		QQ 3 4
		- move QQ (the Queen) to row 3 column 4 where indices start at 0

		
