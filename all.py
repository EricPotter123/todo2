from tkinter import *


def run():
    wd = Tk()
    wd.geometry("200x200")
    wd.title("ToDo: All tasks")

    listbox = Listbox(wd)
    listbox.pack(fill=BOTH, expand=1)

    wd.mainloop()
