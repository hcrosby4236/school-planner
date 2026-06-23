import tkinter as tk
import data.database as db

def open_schedule():

    window = tk.Toplevel()

    window.title("Schedule")
    window.geometry("700x500")

    tk.Label(
        window, 
        text="Course Name"
    ).pack()

    course_entry = tk.Entry(window)
    course_entry.pack()

    tk.Label(
        window, 
        text="Day"
    ).pack()

    day_entry = tk.Entry(window)
    day_entry.pack()

    tk.Label(
        window,
        text="Start Time"
    ).pack()   

    start_entry = tk.Entry(window)
    start_entry.pack() 

    tk.Label(
        window,
        text="End Time"
    ).pack()

    end_entry = tk.Entry(window)
    end_entry.pack()


    schedule_list = tk.Listbox(
        window,
        width = 80
    )

    schedule_list.pack(pady=10)

    def refresh():

        schedule_list.delete(0, tk.END)

        for course in db.get_schedule():
            text = (
                f"{course[1]} | "
                f"{course[2]} | "
                f"{course[3]} - "
                f"{course[4]}"
            )

            schedule_list.insert(
                tk.END, 
                text
            )

    def add():
        db.add_class(
            course_entry.get(),
            day_entry.get(),
            start_entry.get(),
            end_entry.get()
        )

        refresh()

    tk.Button(
        window,
        text="Add Class",
        command=add
    ).pack()

    refresh()