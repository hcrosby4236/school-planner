import tkinter as tk
import data.database as db


def show_dashboard(content):

    # -- Clear previous page --
    for widget in content.winfo_children():
        widget.destroy()

    # -- Page Title --
    tk.Label(
        content,
        text="Dashboard",
        font=("Arial", 24, "bold")
    ).pack(pady=20)

    # -- Cards Container --
    cards = tk.Frame(content)
    cards.pack(fill="both", expand=True, padx=20)

    cards.columnconfigure(0, weight=1)
    cards.columnconfigure(1, weight=1)
    cards.columnconfigure(2, weight=1)

    # == ASSIGNMENTS CARD ==
    assignment_card = tk.LabelFrame(
        cards,
        text="📚 Upcoming Assignments",
        padx=15,
        pady=15
    )

    assignment_card.grid(
        row=0,
        column=0,
        padx=10,
        pady=10,
        sticky="nsew"
    )

    assignments = db.get_assignments()

    if assignments:

        for assignment in assignments[:5]:

            status = "✓" if assignment[4] else "✗"

            tk.Label(
                assignment_card,
                anchor="w",
                text=f"{status} {assignment[2]}"
            ).pack(fill="x")

    else:

        tk.Label(
            assignment_card,
            text="No assignments."
        ).pack()

    # == SCHEDULE CARD ==
    schedule_card = tk.LabelFrame(
        cards,
        text="📅 Schedule",
        padx=15,
        pady=15
    )

    schedule_card.grid(
        row=0,
        column=1,
        padx=10,
        pady=10,
        sticky="nsew"
    )

    schedule = db.get_schedule()

    if schedule:

        for course in schedule[:5]:

            tk.Label(
                schedule_card,
                anchor="w",
                text=f"{course[1]} ({course[2]})"
            ).pack(fill="x")

    else:

        tk.Label(
            schedule_card,
            text="No classes."
        ).pack()

   # == STATISTICS CARD ==
    stats_card = tk.LabelFrame(
        cards,
        text="📈 Statistics",
        padx=15,
        pady=15
    )

    stats_card.grid(
        row=0,
        column=2,
        padx=10,
        pady=10,
        sticky="nsew"
    )

    total = len(assignments)
    completed = sum(a[4] for a in assignments)
    remaining = total - completed

    tk.Label(
        stats_card,
        text=f"Assignments: {total}"
    ).pack(anchor="w")

    tk.Label(
        stats_card,
        text=f"Completed: {completed}"
    ).pack(anchor="w")

    tk.Label(
        stats_card,
        text=f"Remaining: {remaining}"
    ).pack(anchor="w")