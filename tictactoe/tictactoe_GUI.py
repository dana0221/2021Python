import tkinter
from tkinter import messagebox

from tictactoe_gameengine import TictactoeGameEngine

class TictactoeGUI:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()
        self.init_GUI()

    def init_GUI(self):
        self.CANVAS_SIZE = 300
        self.root = tkinter.Tk()
        self.root.title('틱택토')
        self.root.geometry(f'{self.CANVAS_SIZE}x{self.CANVAS_SIZE}')
        self.root.resizable(width=False, height=False)

        self.canvas = tkinter.Canvas(self.root, bg='white', width=self.CANVAS_SIZE, height=self.CANVAS_SIZE)
        self.canvas.pack()

        self.images = {}
        self.images['X'] = tkinter.PhotoImage(file='X.gif')
        self.images['O'] = tkinter.PhotoImage(file='O.gif')

        self.canvas.bind('<Button-1>', self.click_handler)

        self.root.mainloop()

    def click_handler(self, event):
        row, col = self.coordinate_to_position(event.x, event.y)

        # set row, cal
        self.game_engine.set(col, row)

        # set winner
        winner = self.game_engine.set_winner()
        self.draw_board()

        # 승자가 있거나 무승부이면, 게임 끝, 결과표시
        if winner == 'O' or winner == 'X':
            messagebox.showinfo('GameOver', f'{winner} 승리🎉')

            self.root.quit()
        elif winner == 'd':
            messagebox.showinfo('GameOver', '무승부✨')
            self.root.quit()

        # change_trun
        print(f'{event.x}, {event.y}')
        self.game_engine.change_turn()

    def draw_board(self):
        TILE_SIZE = self.CANVAS_SIZE // self.game_engine.SIZE
        x = 0
        y = 0

        for i, v in enumerate(self.game_engine.board):
            if v == '.':
                pass
            else:   # elif v == 'X' or v == 'O'
                self.canvas.create_image(x, y, anchor='nw', image=self.images[v])

            x += TILE_SIZE

            if i % self.game_engine.SIZE == self.game_engine.SIZE - 1:
                x = 0
                y += TILE_SIZE

    def coordinate_to_position(self, x, y):
        col = x // (self.CANVAS_SIZE // self.game_engine.SIZE) + 1
        row = y // (self.CANVAS_SIZE // self.game_engine.SIZE) + 1
        return col, row


if __name__ == '__main__':
    ttt_GUI = TictactoeGUI()