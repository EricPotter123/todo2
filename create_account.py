from tkinter import *
from database import create_connection, create_accounts
import mail_sending
import login


def run():
    global password, wd
    wd = Tk()
    wd.geometry("300x325")
    wd.title("ToDo: Sign Up")

    def add_account():
        global email, username, password, wd

        conn = create_connection(r"C:\Users\Dell\Desktop\File folder\Python\Agileroo\To Do App\database\accounts.db")

        email = email_entry.get("1.0", "end")
        username = username_entry.get("1.0", "end")
        password = password_entry.get()

        create_accounts(conn, username, email, password)

        for widgets in wd.winfo_children():
            widgets.destroy()

        continue_()

    title = Label(wd, text="ToDo", font=("Arial-Black", 15))

    email_lbl = Label(wd, text="Email")
    email_entry = Text(wd, font=("Calibri", 10), width=30, height=1)

    username_lbl = Label(wd, text="Username")
    username_entry = Text(wd, font=("Calibri", 10), width=30, height=1)

    password_lbl = Label(wd, text="Password")
    password_entry = Entry(wd, font=("Calibri", 10), show="•")

    submit_btn = Button(wd, text="Submit", command=add_account)

    email_lbl.place(x=10, y=40)
    email_entry.place(x=10, y=60)
    username_lbl.place(x=10, y=90)
    username_entry.place(x=10, y=110)
    password_lbl.place(x=10, y=140)
    password_entry.place(x=10, y=170)

    submit_btn.place(x=50, y=200)

    title.place(x=125, y=0)

    def continue_():
        def next_():
            for thing in wd.winfo_children():
                thing.destroy()
            continue_2()

        Label(wd, text='''We sent you an email with the address\n\'TheToDoAppTeam2021@outlook.com\'.\nIf you didn\'t find it, try looking\n in the junk folder.''').place(x=40, y=0)
        mail_sending.run(email, '''All done! If you are seeing this email, you can go to the app and click \'next\'.''', 'Confirming')

        next_btn = Button(wd, text="Next", command=next_)

        next_btn.place(x=125, y=80)

    def continue_2():
        Label(wd, text="All done!", font=("Helvetica", 15)).place(x=100, y=10)
        Button(wd, text="Login", command=login.run).place(x=125, y=50)

    wd.mainloop()


run()
