import tkinter as tk


def open_settings():
    window = tk.Toplevel()

    window.title("Settings")
    window.geometry("500x400")

    def set_background_color(color):
        window.configure(bg=color)

    tk.Label(
        window, 
        text="Choose Background Color"
    ).pack(pady=10)

    tk.Button(
        window,
        text="Blue",
        command=lambda: set_background_color("lightblue")
    ).pack()

    tk.Button(
        window,
        text="Green",
        command=lambda: set_background_color("lightgreen")
    ).pack()

    tk.Button(
        window,
        text="Pink",
        command=lambda: set_background_color("pink")
    ).pack()

    def dark_mode():
        window.configure(bg="black")

    tk.Button(
        window,
        text="Dark Mode",
        command=dark_mode
    ).pack(pady=10)

    def light_mode():

        window.configure(bg="white")
        
    tk.Button(
        window,
        text="Light Mode",
        command=light_mode
    ).pack()