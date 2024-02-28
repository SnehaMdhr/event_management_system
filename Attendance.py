import sqlite3
from tkinter import Tk, Label, Entry, Button, Listbox, Scrollbar, messagebox
import sqlite3

def create_database():
    try:
        conn = sqlite3.connect('event_management.db')
        cursor = conn.cursor()

        # Create Event table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Event (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE
            )
        ''')

        # Create Attendance table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                event_name TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(event_name) REFERENCES Event(name),
                UNIQUE(student_id, event_name)
            )
        ''')

        print("Database and tables created successfully.")

    except sqlite3.Error as e:
        print("SQLite error:", e)
        print("An error occurred while creating the database and tables.")

    finally:
        conn.close()

if __name__ == "__main__":
    create_database()

class AttendanceSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance System")

        self.label_event = Label(root, text="Select Event:")
        self.label_event.grid(row=0, column=0, padx=10, pady=10)

        # Create a Listbox to show the available events
        self.event_listbox = Listbox(root, selectmode="single", height=5)
        self.event_listbox.grid(row=0, column=1, padx=10, pady=10)

        # Add a Scrollbar to navigate through the list of events
        scrollbar = Scrollbar(root, command=self.event_listbox.yview)
        scrollbar.grid(row=0, column=2, pady=10, sticky="nsew")
        self.event_listbox.config(yscrollcommand=scrollbar.set)

        # Populate the Listbox with initial event names
        self.populate_event_listbox()

        self.label_event_name = Label(root, text="New Event Name:")
        self.label_event_name.grid(row=1, column=0, padx=10, pady=10)

        self.entry_event_name = Entry(root)
        self.entry_event_name.grid(row=1, column=1, padx=10, pady=10)

        self.add_event_button = Button(root, text="Add Event", command=self.add_event)
        self.add_event_button.grid(row=1, column=2, padx=10, pady=10)

        self.label_student = Label(root, text="Student Email:")
        self.label_student.grid(row=2, column=0, padx=10, pady=10)

        self.entry_student = Entry(root)
        self.entry_student.grid(row=2, column=1, padx=10, pady=10)

        self.mark_button = Button(root, text="Mark Attendance", command=self.mark_attendance)
        self.mark_button.grid(row=2, column=2, padx=10, pady=10)

    def populate_event_listbox(self):
        try:
            conn = sqlite3.connect('event_management.db')
            cursor = conn.cursor()

            # Fetch event names from the Event table
            cursor.execute("SELECT name FROM Event")
            events = [row[0] for row in cursor.fetchall()]

            # Insert event names into the Listbox
            for event in events:
                self.event_listbox.insert("end", event)

        except sqlite3.Error as e:
            print("SQLite error:", e)
            messagebox.showerror("Error", "An error occurred while fetching event names.")

        finally:
            conn.close()

    def add_event(self):
        new_event_name = self.entry_event_name.get()

        if not new_event_name:
            messagebox.showerror("Error", "Please enter a new event name.")
            return

        try:
            conn = sqlite3.connect('event_management.db')
            cursor = conn.cursor()

            # Check if the event already exists
            cursor.execute("SELECT * FROM Event WHERE name = ?", (new_event_name,))
            existing_event = cursor.fetchone()

            if existing_event:
                messagebox.showinfo("Info", "Event already exists.")
            else:
                # Insert new event name into the Event table
                cursor.execute("INSERT INTO Event (name) VALUES (?)", (new_event_name,))
                conn.commit()

                # Update the Listbox with the new event name
                self.event_listbox.insert("end", new_event_name)

                messagebox.showinfo("Success", "Event added successfully!")

        except sqlite3.Error as e:
            print("SQLite error:", e)
            messagebox.showerror("Error", "An error occurred while adding the event.")

        finally:
            conn.close()

    def mark_attendance(self):
        # Get the selected event from the Listbox
        selected_index = self.event_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select an event.")
            return

        event_name = self.event_listbox.get(selected_index)
        student_id = self.entry_student.get()

        if not student_id:
            messagebox.showerror("Error", "Please enter Student ID.")
            return

        try:
            conn = sqlite3.connect('event_management.db')
            cursor = conn.cursor()

            # Check if the student is already marked for attendance in this event
            cursor.execute("SELECT * FROM Attendance WHERE event_name = ? AND student_id = ?", (event_name, student_id))
            existing_attendance = cursor.fetchone()

            if existing_attendance:
                messagebox.showinfo("Info", "Student already marked for attendance in this event.")
            else:
                # Insert new attendance record
                cursor.execute("INSERT INTO Attendance (event_name, student_id) VALUES (?, ?)", (event_name, student_id))
                conn.commit()
                messagebox.showinfo("Success", "Attendance marked successfully!")

        except sqlite3.Error as e:
            print("SQLite error:", e)
            messagebox.showerror("Error", "An error occurred while marking attendance.")

        finally:
            conn.close()



def add_event(event_name):
    try:
        conn = sqlite3.connect('event_management.db')
        cursor = conn.cursor()

        # Check if the event already exists
        cursor.execute("SELECT * FROM Event WHERE name = ?", (event_name,))
        existing_event = cursor.fetchone()

        if existing_event:
            print(f"Event '{event_name}' already exists.")
        else:
            # Insert the new event into the Event table
            cursor.execute("INSERT INTO Event (name) VALUES (?)", (event_name,))
            conn.commit()
            print(f"Event '{event_name}' added successfully.")

    except sqlite3.Error as e:
        print("SQLite error:", e)
        print("An error occurred while adding the event.")

    finally:
        conn.close()

# Add events to the database
events_to_add = ["Holi", "Dashain", "Valentines"]

for event in events_to_add:
    add_event(event)

# Create the Tkinter window
root = Tk()
attendance_system = AttendanceSystem(root)
root.mainloop()

