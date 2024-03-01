import tkinter as tk
from tkinter import ttk
import sqlite3
from PIL import ImageTk, Image
import os

conn = sqlite3.connect("feedback.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS feed(
               ID INTEGER PRIMARY KEY AUTOINCREMENT,
               naam TEXT,
               mail TEXT,
               mess TEXT
               )""")
conn.commit()
conn.close()


def fetch_data():
    connection = sqlite3.connect("feedback.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM feed")
    data = cursor.fetchall()
    connection.close()
    return data

def populate_table():
    for row in table.get_children():
        table.delete(row)
    data = fetch_data()
    for record in data:
        table.insert("", tk.END, values=record)


def dot():
    root.destroy()
    os.system('python 3dotad.py')

root = tk.Tk()
root.title("KASA - The Event Manager")
root.configure(bg='#ADD8E6')
root.geometry("800x600")
header = tk.Canvas(root, width=800, height=150, bg="#001F3F")
header.create_text(500, 100, text="KASA - The Event Manager", fill="white", font=('Cochin', 30))


# Load and display the logo
logo = Image.open("KASA.png")
resized_image = logo.resize((150, 150))
new_image = ImageTk.PhotoImage(resized_image)
header.create_image(0, 10, anchor="nw", image=new_image)
header.pack(fill=tk.X)

# Create the main content canvas
mid = tk.Canvas(root, bg="white")
mid.pack(fill=tk.BOTH, expand=True)

features_button = tk.Button(root, text="☰", bg="#337AB7", fg="white", font=("Helvetica", 14), command=dot)
features_button.place(x=750, y=30)


# Styling the Treeview
style = ttk.Style()
style.theme_use('default')
style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3"
)
style.map('Treeview', background=[('selected', '#347083')])

table = ttk.Treeview(root, columns=("S.no", "name", "mail", "message"), show="headings", height=18)
table.heading("S.no", text="S.no")
table.heading("name", text="Name") 
table.heading("mail", text="Email")
table.heading("message", text="Message")

# Adjust column widths
column_width=60
for column in ("S.no", "name","mail", "message"):
    table.column(column, width=column_width)

populate_table()

# Positioning the table in the center
table.place(x=0, y=150, relwidth=1, relheight=1)

mid.pack()
root.mainloop()
