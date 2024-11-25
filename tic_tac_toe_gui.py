import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text=' ', font=('normal', 20), height=2, width=4,
                                                command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)
    
    def on_button_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_winner(row, col):
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_full():
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def check_winner(self, row, col):
        player = self.board[row][col]
        # Check row
        if all([cell == player for cell in self.board[row]]):
            return True
        # Check column
        if all([self.board[i][col] == player for i in range(3)]):
            return True
        # Check main diagonal
        if row == col and all([self.board[i][i] == player for i in range(3)]):
            return True
        # Check anti-diagonal
        if row + col == 2 and all([self.board[i][2 - i] == player for i in range(3)]):
            return True
        return False
    
    def is_full(self):
        return all([cell != ' ' for row in self.board for cell in row])
    
    def reset_board(self):
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
