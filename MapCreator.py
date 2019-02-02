import tkinter as tk
import os


def mapcreator():
    def export(*args):
        with open(os.getcwd()+"\Maps\%s.txt" % name.get(), "w") as f:
            f.write(str(rows.get())+";"+str(cols.get())+";" +
                    str(board)+";"+str(["....."]*10)+";"+str(["0"]*10))

    def checknr(arg, *args):
        x = 0
        if(str(arg)[-1] == "n"):
            x = 1
        elif(str(arg)[-2] == "n"):
            x = int(str(arg)[-1])
        elif(str(arg)[-3] == "n"):
            x = int(str(arg)[-1])+10*int(str(arg)[-2])
        elif(str(arg)[-4] == "n"):
            x = int(str(arg)[-1])+10*int(str(arg)[-2])+100*int(str(arg)[-3])
        elif(str(arg)[-5] == "n"):
            x = int(str(arg)[-1])+10*int(str(arg)[-2])+100 * \
                int(str(arg)[-3])+1000*int(str(arg)[-4])
        return x

    def change(arg, *args):
        x = checknr(arg)
        if (mode.get() == 1):
            arg.config(bg='blue')  # wall
        elif (mode.get() == 2):
            arg.config(bg='magenta')  # point
        elif (mode.get() == 3):
            arg.config(bg='purple')  # special point
        elif (mode.get() == 4):
            arg.config(bg='red')  # ghost1-blinky
            onboard(mode.get())
        elif (mode.get() == 5):
            arg.config(bg='pink')  # ghost2-pinky
            onboard(mode.get())
        elif (mode.get() == 6):
            arg.config(bg='cyan')  # ghost3-inky
            onboard(mode.get())
        elif (mode.get() == 7):
            arg.config(bg='orange')  # ghost4-clyde
            onboard(mode.get())
        elif (mode.get() == 8):
            arg.config(bg='yellow')  # pacman
            onboard(mode.get())
        board[x-1] = mode.get()

    def onboard(n, *args):
        if n in board:
            tiles[board.index(n)].config(bg='magenta')
            board[board.index(n)] = 2

    def fill(*args):
        for i in range(len(board)):
            if(board[i] == 0):
                board[i] = 2
                tiles[i].config(bg='magenta')

    def sketch(*args):
        global board
        board = [0]*rows.get()*cols.get()
        return board

    def draw(*args):
        sketch()
        global tiles
        global buttons
        try:
            clear()
        except:
            pass
        buttons = tk.Frame(frame)
        buttons.grid(column=10, row=3)
        tiles = [0]*rows.get()*cols.get()
        while (str(rows.get())[0] == 0):
            rows.set(str(rows.get()[1:]))
        while (str(cols.get())[0] == 0):
            cols.set(str(cols.get()[1:]))
        for row in range(rows.get()):
            for col in range(cols.get()):
                if(row == 0 or col == 0 or
                   row == rows.get()-1 or col == cols.get()-1):
                    tiles[col+(cols.get())*row] = (
                        tk.Button(buttons, image=pixel, bg='blue')
                    )
                    tiles[col+(cols.get())*row].config(command=(
                        lambda arg=tiles[col+(cols.get())*row]: change(arg)))
                    tiles[col+(cols.get())*row].grid(column=col, row=row)
                    board[col+(cols.get())*row] = 1
                else:
                    tiles[col+(cols.get())*row] = (
                        tk.Button(buttons, image=pixel, bg='white')
                    )
                    tiles[col+(cols.get())*row].config(command=(
                        lambda arg=tiles[col+(cols.get())*row]: change(arg)))
                    tiles[col+(cols.get())*row].grid(column=col, row=row)

    def change_mode(n, *args):
        if n == 1:
            mode.set(1)
        elif n == 2:
            mode.set(2)
        elif n == 3:
            mode.set(3)
        elif n == 4:
            mode.set(4)
        elif n == 5:
            mode.set(5)
        elif n == 6:
            mode.set(6)
        elif n == 7:
            mode.set(7)
        elif n == 8:
            mode.set(8)
        elif n == 8:
            mode.set(9)

    def clear(*args):
        for i in range(len(tiles)-1, -1, -1):
            tiles[i].destroy()
        buttons.delete()
    top = tk.Tk()
    pixel = tk.PhotoImage(width=8, height=8)
    top.title("Map creator for PacMan")
    frame = tk.Frame(top)
    frame.grid(column=0, row=0)
    rows = tk.IntVar(frame)
    rows.set(20)
    cols = tk.IntVar(frame)
    cols.set(20)
    mode = tk.IntVar(frame)
    name = tk.StringVar(frame)
    name.set("levelname")
    mode.set(1)

    l_size = tk.Label(frame, text="Map size: ")
    l_size.grid(column=1, row=1)

    l_size = tk.Label(frame, text="x")
    l_size.grid(column=3, row=1)

    e_rows = tk.Entry(frame, width=8, textvariable=rows)
    e_rows.grid(column=2, row=1)

    e_cols = tk.Entry(frame, width=8, textvariable=cols)
    e_cols.grid(column=4, row=1)

    b_draw = tk.Button(frame, text="draw", command=draw)
    b_draw.grid(column=5, row=1)

    b_save = tk.Button(frame, text="save", command=export)
    b_save.grid(column=6, row=1)

    b_wall = tk.Button(frame, text="wall", bg='blue',
                       command=lambda: change_mode(1))
    b_wall.grid(column=2, row=2)

    b_point = tk.Button(frame, text="point", bg='magenta',
                        command=lambda: change_mode(2))
    b_point.grid(column=3, row=2)

    b_powerup = tk.Button(frame, text="special", bg='purple',
                          command=lambda: change_mode(3))
    b_powerup.grid(column=4, row=2)

    b_ghost1 = tk.Button(frame, text="blinky", bg='red',
                         command=lambda: change_mode(4))
    b_ghost1.grid(column=5, row=2)

    b_ghost2 = tk.Button(frame, text="pinky", bg='pink',
                         command=lambda: change_mode(5))
    b_ghost2.grid(column=6, row=2)

    b_ghost3 = tk.Button(frame, text="inky", bg='cyan',
                         command=lambda: change_mode(6))
    b_ghost3.grid(column=7, row=2)

    b_ghost4 = tk.Button(frame, text="clyde", bg='orange',
                         command=lambda: change_mode(7))
    b_ghost4.grid(column=8, row=2)

    b_pacman = tk.Button(frame, text="pacman", bg='yellow',
                         command=lambda: change_mode(8))
    b_pacman.grid(column=8, row=1)

    b_fill = tk.Button(frame, text="fill", bg='magenta', command=fill)
    b_fill.grid(column=7, row=1)

    e_name = tk.Entry(frame, text=name, textvariable=name)
    e_name.grid(column=1, row=2)

    top.mainloop()


if __name__ == "__main__":
    mapcreator()
