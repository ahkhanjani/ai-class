import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        # پنجره بازی
        self.window = tk.Tk()
        self.window.title("TicTacToe")

        # صفحه بازی
        self.board = [' ']*9

        # کامپیوتر با O بازی می‌کند
        self.current_player = 'O'

        # مربع جادویی
        self.magic_square = [8, 1, 6, 3, 5, 7, 4, 9, 2]

        # ساخت دکمه‌های صفحه بازی
        self.buttons = [self.create_button(i) for i in range(9)]

        # کامپیوتر حرکت می‌کند
        self.computer_move()

    def create_button(self, i):
        button = tk.Button(self.window, text=' ',
                           command=lambda: self.click(i), height=3, width=6)

        button.grid(row=i//3, column=i % 3)

        return button

    # کلیک کاربر

    def click(self, i):
        if self.board[i] == ' ':
            self.board[i] = 'X'
            self.buttons[i]['text'] = 'X'

            if self.check_win('X'):
                self.gameover("شما بردید!")
            else:
                self.computer_move()

    # حرکت کامپیوتر با روش مربع جادویی

    def computer_move(self):
        # بررسی حالات برد
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                if self.check_win('O'):
                    self.buttons[i]['text'] = 'O'
                    self.gameover("شما باختید!")
                    return
                # اگر برنده نیست، برگرد
                self.board[i] = ' '

        # اگر حالتی برای برد نیست، از مربع جادویی استفاده کن
        scores = []
        for i in range(9):
            if self.board[i] == ' ':
                scores.append(self.magic_square[i])
            else:
                scores.append(0)

        move = scores.index(max(scores))

        self.board[move] = 'O'
        self.buttons[move]['text'] = 'O'

        if self.check_win('O'):
            self.gameover("شما باختید!")
        elif ' ' not in self.board:
            self.gameover("تساوی!")

    # بررسی برد یک طرف
    def check_win(self, player):
        # لیست حالات برد
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

        for condition in win_conditions:
            i, j, k = condition

            if self.board[i] == self.board[j] == self.board[k] == player:
                return True

        return False

    def gameover(self, message):
        messagebox.showinfo("پایان بازی", message)
        self.window.quit()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    TicTacToe().run()
