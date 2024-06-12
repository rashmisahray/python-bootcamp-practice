import tkinter as tk
import sqlite3

class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.conn = sqlite3.connect('example.db')
        self.c = self.conn.cursor()
        self.create_table()
        self.create_widgets()

    def create_table(self):
        self.c.execute
        self.conn.commit()

    def create_widgets(self):
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()
        self.add_button = tk.Button(self.root, text="Add Record", command=self.add_record)
        self.add_button.pack()
        self.show_button = tk.Button(self.root, text="Show Records", command=self.show_records)
        self.show_button.pack()

    def add_record(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        self.c.execute("INSERT INTO contacts (name, email) VALUES (?, ?)", (name, email))
        self.conn.commit()

    def show_records(self):
        self.records = self.c.execute("SELECT * FROM contacts").fetchall()
        for record in self.records:
            print(record)

root = tk.Tk()
app = DatabaseApp(root)
root.mainloop()
