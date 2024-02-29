import tkinter as tk
from tkinter import ttk


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.configure_windows()
        self.grid()
        self.colocate_items()

    def configure_windows(self):
        self.title("Torneos")
        self.geometry("900x600")
        self.configure(background="#1d2d44")
        self.styles = ttk.Style(self)
        self.styles.theme_use('clam')
        self.styles.configure(self, background='#1d2d44', foreground='white', fieldbackground='black')

    def colocate_items(self):
        self.styles.configure('TButton', background='#005f73')
        self.styles.map('TButton', background=[('active', '#0a9396')])
        buttons = ttk.Frame(self)
        buttons.grid(row = 1, column = 0)
        self.button1 = ttk.Button(buttons, text="League")
        self.button1.grid(row = 0, column = 0, padx = 20)
        self.button2 = ttk.Button(buttons, text = "Tournament")
        self.button2.grid(row=0, column = 1, padx = 20)
        self.button1.bind("<Button-1>", self.league)

    def league(self, event):
        self.destroy()
        from interfaces.League_Table import LeagueTable
        league = LeagueTable()
        league.mainloop()

    def grid(self):
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(1, weight=1)


if __name__ == "__main__":
    app = App()
    app.mainloop()