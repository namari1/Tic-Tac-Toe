from tkinter import *

BACKGROUND_COLOR = "#2A2F4F"
FONT_COLOR = "#FDE2F3"
GRID_COLOR = "#917FB3"
WINNING_COMBOS = [
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],

    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],

    [(0, 0), (1, 1), (2, 2)],
    [(2, 0), (1, 1), (0, 2)],
]


class TicTacToe(Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.config(padx=25, pady=20, bg=BACKGROUND_COLOR)
        self.cells = {}
        self.current_player = ""
        self.round = 0
        self.moves_made = []
        self.x_moves = []
        self.o_moves = []
        self.game_over = False
        self.frame = Frame(master=self, bg=BACKGROUND_COLOR)
        self.frame.pack(fill=X)
        self.display = Label(master=self.frame, fg=FONT_COLOR, bg=BACKGROUND_COLOR, highlightthickness=0,
                             text="Tic-Tac-Toe",
                             font=("Modern No. 20", 30, "normal"))
        self.display.pack()
        self.make_board()

    def make_board(self):
        grid = Frame(master=self, bg=GRID_COLOR, padx=5, pady=5)
        grid.pack()
        for row in range(3):
            for column in range(3):
                button = Button(master=grid, text="", font=("Arial", 40, "bold"), bg=BACKGROUND_COLOR)
                button.config(height=1, width=3)
                button.grid(row=row, column=column, sticky="EW", padx=5, pady=5)
                self.cells[button] = (row, column)
                button.bind("<ButtonPress-1>", self.play)

    def play(self, button):
        button_pressed = button.widget
        if button_pressed not in self.moves_made and not self.game_over:
            move = self.cells[button_pressed]
            self.moves_made.append(button_pressed)
            if self.round == 8:
                self.display.config(text="It's a draw!")
            elif self.round % 2 == 0:
                self.current_player = "X"
                self.x_moves.append(move)
                if self.check_combo(self.x_moves):
                    self.display.config(text="X Wins!")
                    self.game_over = True
            else:
                self.current_player = "O"
                self.o_moves.append(move)
                if self.check_combo(self.o_moves):
                    self.display.config(text="O Wins!")
                    self.game_over = True
            button_pressed.config(text=self.current_player, fg=FONT_COLOR)
            self.round += 1

    def check_combo(self, moves):
        for combo in WINNING_COMBOS:
            check = all(item in moves for item in combo)
            if check:
                return True
