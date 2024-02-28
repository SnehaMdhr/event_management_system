from tkinter import *
from PIL import Image, ImageTk
import os
from PIL import Image





root = Tk()
root.geometry("1570x1570")
root.resizable(0,0)

header = Canvas(root, width=1600, height=300, bg="#001F3F")
header.create_text(550, 130, text="KASA-\nThe Event Manager", fill="white", font=('Cochin', 80))
header.create_text(1330, 30, text="kasaeventmanager@gmail.com.np", fill="white", font=('Times', 20))
header.create_text(1330, 70, text="9810342323, 9825367231", fill="white", font=('Times', 20))
header.create_text(1330, 100, text="Mahakavi Marg, Kathmandu", fill="white", font=('Times', 20))

logo = (Image.open("KASA.png"))
resized_image = logo.resize((20, 20))
new_image = ImageTk.PhotoImage(resized_image)

header.create_image(30, 60, anchor=NW, image=new_image)
header.place(x=0, y=0)

mid = Canvas(root, width=1600, height=1300, bg="white")
mid.place(x=0, y=300)

teamwork = (Image.open("TeamWork.jpg"))
resized_image = teamwork.resize((800, 800))
new_image = ImageTk.PhotoImage(resized_image)

mid.create_image(650, 300, anchor=W, image=new_image)

mid.create_text(350, 60, text="Welcome to Softwarica College Event Management App...", fill="#2B8BB4",
                font=("Courier", 15))
mid.create_text(320, 160,
                text="Enhance your event experience with\nour perfect event management app.\nWith the best features and quality,\nyour event will be well-organized\nin our hands.",
                fill="#335CC3", font=("Courier New", 20))


def open_student_login():
    os.system('python log.py')

def open_admin_login():
    os.system('python adminlogin.py')
    
btn_student = Button(text="Student", height=2, width=15, bg='#605EC2', fg='Black', font='Helvetica 12 bold', command=open_student_login)
btn_student.place(x=300, y=600)

btn_admin = Button(text="Admins", height=2, width=15, bg='#605EC2', fg='Black', font='Helvetica 12 bold', command=open_admin_login)
btn_admin.place(x=480, y=600)





root.mainloop()
