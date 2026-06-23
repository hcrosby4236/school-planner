# Import TKinter
import tkinter as tk
# Import function to open assignments page
from pages.assignments import open_assignments
# Import function to open schedule page
from pages.schedule import open_schedule
# Import function to open settings page
from pages.settings import open_settings

root = tk.Tk()

# Set title and size of the window
root.title("School Planner")
root.geometry("1000x700")

# Title on top of page
title = tk.Label(root,
        text="School Planner", 
        font=("Arial", 24, "bold")
)

title.pack(pady=20)

# Button to open assignments page
assignments_button = tk.Button(
    root,
    text="Assignments",
    command=open_assignments
)

assignments_button.pack(pady=10)

# Button to open schedule page
schedule_button = tk.Button(
    root,
    text="Schedule",
    command=open_schedule
)

schedule_button.pack(pady=10)

# Button to open settings page
settings_button = tk.Button(
    root,
    text="Settings",
    command=open_settings
)

settings_button.pack(pady=10)

root.mainloop()