import tkinter as tk
from tkinter import ttk
import os
import sqlite3
from PIL import Image, ImageTk

def populate_event_list():
    # Connect to the database
    conn = sqlite3.connect("add.db")
    cursor = conn.cursor()

    # Execute query to fetch event data
    cursor.execute("SELECT name, date, location FROM events")

    # Fetch all rows
    events = cursor.fetchall()

    # Populate event list with retrieved data
    for event in events:
        event_listbox.insert("", "end", values=event)

    # Close the connection
    conn.close()

def add():
    root.destroy()
    os.system('python add_event.py')

def dot():
    root.destroy()
    os.system('python 3dotad.py')

# Create main window
root = tk.Tk()
root.title("Event List Page")
root.geometry("800x600")

# Load the background image
image = Image.open("bg.jpg")
image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
bg = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Event List Frame
event_list_frame = tk.Frame(root, bg="#f0f0f0", bd=2, relief=tk.GROOVE)
event_list_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Event List Heading
heading_label = tk.Label(event_list_frame, text="Event List", font=("Helvetica", 20), bg="#f0f0f0")
heading_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

# Event List
event_listbox = ttk.Treeview(event_list_frame, columns=("Name", "Date", "Location"), show="headings", height=15)
event_listbox.heading("Name", text="Name")
event_listbox.heading("Date", text="Date")
event_listbox.heading("Location", text="Location")
event_listbox.grid(row=1, column=0, columnspan=3)

# Populate Event List
populate_event_list()

Add_button = tk.Button(root, text="Add Events", fg='white', bg='#4CAF50', font=('Helvetica', 12, 'bold'), command=add)
Add_button.place(x=500, y=350)

features_button = tk.Button(root, text="☰", bg="#337AB7", fg="white", font=("Helvetica", 14), command=dot)
features_button.place(x=700, y=50)

root.mainloop()

