import random

class Sudoku:
    def __init__(self, size=9):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
        self.generate_puzzle()
    
    def generate_puzzle(self):
        self.fill_grid()
        self.remove_numbers()
    
    def fill_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 0:
                    num = random.randint(1, 9)
                    if self.is_safe(num, i, j):
                        self.grid[i][j] = num
                        if self.fill_grid():
                            return True
                        self.grid[i][j] = 0
        return False

    def remove_numbers(self):
        # Randomly remove numbers to create the puzzle
        for _ in range(random.randint(40, 60)):
            x, y = random.randint(0, 8), random.randint(0, 8)
            while self.grid[x][y] == 0:
                x, y = random.randint(0, 8), random.randint(0, 8)
            self.grid[x][y] = 0

    def is_safe(self, num, row, col):
        for x in range(9):
            if self.grid[row][x] == num or self.grid[x][col] == num:
                return False
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
        return True
    
    def display_grid(self):
        for row in self.grid:
            print(' '.join(str(num) if num != 0 else '.' for num in row))
    
    def play(self):
        while True:
            self.display_grid()
            print("Enter your move in the format 'row col value' (or 'exit' to quit):")
            move = input().strip()
            if move.lower() == 'exit':
                break
            
            try:
                row, col, value = map(int, move.split())
                if 0 <= row < 9 and 0 <= col < 9 and 1 <= value <= 9:
                    if self.grid[row][col] == 0:
                        if self.is_safe(value, row, col):
                            self.grid[row][col] = value
                        else:
                            print("This move is not safe.")
                    else:
                        print("Cell is already filled.")
                else:
                    print("Invalid input. Please enter valid row, column, and value.")
            except ValueError:
                print("Invalid input format. Please try again.")

if __name__ == "__main__":
    game = Sudoku()
    game.play()
