print ("Schedule.py Loaded")

import tkinter as tk
import data.database as db

def show_schedule(content):

    # Clear the previous page
    for widget in content.winfo_children():
        widget.destroy()

    
    tk.Label(
        content,
        text="Course Name"
    ).pack()

    course_entry = tk.Entry(content)
    course_entry.pack()

    tk.Label(
        content, 
        text="Day"
    ).pack()

    day_entry = tk.Entry(content)
    day_entry.pack()

    tk.Label(
        content,
        text="Start Time"
    ).pack()   

    start_entry = tk.Entry(content)
    start_entry.pack() 

    tk.Label(
        content,
        text="End Time"
    ).pack()

    end_entry = tk.Entry(content)
    end_entry.pack()


    schedule_list = tk.Listbox(
        content,
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
        content,
        text="Add Class",
        command=add
    ).pack()

    refresh()

print("show_schedule exists:", "show_schedule" in globals())