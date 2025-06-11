import tkinter as tk

def set_title(r, c):
    global curr_player, game_over
    if game_over or board[r][c]["text"]: return
    board[r][c]["text"] = curr_player
    curr_player = "X" if curr_player == "O" else "O"
    label["text"] = curr_player + "'s turn"
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1
    lines = [[(i, j) for j in range(3)] for i in range(3)] + [[(i, j) for i in range(3)] for j in range(3)]
    lines += [[(i, i) for i in range(3)], [(i, 2-i) for i in range(3)]]
    for line in lines:
        a, b, c = line
        if board[a[0]][a[1]]["text"] == board[b[0]][b[1]]["text"] == board[c[0]][c[1]]["text"] != "":
            w = board[a[0]][a[1]]["text"]
            label.config(text=w + " is the winner!", fg=yellow)
            for x, y in line:
                board[x][y].config(fg=yellow, bg=light_gray)
            game_over = True
            return
    if turns == 9:
        label.config(text="Tie", fg=yellow)
        game_over = True

def new_game():
    global turns, game_over
    turns, game_over = 0, False
    label.config(text=curr_player + "'s turn", fg="white")
    for row in board:
        for cell in row:
            cell.config(text="", fg=blue, bg=gray)

# Setup
curr_player = "X"
board = [[None]*3 for _ in range(3)]
blue, yellow, gray, light_gray = "#4584b6", "#ffde57", "#343434", "#646464"
turns = 0
game_over = False

w = tk.Tk()
w.title("Tic Tac Toe")
w.resizable(False, False)
f = tk.Frame(w)
label = tk.Label(f, text="X's turn", font=("Consolas", 20), bg=gray, fg="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

for r in range(3):
    for c in range(3):
        board[r][c] = tk.Button(f, text="", font=("Consolas", 50), bg=gray, fg=blue, width=4, height=1,
                                command=lambda c=c, r=r: set_title(r, c))
        board[r][c].grid(row=r+1, column=c)

tk.Button(f, text="restart", font=("Consolas", 20), bg=gray, fg=gray, command=new_game)\
    .grid(row=4, column=0, columnspan=3, sticky="we")

f.pack()
w.update()
w.geometry(f"{w.winfo_width()}x{w.winfo_height()}+{(w.winfo_screenwidth()-w.winfo_width())//2}+{(w.winfo_screenheight()-w.winfo_height())//2}")
w.mainloop()
