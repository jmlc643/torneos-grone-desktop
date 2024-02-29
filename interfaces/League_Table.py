import tkinter as tk
from tkinter import ttk

from PlayerDAO import PlayerDAO


class LeagueTable(tk.Tk):

    def __init__(self):
        super().__init__()
        self.configure_windows()
        self.grid()
        self.colocate_title()
        self.create_table()
        self.get_data()
        self.colocate_buttons()

    def configure_windows(self):
        self.title("Torneos")
        self.geometry("900x600")
        self.configure(background="#1d2d44")
        self.resizable(False, False)
        self.styles = ttk.Style(self)
        self.styles.theme_use('clam')
        self.styles.configure(self, background='#1d2d44', foreground='white', fieldbackground='black')

    def colocate_title(self):
        title = ttk.Frame(self)
        title.grid(row = 0, column = 1)
        self.text = ttk.Label(title, text = "Summer Grone League Table", font = ("Arial", 36))
        self.text.grid(row = 0, column = 0, pady = 50)

    def create_table(self):
        self.styles.configure("Treeview", background="black", foreground="white", fieldbackground="black", rowheight=30)
        table = ttk.Frame(self)
        table.grid(row=1, column=1, padx = 100)
        # Definimos las columnas
        self.columns = ('Puesto', 'Username', 'Points', 'Percent For', 'Percent Against', 'Won', 'Drawn', 'Lost', 'Percent Difference')
        self.table = ttk.Treeview(table, columns=self.columns, show='headings')
        # Encabezados
        self.table.heading('Puesto', text='N°   ', anchor=tk.CENTER)
        self.table.heading('Username', text='Username', anchor=tk.CENTER)
        self.table.heading('Points', text='Pts', anchor=tk.CENTER)
        self.table.heading('Percent For', text='PF', anchor=tk.CENTER)
        self.table.heading('Percent Against', text='PA', anchor=tk.CENTER)
        self.table.heading('Won', text='Won', anchor=tk.CENTER)
        self.table.heading('Drawn', text='Drawn', anchor=tk.CENTER)
        self.table.heading('Lost', text='Lost', anchor=tk.CENTER)
        self.table.heading('Percent Difference', text='Diff', anchor=tk.CENTER)
        # Formato a las columnas
        self.table.column('Puesto', width=60, anchor=tk.CENTER)
        self.table.column('Username', width=120, anchor=tk.CENTER)
        self.table.column('Points', width=60, anchor=tk.CENTER)
        self.table.column('Percent For', width=60, anchor=tk.CENTER)
        self.table.column('Percent Against', width=60, anchor=tk.CENTER)
        self.table.column('Won', width=60, anchor=tk.CENTER)
        self.table.column('Drawn', width=60, anchor=tk.CENTER)
        self.table.column('Lost', width=60, anchor=tk.CENTER)
        self.table.column('Percent Difference', width=60, anchor=tk.CENTER)
        self.table.grid(row=0, column=0)
        # Agregar un scrollbar
        scrollbar = ttk.Scrollbar(table, orient=tk.VERTICAL, command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

    def get_data(self):
        # Cargar datos a la self
        data = PlayerDAO.select()
        i = 1
        for player in data:
            self.table.insert(parent='', index=tk.END,
                              values=(i, player.username, player.points, player.percent_for, player.percent_against, player.won, player.drawn, player.lost, player.percent_difference))
            i += 1

    def colocate_buttons(self):
        buttons = ttk.Frame(self)
        buttons.grid(column=1, row=2, pady = 20)
        self.button_back = ttk.Button(buttons, text = "Back")
        self.button_back.grid(column = 0, row = 0)
        self.button_back.bind("<Button-1>", self.back)

    def back(self, event):
        self.destroy()
        from interfaces.App import App
        app = App()
        app.mainloop()

    def grid(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

if __name__ == "__main__":
    app = LeagueTable()
    app.mainloop()