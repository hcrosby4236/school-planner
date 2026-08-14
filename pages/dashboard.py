import tkinter as tk
import data.database as db
from datetime import datetime


# ============================================================
# Dashboard Theme
# ============================================================

COLORS = {
    "background": "#FFF3F7",
    "card": "#FFFFFF",
    "primary": "#EC168C",
    "primary_light": "#FDE7F2",
    "green": "#10B981",
    "green_light": "#E8FAF4",
    "red": "#EF4444",
    "red_light": "#FFF0F0",
    "orange": "#F59E0B",
    "orange_light": "#FFF6E5",
    "text": "#321827",
    "secondary_text": "#7D7180",
    "border": "#F6C3D9"
}


# ============================================================
# Helper Functions
# ============================================================

def create_card(parent, **kwargs):
    """Create a white card with a pink border."""

    return tk.Frame(
        parent,
        bg=COLORS["card"],
        highlightbackground=COLORS["border"],
        highlightthickness=1,
        **kwargs
    )


def create_stat_card(parent, number, title, subtitle, color, light_color):
    """Create one of the dashboard statistic cards."""

    card = tk.Frame(
        parent,
        bg=COLORS["card"],
        highlightbackground=COLORS["border"],
        highlightthickness=1
    )

    number_label = tk.Label(
        card,
        text=str(number),
        bg=COLORS["card"],
        fg=color,
        font=("Helvetica", 26, "bold")
    )

    number_label.pack(
        anchor="w",
        padx=20,
        pady=(16, 0)
    )

    title_label = tk.Label(
        card,
        text=title,
        bg=COLORS["card"],
        fg=COLORS["text"],
        font=("Helvetica", 11, "bold")
    )

    title_label.pack(
        anchor="w",
        padx=20,
        pady=(2, 0)
    )

    subtitle_label = tk.Label(
        card,
        text=subtitle,
        bg=COLORS["card"],
        fg=COLORS["secondary_text"],
        font=("Courier", 8)
    )

    subtitle_label.pack(
        anchor="w",
        padx=20,
        pady=(0, 14)
    )

    return card


# ============================================================
# Dashboard
# ============================================================

