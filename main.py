from tkinter import *
import add
import all
import login
import create_account


wd = Tk()
wd.geometry("200x125")
wd.title("ToDo")
logged_in = False


def run_add():
    add.run()


def run_all():
    all.run()


def run_login():
    login.run()


def run_create_account():
    create_account.run()


title = Label(wd, text="ToDo", font=("Arial-Black", 15))

if logged_in:
    add_btn = Button(wd, text="Add task", command=run_add)
    all_btn = Button(wd, text="All tasks", command=run_all)

    add_btn.place(x=74, y=50)
    all_btn.place(x=75, y=80)

else:
    login_btn = Button(wd, text="Login", command=run_login)
    create_account_btn = Button(wd, text="Sign up", command=run_create_account)

    create_account_btn.place(x=75, y=50)
    login_btn.place(x=80, y=80)


title.place(x=75, y=0)

wd.mainloop()