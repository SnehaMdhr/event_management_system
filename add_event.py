import tkinter as tk
from tkinter import ttk
import sqlite3
from plyer import notification  # Import the notification module
import os

# Create the 'events' table if not exists
conn = sqlite3.connect("add.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS events(
               ID INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               date DATE,
               location TEXT,
               description TEXT
               )""")
conn.commit()
conn.close()

def go_to_homepage():
    root.destroy()
    os.system('python Homepageforadmin.py')

def add_record():
    # Get data from the entry widgets
    name = name_entry.get()
    date = date_entry.get()
    location = location_entry.get()
    description = description_entry.get()

    # Connect to SQLite database
    conn = sqlite3.connect("add.db")
    cursor = conn.cursor()

    # Insert record into events table
    cursor.execute("INSERT INTO events (name, date, location, description) VALUES (?, ?, ?, ?)", (name, date, location, description))

    # Commit changes and close connection
    conn.commit()
    conn.close()
    go_to_homepage()


    # Clear entry widgets
    name_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    location_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)

    # Notify that a new event has been added
    notification.notify(
        title="Event Added",
        message="New event has been added.",
    )

    print("Record added successfully.")

# Create main window
root = tk.Tk()
root.title("Add Event Record")

# Create form
form_frame = tk.Frame(root, padx=20, pady=20)
form_frame.pack()

name_label = tk.Label(form_frame, text="Event Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry = ttk.Entry(form_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

date_label = tk.Label(form_frame, text="Date (YYYY-MM-DD):")
date_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
date_entry = ttk.Entry(form_frame)
date_entry.grid(row=1, column=1, padx=5, pady=5)

location_label = tk.Label(form_frame, text="Location:")
location_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
location_entry = ttk.Entry(form_frame)
location_entry.grid(row=2, column=1, padx=5, pady=5)

description_label = tk.Label(form_frame, text="Description:")
description_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")  # Adjusted row index
description_entry = ttk.Entry(form_frame)
description_entry.grid(row=3, column=1, padx=5, pady=5)  # Adjusted row index

add_button = ttk.Button(form_frame, text="Add Record", command=add_record)
add_button.grid(row=4, column=0, columnspan=2, pady=10)  # Adjusted row index

root.mainloop()