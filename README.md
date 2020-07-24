# Puzzle-Solver
Solver for a circle puzzle

The circle puzzle has 4 concentric circles in total, with each circle contains 12 spaces. The puzzle is regarded as solved if all objects on the board either lineup into a straight line on the circles or they form a "square" near the center.

You are allowed to either rotate one of the circle or choose a straight line in the board and shift it. You may usually only able to perform at most 3 movement.

This solver will output an instruction on how to solve on this circle puzzle.

You have to gives the initial position of the objects and how much movement is allowed. which you have to gives the board as input and the number of movement via main() function.

The board is encoded as a 12x4 matrix, started from the line at 5.5 o'clock direction and go anticlockwise. 1 if there is an object in the corresponding tile and 0 if it is an empty space.

This solver went on a brute-force approach which it simply try to check all possible movement and find a movement that can solve the puzzle, so it can be time consuming sometimes.
