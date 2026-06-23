# Import TKinter
import tkinter as tk
# Import function to open assignments page
from pages.assignments import show_assignments
# Import function to open schedule page
from pages.schedule import show_schedule
# Import function to open settings page
from pages.settings import show_settings

root = tk.Tk()

# Set title and size of the window
root.title("School Planner")
root.geometry("1000x700")

# Create sidebar and content frames
sidebar = tk.Frame(
    root, 
    width=200, 
    bg="lightgray"
)

sidebar.pack(
    side="left", 
    fill="y"
)

content = tk.Frame(root)

content.pack(
    side="right", 
    fill="both", 
    expand=True
)

# Command to clear content frame and display assignments page
def clear_content():
    for widget in content.winfo_children():
        widget.destroy() 


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
    command=lambda: clear_content() or show_assignments(content)
)

assignments_button.pack(pady=10)

# Button to open schedule page
schedule_button = tk.Button(
    root,
    text="Schedule",
    command=lambda: clear_content() or show_schedule(content)
)

schedule_button.pack(pady=10)

# Button to open settings page
settings_button = tk.Button(
    root,
    text="Settings",
    command=lambda: clear_content() or show_settings(content)
)

settings_button.pack(pady=10)

# Sidebar buttons to open pages
tk.Button(
    sidebar,
    text="Dashboard",
    command=lambda: show_dashboard(content)
).pack(fill="x")

tk.Button(
    sidebar,
    text="Assignments",
    command=lambda: show_assignments(content)
).pack(fill="x")

tk.Button(
    sidebar,
    text="Schedule",
    command=lambda: show_schedule(content)
).pack(fill="x")

tk.Button(
    sidebar,
    text="Settings",
    command=lambda: show_settings(content)
).pack(fill="x")



root.mainloop()