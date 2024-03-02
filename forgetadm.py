import tkinter as tk
import re
import sqlite3
from PIL import Image, ImageTk 
from tkinter import messagebox
import os


conn = sqlite3.connect("admin.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS data(
               ID INTEGER PRIMARY KEY AUTOINCREMENT,
               fname TEXT,
               lname TEXT,
               me TEXT,
               pass TEXT,
               day INT,
               month INT,
               year INT,
               gender TEXT,
               role TEXT
               )""")
conn.commit()
conn.close()

root = tk.Tk()
root.geometry("1350x700+0+0")
root.config(bg='#ADD8E6')


def show_password():
    if show_password_var.get():
        passw.config(show="")
    else:
        passw.config(show="*")
def check_password_requirements():
    # Password must contain at least one number, one special character, and one alphabet
    if re.search(r"(?=.*\d)(?=.*\W)(?=.*[a-zA-Z])", passw.get()):
        add()
        return True
    else:
        messagebox.showerror("Error", "Password must contain at least one number, one special character, and one alphabet.")
        return False
    
# Load the background image
image = Image.open("bg.jpg") 
image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
bg = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#D9D9D9', relief=tk.RIDGE)
frame.place(x=400, y=200, width=600, height=400)

Forget = tk.Label(root, text='Update your password', fg='black',bg='#D9D9D9', font=('Times', 23, 'bold'))
Forget.place(x=400, y=200)



email_label = tk.Label(frame, text="Email", font=("times new roman", 15), bg="#151E4C", fg="Gray")
email_label.place(x=50, y=100)
        

email =tk.Entry(frame, text= 'Email', width=30, bg="#C6B9B9")
email.place(x=180, y=100, width=280, height=30)


email_pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

new_password_label = tk.Label(frame, text="New Password", font=("times new roman", 15), bg="#151E4C", fg="Gray")
new_password_label.place(x=50, y=180)
        
passw =tk.Entry(frame, text= 'New Password', width=30, bg="#C6B9B9")
passw.place(x=180, y=180, width=280, height=30)
show_password_var = tk.BooleanVar()
show_password_var.set(False)

show_password_checkbox = tk.Checkbutton(frame,  variable=show_password_var,
                                             onvalue=True, offvalue=False, font=("times new roman", 14),
                                             padx=0,pady=0 , bg="#151E4C", fg="Gray", command=show_password)
show_password_checkbox.place(x=430, y=180)
    


def cancel():
    
    root.destroy()

def login():
    root.destroy()
    os.system('python main.py')

def add():
    conn = sqlite3.connect("admin.db")
    c = conn.cursor()
    c.execute("SELECT me FROM data")
    records = c.fetchall()
    print_records = " "
    email_input = email.get()
    match = email_input.isdigit() or re.match(email_pattern, email_input)
    if match:
        found = False
        for record in records:
            if record[0] == email_input:
                c.execute("""UPDATE data SET pass = ? WHERE me = ?""", (passw.get(), email_input))
                print("Password updated successfully.")
                messagebox.showinfo("Updated","Password updated successfully.")
                login()
                found = True
                break  # Exit the loop once the email is found
        if not found:
            messagebox.showerror("Error", "Email not found. Please try again.")
    else:
        messagebox.showerror("Error", "Invalid email. Please try again.")
    conn.commit()
    conn.close()


    

cancel_button = tk.Button(frame, text="Cancel", width=10,fg='black', bg='#5280A9', command=cancel)
cancel_button.place(x=180, y=240, width=80, height=30)

submit_button = tk.Button(frame, text="Submit", width=10, fg='black', bg='#5280A9',command=check_password_requirements)
submit_button.place(x=350, y=240, width=80, height=30)


root.mainloop()
