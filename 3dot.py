from tkinter import *
from tkinter.ttk import *
import os

root = Tk()
root.geometry("300x250+1200+221")
root.title("Features")

# Function to handle event button click
def event():
    root.destroy()
    os.system('python HomepageofSandA.py')

# Function to handle attendance button click
def attendance():
    root.destroy()
    os.system('python Attendance.py')

# Function to handle feedback button click
def feedback():
    root.destroy()
    os.system('python feedback.py')



# Function to set rounded button style
def set_rounded_button_style(button):
    button.config(style='RoundedButton.TButton')

# Create a custom style for rounded buttons
style = Style()
style.configure('RoundedButton.TButton', 
                foreground='green',          # Set text color to green
                background='light gray',     # Set background color to light gray
                font=('Arial', 12, 'bold'))

# Create buttons with rounded corners and icon buttons
upcoming_events_btn = Button(root, text="Upcoming Events", command=event)
set_rounded_button_style(upcoming_events_btn)
upcoming_events_btn.pack(pady=10, padx=20, fill=X)

attendance_btn = Button(root, text="Attendance", command=attendance)
set_rounded_button_style(attendance_btn)
attendance_btn.pack(pady=10, padx=20, fill=X)

feedback_btn = Button(root, text="Write Feedback", command=feedback)
set_rounded_button_style(feedback_btn)
feedback_btn.pack(pady=10, padx=20, fill=X)


root.mainloop()