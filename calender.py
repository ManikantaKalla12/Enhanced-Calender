from tkinter import *
import calendar

events = {}

def add_event():
    date = date_field.get()
    event_text = event_field.get()
    if date and event_text:
        if date not in events:
            events[date] = []
        events[date].append(event_text)
        event_label.config(text=f"Events on {date}: {', '.join(events[date])}")
    date_field.delete(0, END)
    event_field.delete(0, END)

def show_calendar():
    year = int(year_field.get())
    gui = Toplevel()
    gui.title(f"Calendar {year}")
    cal_text = calendar.calendar(year)
    cal_label = Label(gui, text=cal_text, font="Consolas 10 bold", justify=LEFT)
    cal_label.pack()

# main window
root = Tk()
root.title("Enhanced Calendar")
root.geometry("400x300")

Label(root, text="Enter Year:").pack()
year_field = Entry(root)
year_field.pack()

Button(root, text="Show Calendar", command=show_calendar).pack(pady=5)

# Event Section
Label(root, text="Enter Date (YYYY-MM-DD):").pack()
date_field = Entry(root)
date_field.pack()

Label(root, text="Enter Event:").pack()
event_field = Entry(root)
event_field.pack()

Button(root, text="Add Event", command=add_event).pack(pady=5)
event_label = Label(root, text="", fg="blue")
event_label.pack()

root.mainloop()
