# 3x3 Number Slide Puzzle
# A.I Disclaimer: Some, I used A.I to fix syntax errors
import random


class SlidePuzzle:
    def __init__(self):
        self.board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, "_"]
        ]

    def print_board(self):
        for row in self.board:
            print(" ".join(str(item) for item in row))
        print()

    def find_blank(self):
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == "_":
                    return r, c

    def slide(self, direction):
        row, col = self.find_blank()

        new_row, new_col = row, col

        if direction == "w":      
            new_row -= 1
        elif direction == "s":    
            new_row += 1
        elif direction == "a":    
            new_col -= 1
        elif direction == "d":    
            new_col += 1
        else:
            return False

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            self.board[row][col], self.board[new_row][new_col] = (
                self.board[new_row][new_col],
                self.board[row][col]
            )
            return True

        return False

    def scramble(self, moves):
        directions = ["w", "a", "s", "d"]

        for _ in range(moves):
            direction = random.choice(directions)
            self.slide(direction)

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
    print("Type quit to exit.\n")

    while True:
        puzzle.print_board()

        if puzzle.is_solved():
            print("Congratulations! You solved the puzzle!")
            break

        move = input("Enter move: ").lower()

        if move == "quit":
            print("Thanks for playing!")
            break

        if move not in ["w", "a", "s", "d"]:
            print("Invalid input. Use w, a, s, d, or quit.\n")
            continue

        if not puzzle.slide(move):
            print("That move is not possible.\n")
main()