def show_dashboard(content):

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


    # --------------------------------------------------------
    # Header
    # --------------------------------------------------------

    current_date = datetime.now().strftime("%A, %d %B %Y")

    date_label = tk.Label(
        container,
        text=f"{current_date}  ·  Term 1",
        bg=COLORS["background"],
        fg="#A34B76",
        font=("Courier", 10)
    )

    date_label.pack(
        anchor="w",
        pady=(0, 30)
    )


    # --------------------------------------------------------
    # Get Database Information
    # --------------------------------------------------------

    assignments = db.get_assignments()
    schedule = db.get_schedule()


    # --------------------------------------------------------
    # Statistics
    # --------------------------------------------------------

    total = len(assignments)

    completed = sum(
        assignment[4]
        for assignment in assignments
    )

    pending = total - completed

    # For now, use the first two incomplete assignments as the
    # urgent section. We will add a real priority field later.
    urgent = min(
        2,
        pending
    )


    # --------------------------------------------------------
    # Statistics Container
    # --------------------------------------------------------

    stats = tk.Frame(
        container,
        bg=COLORS["background"]
    )

    stats.pack(
        fill="x",
        pady=(0, 34)
    )

    stats.columnconfigure(0, weight=1)
    stats.columnconfigure(1, weight=1)
    stats.columnconfigure(2, weight=1)


    pending_card = create_stat_card(
        stats,
        pending,
        "Pending",
        "assignments",
        COLORS["primary"],
        COLORS["primary_light"]
    )

    pending_card.grid(
        row=0,
        column=0,
        sticky="ew",
        padx=(0, 8)
    )


    completed_card = create_stat_card(
        stats,
        completed,
        "Completed",
        "assignments",
        COLORS["green"],
        COLORS["green_light"]
    )

    completed_card.grid(
        row=0,
        column=1,
        sticky="ew",
        padx=8
    )


    urgent_card = create_stat_card(
        stats,
        urgent,
        "Urgent",
        "due soon",
        COLORS["red"],
        COLORS["red_light"]
    )

    urgent_card.grid(
        row=0,
        column=2,
        sticky="ew",
        padx=(8, 0)
    )


    # --------------------------------------------------------
    # Lower Dashboard Area
    # --------------------------------------------------------

    lower = tk.Frame(
        container,
        bg=COLORS["background"]
    )

    lower.pack(
        fill="both",
        expand=True
    )

    lower.columnconfigure(0, weight=1)
    lower.columnconfigure(1, weight=1)


    # ========================================================
    # Urgent Assignments
    # ========================================================

    assignments_section = tk.Frame(
        lower,
        bg=COLORS["background"]
    )

    assignments_section.grid(
        row=0,
        column=0,
        sticky="nsew",
        padx=(0, 10)
    )


    tk.Label(
        assignments_section,
        text="Urgent Assignments",
        bg=COLORS["background"],
        fg=COLORS["text"],
        font=("Helvetica", 14, "bold")
    ).pack(
        anchor="w",
        pady=(0, 12)
    )


    # Get incomplete assignments
    incomplete = [
        assignment
        for assignment in assignments
        if not assignment[4]
    ]


    if incomplete:

        for index, assignment in enumerate(incomplete[:4]):

            assignment_card = create_card(
                assignments_section
            )

            assignment_card.pack(
                fill="x",
                pady=(0, 8)
            )


            # Colored dot
            dot = tk.Label(
                assignment_card,
                text="●",
                bg=COLORS["card"],
                fg=COLORS["primary"]
                if index == 0
                else COLORS["orange"],
                font=("Helvetica", 10)
            )

            dot.pack(
                side="left",
                padx=(15, 8)
            )


            assignment_info = tk.Frame(
                assignment_card,
                bg=COLORS["card"]
            )

            assignment_info.pack(
                side="left",
                fill="x",
                expand=True,
                pady=10
            )


            title = assignment[2]

            tk.Label(
                assignment_info,
                text=title,
                bg=COLORS["card"],
                fg=COLORS["text"],
                font=("Helvetica", 11)
            ).pack(
                anchor="w"
            )


            # Current database structure provides the class name
            # and due date.
            subject = assignment[1]
            due_date = assignment[3]


            tk.Label(
                assignment_info,
                text=f"{subject}    Due {due_date}",
                bg=COLORS["card"],
                fg=COLORS["secondary_text"],
                font=("Courier", 8)
            ).pack(
                anchor="w",
                pady=(3, 0)
            )

    else:

        empty = create_card(
            assignments_section
        )

        empty.pack(
            fill="x"
        )

        tk.Label(
            empty,
            text="No urgent assignments",
            bg=COLORS["card"],
            fg=COLORS["secondary_text"],
            font=("Helvetica", 10)
        ).pack(
            pady=20
        )


    # ========================================================
    # Today's Classes
    # ========================================================

    schedule_section = tk.Frame(
        lower,
        bg=COLORS["background"]
    )

    schedule_section.grid(
        row=0,
        column=1,
        sticky="nsew",
        padx=(10, 0)
    )


    heading = tk.Frame(
        schedule_section,
        bg=COLORS["background"]
    )

    heading.pack(
        fill="x",
        pady=(0, 12)
    )


    tk.Label(
        heading,
        text="Today's Classes",
        bg=COLORS["background"],
        fg=COLORS["text"],
        font=("Helvetica", 14, "bold")
    ).pack(
        side="left"
    )


    tk.Label(
        heading,
        text=datetime.now().strftime("%A"),
        bg=COLORS["background"],
        fg=COLORS["secondary_text"],
        font=("Helvetica", 8)
    ).pack(
        side="left",
        padx=8,
        pady=3
    )


    if schedule:

        class_colors = [
            COLORS["primary"],
            COLORS["orange"],
            COLORS["green"],
            COLORS["primary"]
        ]

        for index, course in enumerate(schedule[:4]):

            class_card = create_card(
                schedule_section
            )

            class_card.pack(
                fill="x",
                pady=(0, 8)
            )


            # Colored vertical indicator
            indicator = tk.Frame(
                class_card,
                bg=class_colors[index % len(class_colors)],
                width=4
            )

            indicator.pack(
                side="left",
                fill="y",
                padx=(15, 10),
                pady=10
            )


            class_info = tk.Frame(
                class_card,
                bg=COLORS["card"]
            )

            class_info.pack(
                side="left",
                fill="both",
                expand=True,
                pady=10
            )


            class_name = course[1]

            tk.Label(
                class_info,
                text=class_name,
                bg=COLORS["card"],
                fg=COLORS["text"],
                font=("Helvetica", 11)
            ).pack(
                anchor="w"
            )


            # Display the currently available schedule data.
            details = " · ".join(
                str(value)
                for value in course[2:]
                if value is not None
            )


            tk.Label(
                class_info,
                text=details,
                bg=COLORS["card"],
                fg=COLORS["secondary_text"],
                font=("Courier", 8)
            ).pack(
                anchor="w",
                pady=(3, 0)
            )

    else:

        empty = create_card(
            schedule_section
        )

        empty.pack(
            fill="x"
        )

        tk.Label(
            empty,
            text="No classes scheduled",
            bg=COLORS["card"],
            fg=COLORS["secondary_text"],
            font=("Helvetica", 10)
        ).pack(
            pady=20
        )