import tkinter as tk

def show_settings(content):

    #Clear previous page 
    for widget in content.winfo_children():
        widget.destroy()
    
    def set_background_color(color):
        content.configure(bg=color)

    tk.Label(
        content, 
        text="Choose Background Color"
    ).pack(pady=10)

    tk.Button(
        content,
        text="Blue",
        command=lambda: set_background_color("lightblue")
    ).pack()

    tk.Button(
        content,
        text="Green",
        command=lambda: set_background_color("lightgreen")
    ).pack()

    tk.Button(
        content,
        text="Pink",
        command=lambda: set_background_color("pink")
    ).pack()

    def dark_mode():
        content.configure(bg="black")

    tk.Button(
        content,
        text="Dark Mode",
        command=dark_mode
    ).pack(pady=10)

    def light_mode():
        content.configure(bg="white")
        
    tk.Button(
        content,
        text="Light Mode",
        command=light_mode
    ).pack()