import tkinter as tk
import datetime
from ttkbootstrap.dialogs import Messagebox as show
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
# import database as db


class HomePage(ttk.Frame):
    def __init__(self, controller, parent): 
        super().__init__(parent, width = 500, height = 700) 
        self.create_widgets(controller)

    def create_widgets(self, controller): 
        username = ttk.Entry(self) 
        username.focus()
        username.grid(row = 1, column = 0, sticky = tk.EW, padx = 10, pady = (0,10))

