class TicTacToe:
    def __init__(self, size):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.current_player = 'X'
    
    def display_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.size * 2 - 1))
    
    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False
    
    def check_winner(self):
        # Check rows and columns
        for i in range(self.size):
            if all(self.board[i][j] == self.current_player for j in range(self.size)) or \
               all(self.board[j][i] == self.current_player for j in range(self.size)):
                return True
        
        # Check diagonals
        if all(self.board[i][i] == self.current_player for i in range(self.size)) or \
           all(self.board[i][self.size - 1 - i] == self.current_player for i in range(self.size)):
            return True
        
        return False
    
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def is_draw(self):
        return all(self.board[row][col] != ' ' for row in range(self.size) for col in range(self.size))

    def play(self):
        while True:
            self.display_board()
            print(f"Player {self.current_player}, enter your move (row and column): ")
            row, col = map(int, input().split())
            if row < 0 or row >= self.size or col < 0 or col >= self.size:
                print("Invalid move. Try again.")
                continue
            
            if not self.make_move(row, col):
                print("Cell is already taken. Try again.")
                continue
            
            if self.check_winner():
                self.display_board()
                print(f"Player {self.current_player} wins!")
                break
            
            if self.is_draw():
                self.display_board()
                print("The game is a draw!")
                break
            
            self.switch_player()

if __name__ == "__main__":
    size = int(input("Enter the size of the Tic Tac Toe board (e.g., 3 for 3x3): "))
    game = TicTacToe(size)
    game.play()
