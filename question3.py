3x3 Number Slide Puzzle

Write a Python program for a 3x3 sliding number puzzle using a class.

The puzzle uses numbers 1 through 8 and one blank space.

The board should start solved, then be scrambled by making random legal moves.

Important note: A sliding puzzle can be impossible to solve if you start with a random board arrangement. To avoid that, start with the solved board and scramble it by calling the slide function with random inputs. This guarantees the scrambled board came from legal moves.

Starter Code:

import random
 
 
class SlidePuzzle:
    def __init__(self):
        self.board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, "_"]
        ]
 
    def print_board(self):
        # TODO: print the board in a readable way
        pass
 
    def slide(self, direction):
        # TODO: move the blank using w/a/s/d if possible
        # w = up, a = left, s = down, d = right
        pass
 
    def scramble(self, moves):
        # TODO: call slide with random directions many times
        pass
 
    def is_solved(self):
        return self.board == [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, "_"]
        ]
 
 
def main():
    puzzle = SlidePuzzle()
    puzzle.scramble(100)
 
    print("Sliding Puzzle")
    print("Use w/a/s/d to move the blank space.")
    print("Type quit to exit.")
 
    # TODO: game loop
 
 
main()
Requirements:

Complete the starter code.
Use the SlidePuzzle class.
Store a 3x3 board.
Use w, a, s, and d for movement.
Let the user type quit to stop.
Detect when the puzzle is solved.
Handle invalid input gracefully.
