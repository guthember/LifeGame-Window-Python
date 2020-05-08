import tkinter as tk
from Live import Live

class LiveSpace(tk.Canvas):
    def __init__(self, size):
        self.size = size
        super().__init__(width=self.size, height=self.size, bg='white', highlightthickness=0)

SIZE = 200

live = Live('adatok.txt')

COUNT = live.size

def draw():
    itemWH = SIZE / COUNT
    for x in range(0, COUNT):
        for y in range(0, COUNT):
            startX = x * itemWH
            startY = y * itemWH
            color = '#000000' if live.liveItems[x][y] == 1 else '#ffffff'
            board.create_rectangle(startY, startX, startY + itemWH, startX + itemWH, fill=color)

def key_pressed(event):
    if event.char == ' ':
        live.nextStat()
        draw()
    elif event.char == 'q':
        exit()
    else:
        pass


root = tk.Tk()
root.geometry('200x250')
root.title('Life game')
root.resizable(False, False)
root.bind_all('<Key>', key_pressed)
board = LiveSpace(SIZE)
board.pack()
draw()
tk.mainloop()