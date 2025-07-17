import tkinter as tk
from backend import create_excel_file

def create_window():
    """
    Creates and configures the main application window, including all UI components.
    Returns the main window (`root`), entry fields, checkbuttons, file format variable,
    and buttons for further configuration and use in the main application.
    """
    global root, frame, name_entry, email_entry, phone_entry, branch_vars, file_format_var, submit_button, download_button, clear_button

    # Define color scheme
    bg_color = "#2c3e50"
    label_bg_color = "#34495e"
    entry_bg_color = "#ecf0f1"
    button_bg_color = "#1abc9c"
    button_fg_color = "#ffffff"

    # Create the main application window
    root = tk.Tk()
    root.title("User Data Form")
    root.configure(background=bg_color)  # Set background color of the window

    # Create and pack the title label
    label = tk.Label(root, text="User Data Form", font=("Roboto", 35), bg=bg_color, fg=button_fg_color)
    label.pack(pady=20)

    # Create and pack the main frame
    frame = tk.Frame(root, bg=bg_color)
    frame.pack(padx=100, pady=20)

    # Define common width for labels and entry fields
    label_width = 20
    entry_width = 30

    # Create and place the Name label and entry field
    name_label = tk.Label(frame, text="Name", font=("Arial", 20), width=label_width, anchor='w', bg=label_bg_color, fg=button_fg_color)
    name_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
    name_entry = tk.Entry(frame, font=("Helvetica", 20), width=entry_width, bg=entry_bg_color)
    name_entry.grid(row=0, column=1, padx=10, pady=10, sticky='e')

    # Create and place the Email ID label and entry field
    email_label = tk.Label(frame, text="Email ID", font=("Arial", 20), width=label_width, anchor='w', bg=label_bg_color, fg=button_fg_color)
    email_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    email_entry = tk.Entry(frame, font=("Helvetica", 20), width=entry_width, bg=entry_bg_color)
    email_entry.grid(row=1, column=1, padx=10, pady=10, sticky='e')

    # Create and place the Phone Number label and entry field
    phone_label = tk.Label(frame, text="Phone Number", font=("Arial", 20), width=label_width, anchor='w', bg=label_bg_color, fg=button_fg_color)
    phone_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    phone_entry = tk.Entry(frame, font=("Helvetica", 20), width=entry_width, bg=entry_bg_color)
    phone_entry.grid(row=2, column=1, padx=10, pady=10, sticky='e')

    # Create BooleanVar objects to track branch selections
    branch_vars = {
        "Engineering": tk.BooleanVar(),
        "Medical": tk.BooleanVar(),
        "Degree": tk.BooleanVar()
    }

    # Create and place the branch checkboxes
    branch_frame = tk.Frame(frame, bg=bg_color)
    branch_label = tk.Label(branch_frame, text="Branch", font=("Arial", 20), anchor='w', bg=label_bg_color, fg=button_fg_color)
    branch_label.pack(side=tk.LEFT)
    engineering_checkbox = tk.Checkbutton(branch_frame, text="Engineering", variable=branch_vars["Engineering"], font=("Helvetica", 20), bg=bg_color, fg=button_fg_color, selectcolor=entry_bg_color)
    engineering_checkbox.pack(side=tk.LEFT, padx=20)
    medical_checkbox = tk.Checkbutton(branch_frame, text="Medical", variable=branch_vars["Medical"], font=("Helvetica", 20), bg=bg_color, fg=button_fg_color, selectcolor=entry_bg_color)
    medical_checkbox.pack(side=tk.LEFT, padx=20)
    degree_checkbox = tk.Checkbutton(branch_frame, text="Degree", variable=branch_vars["Degree"], font=("Helvetica", 20), bg=bg_color, fg=button_fg_color, selectcolor=entry_bg_color)
    degree_checkbox.pack(side=tk.LEFT, padx=20)
    branch_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # Create and place the file format selection menu
    file_format_var = tk.StringVar(value='json')
    file_format_label = tk.Label(frame, text="File Format", font=("Arial", 20), width=label_width, anchor='w', bg=label_bg_color, fg=button_fg_color)
    file_format_label.grid(row=4, column=0, padx=10, pady=10, sticky='w')
    file_format_menu = tk.OptionMenu(frame, file_format_var, 'json', 'txt', 'xml', 'xlsx')
    file_format_menu.config(font=("Helvetica", 15), bg=entry_bg_color, fg=bg_color, activebackground=button_bg_color, activeforeground=button_fg_color)
    file_format_menu.grid(row=4, column=1, padx=10, pady=10, sticky='e')

    # Create and place the action buttons
    submit_button = tk.Button(frame, text="Submit", font=("Arial", 20), bg=button_bg_color, fg=button_fg_color)
    submit_button.grid(row=5, column=0, padx=10, pady=10)

    download_button = tk.Button(frame, text="Download", font=("Arial", 20), bg="#3498db", fg=button_fg_color)
    download_button.grid(row=5, column=1, padx=10, pady=10)

    clear_button = tk.Button(frame, text="Clear", font=("Arial", 20), bg="#e74c3c", fg=button_fg_color)
    clear_button.grid(row=5, column=2, padx=10, pady=10)

    # Return the window and widgets to be used in the main application
    return root, name_entry, email_entry, phone_entry, branch_vars, file_format_var, submit_button, download_button, clear_button

# Example usage
if __name__ == "__main__":
    root, name_entry, email_entry, phone_entry, branch_vars, file_format_var, submit_button, download_button, clear_button = create_window()
    root.mainloop()