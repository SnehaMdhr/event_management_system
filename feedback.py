from tkinter import *
from tkinter import messagebox
import sqlite3
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

def submit_feedback():
    feedback = message_feedback_box.get("1.0", "end-1c")
    if feedback.strip() == "":
        messagebox.showwarning("Warning", "Please provide feedback!")
    else:
        print("Submitting feedback...")
        add()
        print("Feedback submitted successfully")
        messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")
        root.destroy()
        os.system('python HomepageofSandA.py')

# Create the main window
root = Tk()
root.title("Feedback Form")
root.geometry("950x500")
root.minsize(width=950, height=500)
root.maxsize(width=950, height=500)
root.config(bg='#ADD8E6')

Feedback = Label(root, text='Feedback', fg='black', bg='#ADD8E6', font=('Times', 23, 'bold'))
Feedback.place(x=350, y=5)

name_feedback = Label(root, text="Name:", fg='black', bg='#ADD8E6', font=('Times', 12, 'bold'))
name_feedback.place(x=300, y=75)

Email_feedback = Label(root, text="Email:", fg='black', bg='#ADD8E6', font=('Times', 12, 'bold'))
Email_feedback.place(x=300, y=135)

message_feedback = Label(root, text="Message: ", fg='black', bg='#ADD8E6', font=('Times', 12, 'bold'))
message_feedback.place(x=300, y=200)

text_feedback = Text(root, height=1.5, width=40, fg='black', border=0, bg='#D9D9D9', font=('Times', 11))
text_feedback.place(x=300, y=100)

text_feedback_Emailbox = Text(root, height=1.5, width=40, fg='black', border=0, bg='#D9D9D9', font=('Times', 11))
text_feedback_Emailbox.place(x=300, y=160)

message_feedback_box = Text(root, height=5, width=40, fg='black', border=0, bg='#D9D9D9', font=('Times', 11))
message_feedback_box.place(x=300,y=230)

btn_submit = Button(root, text='Submit Feedback', fg='black', bg='#276B80', command=submit_feedback)
btn_submit.place(x=380,y=355)

def add():
    print("Adding feedback to database...")
    conn = sqlite3.connect("feedback.db")
    c = conn.cursor()
    c.execute("INSERT INTO feed(naam,mail,mess) VALUES (?,?,?)", (
        text_feedback.get("1.0", "end-1c"),
        text_feedback_Emailbox.get("1.0", "end-1c"),
        message_feedback_box.get("1.0", "end-1c")
    ))
    conn.commit()
    conn.close()
    print("Feedback added to database successfully")

def show_features():
    features_window = Toplevel(root)
    features_window.title("Features")
    features_window.geometry("200x200+800+213")
    features_window.config(bg='#ADD8E6')

    upcoming_events_btn = Button(features_window, text="Upcoming Events")
    upcoming_events_btn.pack(pady=5, fill=X, expand=True)

    attendance_btn = Button(features_window, text="Attendance")
    attendance_btn.pack(pady=5, fill=X, expand=True)

    events_calendar_btn = Button(features_window, text="Events Calendar")
    events_calendar_btn.pack(pady=5, fill=X, expand=True)

    more_btn = Button(features_window,text="More")
    more_btn.pack(pady=5, fill=X, expand=True)




root.mainloop()