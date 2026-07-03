import tkinter as tk

# Create a card widget with a title
def create_card(parent, title):

    card = tk.LabelFrame(
        parent,
        text=title,
        padx=15,
        pady=15
    )

    return card