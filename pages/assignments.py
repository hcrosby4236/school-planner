import tkinter as tk
from data.database import (
    add_assignment,
    get_assignments,
    complete_assignment
)


# ============================================================
# Colors
# ============================================================

COLORS = {
    "background": "#FFF3F7",
    "card": "#FFFFFF",
    "primary": "#EC168C",
    "primary_hover": "#D9147F",
    "text": "#321827",
    "secondary_text": "#7D7180",
    "border": "#F6C3D9",
    "green": "#10B981",
    "orange": "#F59E0B",
    "red": "#EF4444",
    "blue": "#3B82F6"
}


# ============================================================
# Global Assignment Data
# ============================================================

assignment_data = []


# ============================================================
# Assignment Page
# ============================================================

def show_assignments(content):

    # --------------------------------------------------------
    # Clear previous page
    # --------------------------------------------------------

    for widget in content.winfo_children():
        widget.destroy()

    content.configure(bg=COLORS["background"])


    # --------------------------------------------------------
    # Main Container
    # --------------------------------------------------------

    container = tk.Frame(
        content,
        bg=COLORS["background"]
    )

    container.pack(
        fill="both",
        expand=True,
        padx=32,
        pady=30
    )


    # ========================================================
    # Header
    # ========================================================

    header = tk.Frame(
        container,
        bg=COLORS["background"]
    )

    header.pack(
        fill="x"
    )


    title_area = tk.Frame(
        header,
        bg=COLORS["background"]
    )

    title_area.pack(
        side="left"
    )


    tk.Label(
        title_area,
        text="Assignments",
        bg=COLORS["background"],
        fg=COLORS["text"],
        font=("Helvetica", 24, "bold")
    ).pack(
        anchor="w"
    )


    remaining_label = tk.Label(
        title_area,
        text="0 remaining",
        bg=COLORS["background"],
        fg=COLORS["secondary_text"],
        font=("Courier", 9)
    )

    remaining_label.pack(
        anchor="w",
        pady=(3, 0)
    )


    # --------------------------------------------------------
    # Add Assignment Button
    # --------------------------------------------------------

    add_button = tk.Button(
        header,
        text="+  Add Assignment",
        bg=COLORS["primary"],
        fg="white",
        activebackground=COLORS["primary_hover"],
        activeforeground="white",
        font=("Helvetica", 10, "bold"),
        relief="flat",
        bd=0,
        padx=18,
        pady=9,
        cursor="hand2"
    )

    add_button.pack(
        side="right"
    )


    # ========================================================
    # Filters / Sort
    # ========================================================

    controls = tk.Frame(
        container,
        bg=COLORS["background"]
    )

    controls.pack(
        fill="x",
        pady=(28, 20)
    )


    filter_frame = tk.Frame(
        controls,
        bg=COLORS["card"],
        highlightbackground=COLORS["border"],
        highlightthickness=1
    )

    filter_frame.pack(
        side="left"
    )


    current_filter = tk.StringVar(
        value="All"
    )


    # --------------------------------------------------------
    # Assignment Table
    # --------------------------------------------------------

    table = tk.Frame(
        container,
        bg=COLORS["card"],
        highlightbackground=COLORS["border"],
        highlightthickness=1
    )

    table.pack(
        fill="both",
        expand=True
    )


    # ========================================================
    # Add Assignment Window
    # ========================================================

    def open_add_window():

        window = tk.Toplevel(content)
        window.title("Add Assignment")
        window.geometry("400x400")
        window.configure(bg=COLORS["background"])
        window.resizable(False, False)


        frame = tk.Frame(
            window,
            bg=COLORS["background"]
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=30
        )


        tk.Label(
            frame,
            text="Add Assignment",
            bg=COLORS["background"],
            fg=COLORS["text"],
            font=("Helvetica", 20, "bold")
        ).pack(
            anchor="w",
            pady=(0, 25)
        )


        # Class
        tk.Label(
            frame,
            text="CLASS",
            bg=COLORS["background"],
            fg=COLORS["secondary_text"],
            font=("Courier", 8)
        ).pack(
            anchor="w"
        )


        class_entry = tk.Entry(
            frame,
            font=("Helvetica", 11),
            relief="flat",
            bg="#FFF0F5"
        )

        class_entry.pack(
            fill="x",
            pady=(5, 15),
            ipady=8
        )


        # Assignment
        tk.Label(
            frame,
            text="ASSIGNMENT",
            bg=COLORS["background"],
            fg=COLORS["secondary_text"],
            font=("Courier", 8)
        ).pack(
            anchor="w"
        )


        assignment_entry = tk.Entry(
            frame,
            font=("Helvetica", 11),
            relief="flat",
            bg="#FFF0F5"
        )

        assignment_entry.pack(
            fill="x",
            pady=(5, 15),
            ipady=8
        )


        # Due Date
        tk.Label(
            frame,
            text="DUE DATE",
            bg=COLORS["background"],
            fg=COLORS["secondary_text"],
            font=("Courier", 8)
        ).pack(
            anchor="w"
        )


        date_entry = tk.Entry(
            frame,
            font=("Helvetica", 11),
            relief="flat",
            bg="#FFF0F5"
        )

        date_entry.pack(
            fill="x",
            pady=(5, 25),
            ipady=8
        )


        def save_assignment():

            class_name = class_entry.get().strip()
            assignment_name = assignment_entry.get().strip()
            due_date = date_entry.get().strip()


            if not class_name or not assignment_name or not due_date:
                return


            add_assignment(
                class_name,
                assignment_name,
                due_date
            )


            window.destroy()
            refresh()


        tk.Button(
            frame,
            text="Add Assignment",
            command=save_assignment,
            bg=COLORS["primary"],
            fg="white",
            activebackground=COLORS["primary_hover"],
            activeforeground="white",
            font=("Helvetica", 10, "bold"),
            relief="flat",
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2"
        ).pack(
            anchor="e"
        )


    add_button.configure(
        command=open_add_window
    )


    # ========================================================
    # Filter Buttons
    # ========================================================

    def set_filter(value):

        current_filter.set(value)

        for button in filter_buttons:
            if button.cget("text") == value:
                button.configure(
                    bg=COLORS["primary"],
                    fg="white"
                )
            else:
                button.configure(
                    bg=COLORS["card"],
                    fg=COLORS["secondary_text"]
                )

        refresh()


    filter_buttons = []


    for filter_name in [
        "All",
        "Not Started",
        "Done"
    ]:

        button = tk.Button(
            filter_frame,
            text=filter_name,
            command=lambda value=filter_name: set_filter(value),
            font=("Helvetica", 9),
            relief="flat",
            bd=0,
            padx=12,
            pady=7,
            cursor="hand2"
        )

        button.pack(
            side="left"
        )

        filter_buttons.append(button)


    # Set initial active button

    filter_buttons[0].configure(
        bg=COLORS["primary"],
        fg="white"
    )


    # ========================================================
    # Table Header
    # ========================================================

    headers = [
        ("TITLE", 0),
        ("SUBJECT", 1),
        ("DUE", 2),
        ("PRIORITY", 3),
        ("STATUS", 4)
    ]


    for text, column in headers:

        tk.Label(
            table,
            text=text,
            bg=COLORS["card"],
            fg=COLORS["secondary_text"],
            font=("Courier", 8),
            anchor="w"
        ).grid(
            row=0,
            column=column,
            sticky="ew",
            padx=18,
            pady=14
        )


    table.columnconfigure(0, weight=4)
    table.columnconfigure(1, weight=2)
    table.columnconfigure(2, weight=1)
    table.columnconfigure(3, weight=1)
    table.columnconfigure(4, weight=2)
    table.columnconfigure(5, weight=0)


    # ========================================================
    # Refresh Assignments
    # ========================================================

    def refresh():

        global assignment_data

        assignment_data = get_assignments()


        # Remove old rows

        for widget in table.winfo_children():

            if int(widget.grid_info()["row"]) > 0:
                widget.destroy()


        # Update remaining count

        remaining = sum(
            1
            for assignment in assignment_data
            if not assignment[4]
        )

        remaining_label.configure(
            text=f"{remaining} remaining"
        )


        # Filter assignments

        selected_filter = current_filter.get()

        filtered = []

        for assignment in assignment_data:

            completed = assignment[4]

            if selected_filter == "All":
                filtered.append(assignment)

            elif selected_filter == "Done" and completed:
                filtered.append(assignment)

            elif selected_filter == "Not Started" and not completed:
                filtered.append(assignment)


        # ----------------------------------------------------
        # Display Rows
        # ----------------------------------------------------

        for row, assignment in enumerate(filtered, start=1):

            assignment_id = assignment[0]
            subject = assignment[1]
            title = assignment[2]
            due_date = assignment[3]
            completed = assignment[4]


            # Row background

            row_frame = tk.Frame(
                table,
                bg=COLORS["card"]
            )

            row_frame.grid(
                row=row,
                column=0,
                columnspan=6,
                sticky="ew"
            )


            # ------------------------------------------------
            # Title
            # ------------------------------------------------

            title_frame = tk.Frame(
                row_frame,
                bg=COLORS["card"]
            )

            title_frame.grid(
                row=0,
                column=0,
                sticky="ew",
                padx=18,
                pady=12
            )


            dot = tk.Label(
                title_frame,
                text="●",
                bg=COLORS["card"],
                fg=COLORS["green"]
                if completed
                else COLORS["primary"],
                font=("Helvetica", 9)
            )

            dot.pack(
                side="left",
                padx=(0, 8)
            )


            title_label = tk.Label(
                title_frame,
                text=title,
                bg=COLORS["card"],
                fg=COLORS["secondary_text"]
                if completed
                else COLORS["text"],
                font=("Helvetica", 10),
                anchor="w"
            )

            title_label.pack(
                side="left"
            )


            if completed:

                title_label.configure(
                    font=("Helvetica", 10, "overstrike")
                )


            # ------------------------------------------------
            # Subject
            # ------------------------------------------------

            tk.Label(
                row_frame,
                text=subject,
                bg=COLORS["card"],
                fg=COLORS["secondary_text"],
                font=("Courier", 8),
                anchor="w"
            ).grid(
                row=0,
                column=1,
                sticky="ew",
                padx=18
            )


            # ------------------------------------------------
            # Due Date
            # ------------------------------------------------

            tk.Label(
                row_frame,
                text=due_date,
                bg=COLORS["card"],
                fg=COLORS["secondary_text"],
                font=("Courier", 8),
                anchor="w"
            ).grid(
                row=0,
                column=2,
                sticky="ew",
                padx=18
            )


            # ------------------------------------------------
            # Temporary Priority
            # ------------------------------------------------

            priority_frame = tk.Frame(
                row_frame,
                bg=COLORS["card"]
            )

            priority_frame.grid(
                row=0,
                column=3,
                sticky="w",
                padx=18
            )


            tk.Label(
                priority_frame,
                text="●",
                bg=COLORS["card"],
                fg=COLORS["red"],
                font=("Helvetica", 8)
            ).pack(
                side="left"
            )


            tk.Label(
                priority_frame,
                text="High",
                bg=COLORS["card"],
                fg=COLORS["secondary_text"],
                font=("Courier", 8)
            ).pack(
                side="left",
                padx=3
            )


            # ------------------------------------------------
            # Status
            # ------------------------------------------------

            status_text = "Done" if completed else "Not Started"

            status_color = (
                COLORS["green"]
                if completed
                else COLORS["primary"]
            )


            status_label = tk.Label(
                row_frame,
                text=status_text,
                bg="#F4FFF9" if completed else "#FFF0F6",
                fg=status_color,
                font=("Courier", 8),
                padx=15,
                pady=5
            )

            status_label.grid(
                row=0,
                column=4,
                padx=18
            )


            # ------------------------------------------------
            # Complete Button
            # ------------------------------------------------

            if not completed:

                complete_button = tk.Button(
                    row_frame,
                    text="✓",
                    command=lambda aid=assignment_id: mark_complete(aid),
                    bg=COLORS["card"],
                    fg=COLORS["primary"],
                    activebackground=COLORS["primary"],
                    activeforeground="white",
                    relief="flat",
                    bd=0,
                    cursor="hand2",
                    font=("Helvetica", 11)
                )

                complete_button.grid(
                    row=0,
                    column=5,
                    padx=8
                )


    # ========================================================
    # Mark Complete
    # ========================================================

    def mark_complete(assignment_id):

        complete_assignment(
            assignment_id
        )

        refresh()


    # ========================================================
    # Initial Load
    # ========================================================

    refresh()