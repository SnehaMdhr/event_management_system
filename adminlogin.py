from tkinter import *
from PIL import Image, ImageTk 
from tkinter import messagebox 
import sqlite3
import os
import subprocess  # Add this line for subprocess


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


def signin():
    username=user.get()
    Password=pw.get()
    if username =='admin' and  Password == '1234':
        screen=Toplevel(root)
        screen.title('Log in')
        screen.geometry("1350x700+0+0")
        # screen.config(bg='ADD8E6')

        Label(screen,text='Welcome TO KASA Project!',bg='#fff', font=('Calibri(Body)',50,'bold')).pack(expand=True)
        screen.mainloop()
        
    elif username != 'admin' and Password == '1234':
        error_screen = Toplevel(root)
        error_screen.title("Invalid Username and Password")
        error_screen.geometry('400x400+400+300')
        Label(error_screen, text="Invalid username and password").pack()
        error_screen.mainloop()

    elif Password != "1234":
        error_screen = Toplevel(root)
        error_screen.title("Invalid Password")
        error_screen.geometry('400x400+400+300')
        Label(error_screen, text="Invalid password").pack()
        error_screen.mainloop()

    elif username != 'admin':
        error_screen = Toplevel(root)
        error_screen.title("Invalid Username")
        error_screen.geometry('400x400+400+300')
        Label(error_screen, text="Invalid username").pack()
        error_screen.mainloop()


def go_to_homepage():
    root.destroy()
    os.system('python Homepageforadmin.py')

def login():
    conn= sqlite3.connect("admin.db")
    c=conn.cursor()
    c.execute("SELECT * FROM data WHERE me = ? and pass = ?", (user.get(), pw.get()))


    result=c.fetchall()
    if result:
        messagebox.showinfo("Submitted", "Successfully logged in")
        go_to_homepage()
        
    else:
        error_screen = Toplevel(root)
        error_screen.title("Invalid")
        error_screen.geometry('400x400+400+300')
        Label(error_screen, text="Invalid").pack()
        error_screen.mainloop()

    conn.commit()
    conn.close()
    


def on_enter_username(e):
    user.delete(0, 'end')

def on_leave_username(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

def on_enter_password(e):
    pw.delete(0, 'end')

def on_leave_password(e):
    name = pw.get()
    if name == '':
        pw.insert(0, 'Password')


def show_password():
    if show_password_var.get():
        pw.config(show="")
    else:
        pw.config(show="*")

def reg():
    root.destroy()
    os.system('python admin.py')

def forget():
    root.destroy()
    os.system('python forgetadm.py')

root = Tk()
root.geometry('1200x800')
root.configure(bg="#fff")
root.config(bg='#ADD8E6')

# Load the background image
image = Image.open("bg.jpg") 
image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
bg = ImageTk.PhotoImage(image)
background_label = Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# root.resizable(0, 0)
# image = Image.open('TeamWork.jpg')
# resized_image = image.resize((200,100 ), Image.BILINEAR)
# img = ImageTk.PhotoImage(resized_image)
# Label(root, image=img,bg='#ADD8E6').place(x=75, y=100)

frame = Frame(root, width=600, height=450, bg="white")
frame.place(x=480, y=70)
frame.config(bg='gray')

root.resizable(0, 0)
image = Image.open('kasa.png')
resized_image = image.resize((100,80 ), Image.BILINEAR)
img = ImageTk.PhotoImage(resized_image)
Label(frame, image=img, bg='gray').place(x=350, y=2)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='gray', font=('Microsoft YaHei UI light', 23, 'bold'))
heading.place(x=100, y=5)

# create username entry box
user = Entry(frame, width=25, fg='black', border=0, bg='gray', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter_username)
user.bind('<FocusOut>', on_leave_username)
# user.bind('<Key>', on_enter_username )

Frame(frame, width=330, height=2, bg='black').place(x=25, y=107)


# for password
pw = Entry(frame, width=25, fg='black', border=0, bg='gray', font=('Microsoft YaHei UI Light', 11), show='*')
pw.place(x=30, y=150)
pw.insert(0, 'Password')
pw.bind('<FocusIn>', on_enter_password)
pw.bind('<FocusOut>', on_leave_password)
# pw.bind('<Key>', on_enter_password)
Frame(frame, width=330, height=2, bg='black').place(x=25, y=177)

show_password_var = BooleanVar()
show_password_var.set(False)

show_password_checkbox = Checkbutton(frame,  variable=show_password_var,
                                             onvalue=True, offvalue=False, font=("times new roman", 14),
                                             padx=5,pady=5 , bg="#151E4C", fg="Gray", command=show_password)
show_password_checkbox.place(x=320, y=130)


btn = Button(frame, width=30, pady=7, text='Sign in', bg='#57a1f8', fg='white', font=('Arial',12,'bold'), border=0, command=login)
btn.place(x=35, y=204)

lbl = Label(frame, text="Don't Have An Account?", fg='black', bg='gray', font=('Arial', 9))
lbl.place(x=40, y=260)


def forget_password_click(event):
    subprocess.run(["python", "forgetadmin.py"])

forget_password_label = Label(root, text="Forget Password?", font=("Arial", 10), background='gray')
forget_password_label.place(x=520, y=360)
forget_password_label.bind("<Button-1>", forget_password_click)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='gray', cursor='hand2', fg='blue',command=reg)
sign_up.place(x=180, y=260)
root.geometry("1380x700")





forgett = Button(frame, width=12, text='Forget password', border=0, bg='gray', cursor='hand2', fg='blue',command=forget)
forgett.place(x=180, y=290)
root.geometry("1380x700")

root.mainloop()
