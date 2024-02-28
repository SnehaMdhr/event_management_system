import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import os

DATABASE_FILE = "add.db"

def go_to_homepage():
    root.destroy()
    os.system('python Homepageforadmin.py')

def add_record():
    name = name_entry.get()
    date = date_entry.get()
    location = location_entry.get()
    description = description_entry.get()

    if not (name and date and location and description):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    conn = None  # Initialize connection variable outside the try block
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO events (name, date, location, description) VALUES (?, ?, ?, ?)", (name, date, location, description))
        conn.commit()
        messagebox.showinfo("Success", "Record added successfully.")
        go_to_homepage()
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Database error: {e}")
    finally:
        if conn:  # Check if connection is not None before trying to close
            conn.close()
            name_entry.delete(0, tk.END)
            date_entry.delete(0, tk.END)
            location_entry.delete(0, tk.END)
            description_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Add Event Record")

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
description_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
description_entry = ttk.Entry(form_frame)
description_entry.grid(row=3, column=1, padx=5, pady=5)

add_button = ttk.Button(form_frame, text="Add Record", command=add_record)
add_button.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()