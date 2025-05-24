class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
    
    def display_board(self):
        """Display the current board state"""
        print("\n   |   |   ")
        print(f" {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} ")
        print("___|___|___")
        print("   |   |   ")
        print(f" {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} ")
        print("___|___|___")
        print("   |   |   ")
        print(f" {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} ")
        print("   |   |   ")
        print()
    
    def display_positions(self):
        """Show position numbers for reference"""
        print("Position numbers for reference:")
        print("\n   |   |   ")
        print(" 1 | 2 | 3 ")
        print("___|___|___")
        print("   |   |   ")
        print(" 4 | 5 | 6 ")
        print("___|___|___")
        print("   |   |   ")
        print(" 7 | 8 | 9 ")
        print("   |   |   ")
        print()
    
    def make_move(self, position):
        """Make a move at the specified position (1-9)"""
        if position < 1 or position > 9:
            return False
        
        # Convert position to row, col coordinates
        row = (position - 1) // 3
        col = (position - 1) % 3
        
        # Check if position is already taken
        if self.board[row][col] != ' ':
            return False
        
        # Make the move
        self.board[row][col] = self.current_player
        return True
    
    def check_winner(self):
        """Check if there's a winner"""
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        return None
    
    def is_board_full(self):
        """Check if the board is full"""
        for row in self.board:
            if ' ' in row:
                return False
        return True
    
    def switch_player(self):
        """Switch between X and O"""
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def reset_game(self):
        """Reset the game board"""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
    
    def play(self):
        """Main game loop"""
        print("=" * 40)
        print("🎮 Welcome to Tic-Tac-Toe! 🎮")
        print("=" * 40)
        print("Player 1: X")
        print("Player 2: O")
        print()
        
        while True:
            self.display_positions()
            self.display_board()
            
            # Get player input
            try:
                print(f"Player {self.current_player}'s turn!")
                position = int(input("Enter position (1-9): "))
                
                # Try to make the move
                if not self.make_move(position):
                    print("❌ Invalid move! Position already taken or out of range.")
                    print("Please try again.\n")
                    continue
                
                # Check for winner
                winner = self.check_winner()
                if winner:
                    self.display_board()
                    print(f"🎉 Congratulations! Player {winner} wins! 🎉")
                    break
                
                # Check for tie
                if self.is_board_full():
                    self.display_board()
                    print("🤝 It's a tie! Good game!")
                    break
                
                # Switch players
                self.switch_player()
                
            except ValueError:
                print("❌ Please enter a valid number between 1-9.\n")
                continue
            except KeyboardInterrupt:
                print("\n\n👋 Thanks for playing!")
                break
        
        # Ask if players want to play again
        self.play_again()
    
    def play_again(self):
        """Ask if players want to play again"""
        while True:
            try:
                choice = input("\n🔄 Do you want to play again? (y/n): ").lower().strip()
                if choice in ['y', 'yes']:
                    self.reset_game()
                    self.play()
                    break
                elif choice in ['n', 'no']:
                    print("👋 Thanks for playing Tic-Tac-Toe!")
                    break
                else:
                    print("Please enter 'y' for yes or 'n' for no.")
            except KeyboardInterrupt:
                print("\n👋 Thanks for playing!")
                break

def main():
    """Run the tic-tac-toe game"""
    game = TicTacToe()
    game.play()

if __name__ == "__main__":
    main()