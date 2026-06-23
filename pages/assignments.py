import tkinter as tk
from data.database import add_assignment, get_assignments, complete_assignment

assignment_data = []

# Function to open the assignments page
def show_assignments(content):

    for widget in content.winfo_children():
        widget.destroy()

    # Class Name
    tk.Label(
        content,
        text="Class"
    ).pack()

    class_entry = tk.Entry(content)
    class_entry.pack()


    # ----------------- ASSIGNMENT NAME INPUT -----------------
    # Label and entry box for assignment name
    tk.Label(
        content, 
        text="Assignment"
    ).pack()

    assignment_entry = tk.Entry(content)
    # Display entry box
    assignment_entry.pack()

    # ----------------- DUE DATE INPUT -----------------
    # Label and entry box for due date
    tk.Label(content, text="Due Date").pack()
    date_entry = tk.Entry(content)

    # Display entry box
    date_entry.pack()

    # Create listbox to display assignments and show it inside the window
    listbox = tk.Listbox(content, width=70)
    listbox.pack(pady=10)

    # ------------------ REFRESH FUNCTION -----------------
    # Reloads all assignmnet from database and displays them
    def refresh():

        # Clear listbox before reloading assignments
        listbox.delete(0, tk.END)

        assignment_data.clear()

        # Get all assignments from database and display them in listbox
        for item in get_assignments():

            assignment_data.append(item)

            # If completed = 1 show checkmark
            # If completed = 0 show X
            status = "✓" if item[4] else "✗"

            # Build a string to display the assignment in the listbox with the format:
            # [status] class name | assignment name | due date
            text = (
                f"{status} "
                f"{item[1]} | "
                f"{item[2]} | "
                f"{item[3]}"
            )

            # Add assignment to listbox
            listbox.insert(tk.END, text)

    # ------------------ ADD ASSIGNMENT FUNCTION -----------------
    # Runs when user clicks "Add Assignment" button, adds assignment to database and refreshes listbox
    def add():

        # Send entered information to database
        add_assignment(
            class_entry.get(),
            assignment_entry.get(),
            date_entry.get()
        )

        # Reload assignments after adding new one
        refresh()

    def mark_complete():

        # Get selected assignment
        selected = listbox.curselection()

        if not selected:
            return
        
        index = selected[0]

        assignment = assignment_data[index]
        assignment_id = assignment[0]

        complete_assignment(assignment_id)

        refresh()

    # Add assignment button
    tk.Button(
        content,
        text="Add Assignment",
        command=add
    ).pack()


    # Mark Complete Button
    tk.Button(
        content,
        text="Mark Complete",
        command=mark_complete
    ).pack()


    # Load assignments immediately when page is opened
    refresh()