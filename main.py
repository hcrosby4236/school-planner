import tkinter as tk

# Import page functions
from pages.assignments import show_assignments
from pages.schedule import show_schedule
from pages.settings import show_settings
from pages.dashboard import show_dashboard

# =================================================
# Main Window
# =================================================

root = tk.Tk()

root.title("School Planner")
root.geometry("900x600")

# ==================================================
# Color Theme
# ==================================================

BACKGROUND = "#F4F6F9"
SIDEBAR = "#2E7D32"
BUTTON = "#388E3C"
BUTTON_HOVER = "#43A047"
TEXT = "#FFFFFF"
CONTENT_TEXT = "#222222"

root.configure(bg=BACKGROUND)

# ==================================================
# Fonts
# ==================================================

TITLE_FONT = ("Helvetica", 18, "bold")
BUTTON_FONT = ("Helvetica", 12)
BODY_FONT = ("Helvetica", 11)

# ==================================================
# Sidebar
# ==================================================

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

# ==================================================
# Content Area
# ==================================================

content = tk.Frame(
    root,
    bg=BACKGROUND
)

content.pack(
    side="right", 
    fill="both", 
    expand=True
)

# =================================================
# Page Navigation
# =================================================
current_page = None
buttons = {}

def clear_content():
    """CRemove everything currently displayed in the content area."""

    for widget in content.winfo_children():
        widget.destroy()

def show_page(page_function, page_name):
    """Clear the current page and display the second page."""

    global current_page

    # Clear the content area
    clear_content()

    page_function(content)

    # Update the current page
    current_page = page_name

    update_active_button()

def update_active_button():
    """Update the appearance of the active sidebar button."""

    for name, button in buttons.items():

        if name == current_page:
            button.configure(bg=BUTTON_HOVER)

        else:
            button.configure(bg=BUTTON)


# =================================================
# Sidebar Title 
# =================================================

sidebar_title = tk.Label(
    sidebar,
    text="School Planner",
    bg=SIDEBAR,
    fg=TEXT,
    font=TITLE_FONT
)

sidebar_title.pack(
    pady=(30, 35)
)

# =================================================
# Sidebar Buttons
# =================================================

def create_sidebar_button(name, page_function):

    button = tk.Button(
        sidebar,
        text=name,
        command=lambda: show_page(page_function, name),
        font=BUTTON_FONT,
        bg=BUTTON,
        fg=TEXT,
        activebackground=BUTTON_HOVER,
        activeforeground=TEXT,
        relief="flat",
        bd=0,
        width=18,
        pady=10,
        cursor="hand2"
    )

    button.pack(
        fill="x",
        padx=12,
        pady=4
    )

    buttons[name] = button

create_sidebar_button(
    "Dashboard", 
    show_dashboard)
create_sidebar_button(
    "Assignments", 
    show_assignments)
create_sidebar_button(
    "Schedule", 
    show_schedule)
create_sidebar_button(
    "Settings", 
    show_settings
)

# =================================================
# Start on Dashboard
# =================================================

show_page(
    show_dashboard, 
    "Dashboard"
)

# =================================================
# Start Application
# =================================================

root.mainloop()