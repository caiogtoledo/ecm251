from turtle import position, title
import ttkbootstrap as ttk

base = ttk.Window(
    title="Minha GUI",
    size= (1024,400),
    position= (100,100),
    minsize= (600,300),
    maxsize= (1800,900),
    alpha=1.0
)

base.mainloop()