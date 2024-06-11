import tkinter as tk
from tkinter import messagebox

def submit_details():
    name = name_entry.get()
    admission_number = admission_entry.get()

    if name == "" or admission_number == "":
        messagebox.showerror("Error", "Please fill in all the details.")
        return

    messagebox.showinfo("Confirmation", "Details submitted successfully.")

def submit_course():
    selected_course = course_var.get()
    confirmation_message = f"Your selected course is: {selected_course}"
    messagebox.showinfo("Course Selection", confirmation_message)
    messagebox.showinfo("Confirmation", "Thank you for enrolling!")

# Create main window
root = tk.Tk()
root.title("Student Enrollment Form")

# Create and pack widgets for details
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

admission_label = tk.Label(root, text="Admission Number:")
admission_label.grid(row=1, column=0, sticky="w")
admission_entry = tk.Entry(root)
admission_entry.grid(row=1, column=1)

submit_details_button = tk.Button(root, text="Submit Details", command=submit_details)
submit_details_button.grid(row=2, column=0, columnspan=2, pady=5)

# Course selection
courses = ["Mathematics", "Science", "History", "Computer Science"]
course_var = tk.StringVar(root)
course_var.set(courses[0])  # Default value

course_label = tk.Label(root, text="Select Course:")
course_label.grid(row=3, column=0, sticky="w")
course_menu = tk.OptionMenu(root, course_var, *courses)
course_menu.grid(row=3, column=1)

submit_course_button = tk.Button(root, text="Submit Course", command=submit_course)
submit_course_button.grid(row=4, column=0, columnspan=2, pady=5)

# Start the application
root.mainloop()
