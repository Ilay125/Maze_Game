# The Maze Gaem

**A maze game based on a maze generator that
uses the recursive backtracking algorithm.**<br>Made for the Timathon - Code Jam competition
by @iLay#1272 && @I live on saturn#6795.


## Requirements
**You need to have python 3.7+ and pygame** to be able to run the game.

To download python 3.7: https://www.python.org/downloads/release/python-379/

To download pygame in windows 10:
* Open the cmd.
* Go to your python folder (using the `cd` command).
* Go to Scripts folder.
* Type: `pip install pygame`

## The Game
The game is called: **"Gaem.py"**

To move, use the WASD keys of the arrow keys.

When you open the game you'll have two buttons:

_Start_ - will start the main game.<br>
_Custom_ - will let you create your own maze.

**Above 150x150 starts to be really heavy on the pc -
the game might crash.**

The goal of the game is to press all of the buttons
and go to the trapdoor under the time limit.

**Difficulty names:**

* _Easy_ - Eww what a BABY
* _Medium_ - Ehh.. average
* _Hard_ - MY PP
* _Ultimate_ - EPIK GAMER

## Test files
If you wish to see the way that the algorithm works, you
should check out the files in the test folder.

**However,** you need to extract the files from the folder to the main folder (Where the game file is).

## Test.py
The main test file is called: `Test.py` in the Tests folder.<br>
The test file shows how the algorithm works and that's how we tested it.<br>

If you wish to see the info feature, **don't** choose a maze above 15x15.

you can set the speed of the creation using the left/right arrow keys.
and Enter to get into the data analysis mode. In the data analysis mode, use the up arrow key to move a single frame.

**Color indicators:**
* _Cyan_ - starting point.
* _Orange_ - ending point.
* _Magenta_ - current cell.
* _Yellow_ - way cell (You need to understand how recursive backtracking works).
* _Gray_ - dead-end cell.
* _Red wall_ - wall that will be removed after the algorithm finishes.
