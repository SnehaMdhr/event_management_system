import tkinter as tk
from tkinter import ttk
import sqlite3
from PIL import ImageTk, Image
import os

def fetch_data():
    connection = sqlite3.connect("management.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM data")
    data = cursor.fetchall()
    connection.close()
    return data

def populate_table():
    for row in table.get_children():
        table.delete(row)
    data = fetch_data()
    for record in data:
        table.insert("", tk.END, values=record)

def delete():
    try:
        selected_item = table.selection()[0]  # get selected item
        fname = table.item(selected_item)['values'][1]
        conn = sqlite3.connect("management.db")
        c = conn.cursor()
        c.execute("DELETE FROM data WHERE fname=?", (fname,))
        conn.commit()
        conn.close()
        table.delete(selected_item)
    except sqlite3.Error as error:
        print("Failed to delete record from sqlite table", error)
    except IndexError as ie:
        print("No item selected", ie)
    except Exception as e:
        print("An error occurred:", e)


def dot():
    root.destroy()
    os.system('python 3dotad.py')

root = tk.Tk()
root.title("KASA - The Event Manager")

# Load the background image
image = Image.open("bg.jpg") 
image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
bg = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


root.geometry("800x600")



header = tk.Canvas(root, width=800, height=150, bg="#001F3F")
header.create_text(500, 100, text="KASA - The Event Manager", fill="white", font=('Cochin', 30))


# Load and display the logo
logo = Image.open("KASA.png")
resized_image = logo.resize((150, 150))
new_image = ImageTk.PhotoImage(resized_image)
header.create_image(0, 10, anchor="nw", image=new_image)
header.pack(fill=tk.X)

features_button = tk.Button(root, text="☰", bg="#337AB7", fg="white", font=("Helvetica", 14), command=dot)
features_button.place(x=750, y=30)

# Create the main content canvas
mid = tk.Canvas(root, bg="white")
mid.pack(fill=tk.BOTH, expand=True)



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

table = ttk.Treeview(root, columns=("S.no", "fname", "lname", "me", "pass", "day", "month", "year", "gender"), show="headings", height=18)
table.heading("S.no", text="S.no")
table.heading("fname", text="First Name")
table.heading("lname", text="Last Name")  
table.heading("me", text="Email")
table.heading("pass", text="Password")
table.heading("day", text="Day of Birth")
table.heading("month", text="Month of Birth")
table.heading("year", text="Year of Birth")
table.heading("gender", text="Gender")

# Adjust column widths
column_width=60
for column in ("S.no", "fname", "lname", "me", "pass", "day", "month", "year", "gender"):
    table.column(column, width=column_width)

populate_table()

# Positioning the table in the center
table.place(x=0, y=190, relwidth=1, relheight=1)

# Delete button below the table
delete_button = tk.Button(root, text='Delete Selected', command=delete)
delete_button.place(x=350, y=160)

mid.pack()
root.mainloop()
