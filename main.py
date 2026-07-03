import tkinter as tk
from tkinter import font
# Import page functions
from pages.assignments import show_assignments
from pages.schedule import show_schedule
from pages.settings import show_settings
from pages.dashboard import show_dashboard

# == Create Main Window ==
root = tk.Tk()

root.title("School Planner")
root.geometry("900x600")

# == Color Theme ==

BACKGROUND = "#F4F6F9"
SIDEBAR = "#2E7D32"
BUTTON = "#388E3C"
TEXT = "white"

root.configure(bg=BACKGROUND)

# == Sidebar == 
sidebar = tk.Frame(
    root, 
    width=200, 
    bg=SIDEBAR
)

sidebar.pack(
    side="left", 
    fill="y"
)

# Keep the sidebar fixed in place
sidebar.pack_propagate(False)

# == Content Area ==
content = tk.Frame(
    root,
    bg=BACKGROUND
)

content.pack(
    side="right", 
    fill="both", 
    expand=True
)

# Command to clear content frame and display assignments page
def clear_content():
    for widget in content.winfo_children():
        widget.destroy() 

# == Sidebar title ==
sidebar_title = tk.Label(
    sidebar,
    text="School Planner",
    bg=SIDEBAR,
    fg=TEXT,
    font=("Helvetica", 16, "bold")
)

# == Sidebar Buttons ==
button_style = {
    "font": ("Helvetica", 12),
    "bg": BUTTON,
    "fg": TEXT,
    "relief": "flat",
    "width": 18,
    "pady": 8
}

tk.Button(
    sidebar,
    text="Dashboard",
    command=lambda: show_dashboard(content),
    **button_style
).pack(fill="x")

tk.Button(
    sidebar,
    text="Assignments",
    command=lambda: show_assignments(content),
    **button_style 
).pack(fill="x")

tk.Button(
    sidebar,
    text="Schedule",
    command=lambda: show_schedule(content),
    **button_style 
).pack(fill="x")

tk.Button(
    sidebar,
    text="Settings",
    command=lambda: show_settings(content),
    **button_style
).pack(fill="x")

show_dashboard(content)  # Show dashboard by default

# Start the program 
root.mainloop()