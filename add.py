from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import database


def run():
    global hour_start, mins_var_start, sec_start, hour_end, mins_var_end, sec_end, cal1, cal2, conn
    window = Tk()
    window.title("ToDo: Add Task")
    window.geometry("400x400")

    conn = database.create_connection(r"C:\Users\Dell\Desktop\File folder\Python\Agileroo\To Do App\database\tasks.db")

    def submit_funct():
        global hour_start, mins_var_start, sec_start, hour_end, mins_var_end, sec_end, cal1, cal2, conn
        time1 = cal1.get()
        hour_start = str(h_start.get())
        mins_var_start = str(mins_start.get())
        sec_start = str(s_start.get())
        start_time = time1 + " " + hour_start + " " + mins_var_start + " " + sec_start

        time2 = str(cal2.get())
        hour_end = str(h_end.get())
        mins_var_end = str(mins_end.get())
        sec_end = str(s_end.get())
        end_time = time2 + " " + hour_end + " " + mins_var_end + " " + sec_end

        title_v = title_entry.get("1.0", "end-1c")
        description = str(describe_entry.get("1.0", "end-1c"))

        database.create_task(conn, title_v, description, start_time, end_time)

    hrs = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
           "18", "19", "20", "21", "22", "23"]

    s_m = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
           "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35",
           "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53",
           "54", "55", "56", "57", "58", "59"]

    title_label = Label(window, text="Title: ")
    title_entry = Text(window, font=("Calibri", 10), width=30, height=1)

    describe_label = Label(window, text="Description: ")
    describe_entry = Text(window, font=("Calibri", 10), width=30, height=5)

    to_start = Label(window, text='To start: ')
    to_end = Label(window, text='To end: ')

    label1 = Label(window, text=":")
    label2 = Label(window, text=":")
    label3 = Label(window, text=":")
    label4 = Label(window, text=":")

    submit = Button(window, text="Submit", command=submit_funct)

    title = Label(window, text="To Do", font=("Arial-Black", 15))

    h_start = ttk.Combobox(window, values=hrs, state="readonly", width=3)
    hour_start = h_start.get()
    h_start.set("00")

    mins_start = ttk.Combobox(window, values=s_m, state="readonly", width=3)
    mins_var_start = mins_start.get()
    mins_start.set("00")

    s_start = ttk.Combobox(window, values=s_m, state="readonly", width=3)
    sec_start = s_start.get()
    s_start.set("00")

    h_end = ttk.Combobox(window, values=hrs, state="readonly", width=3)
    hour_end = h_end.get()
    h_end.set("00")

    mins_end = ttk.Combobox(window, values=s_m, state="readonly", width=3)
    mins_var_end = mins_end.get()
    mins_end.set("00")

    s_end = ttk.Combobox(window, values=s_m, state="readonly", width=3)
    sec_end = s_end.get()
    s_end.set("00")

    cal1 = DateEntry(window, selectmode='day')
    cal2 = DateEntry(window, selectmode='day')

    title_label.place(x=5, y=40)
    title_entry.place(x=40, y=40)

    describe_label.place(x=5, y=60)
    describe_entry.place(x=75, y=60)

    cal1.place(x=57, y=150)
    cal2.place(x=290, y=150)

    to_start.place(x=5, y=150)
    to_end.place(x=240, y=150)

    h_start.place(x=5, y=180)
    label1.place(x=47, y=180)
    mins_start.place(x=57, y=180)
    label2.place(x=99, y=180)
    s_start.place(x=109, y=180)

    h_end.place(x=240, y=180)
    label3.place(x=282, y=180)
    mins_end.place(x=292, y=180)
    label4.place(x=334, y=180)
    s_end.place(x=344, y=180)

    submit.place(x=173, y=220)
    title.place(x=170, y=0)

    window.mainloop()


run()
