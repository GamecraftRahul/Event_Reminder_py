import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import mysql.connector
from datetime import datetime
import winsound

# ================= DATABASE CONNECTION =================
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="RAHUL123",  # change this
        database="event_reminder_db"  # using your existing DB
    )

# ================= MAIN APPLICATION =================
class EventReminderApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Event Reminder System")
        self.root.geometry("1000x600")
        self.root.configure(bg="#1e1e2f")

        self.create_widgets()
        self.load_events()
        self.load_dashboard()
        self.check_reminders()

    # ================= UI =================
    def create_widgets(self):

        style = ttk.Style()
        style.theme_use("clam")

        # ===== Dashboard =====
        dashboard = tk.LabelFrame(self.root, text="Upcoming Events", fg="white", bg="#2c2f4a")
        dashboard.pack(fill="x", padx=10, pady=5)

        self.dashboard_text = tk.Label(
            dashboard, bg="#2c2f4a", fg="white",
            font=("Arial", 11), justify="left"
        )
        self.dashboard_text.pack(padx=10, pady=5)

        # ===== Form =====
        form = tk.LabelFrame(self.root, text="Event Details", fg="white", bg="#2c2f4a")
        form.pack(fill="x", padx=10, pady=5)

        tk.Label(form, text="Title", bg="#2c2f4a", fg="white").grid(row=0, column=0)
        self.title = tk.Entry(form, width=25)
        self.title.grid(row=0, column=1)

        tk.Label(form, text="Description", bg="#2c2f4a", fg="white").grid(row=1, column=0)
        self.desc = tk.Entry(form, width=25)
        self.desc.grid(row=1, column=1)

        tk.Label(form, text="Date", bg="#2c2f4a", fg="white").grid(row=2, column=0)
        self.date = DateEntry(form, date_pattern="yyyy-mm-dd")
        self.date.grid(row=2, column=1)

        tk.Label(form, text="Time (HH:MM:SS)", bg="#2c2f4a", fg="white").grid(row=3, column=0)
        self.time = tk.Entry(form)
        self.time.grid(row=3, column=1)

        tk.Button(form, text="Add Event", command=self.add_event,
                  bg="green", fg="white").grid(row=4, column=0, pady=10)

        tk.Button(form, text="Update Event", command=self.update_event,
                  bg="orange", fg="white").grid(row=4, column=1)

        tk.Button(form, text="Delete Event", command=self.delete_event,
                  bg="red", fg="white").grid(row=4, column=2)

        # ===== Search =====
        search_frame = tk.Frame(self.root, bg="#1e1e2f")
        search_frame.pack(pady=5)

        tk.Label(search_frame, text="Search:",
                 bg="#1e1e2f", fg="white").pack(side="left")

        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side="left", padx=5)

        tk.Button(search_frame, text="Search",
                  command=self.search_event).pack(side="left")

        tk.Button(search_frame, text="Show All",
                  command=self.load_events).pack(side="left", padx=5)

        # ===== Table =====
        self.tree = ttk.Treeview(
            self.root,
            columns=("ID", "Title", "Description", "Date", "Time", "Created"),
            show="headings"
        )
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        for col in ("ID", "Title", "Description", "Date", "Time", "Created"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        self.tree.bind("<ButtonRelease-1>", self.select_event)

    # ================= CRUD =================
    def add_event(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO events (title,description,event_date,event_time) VALUES (%s,%s,%s,%s)",
            (self.title.get(), self.desc.get(),
             self.date.get(), self.time.get())
        )
        conn.commit()
        conn.close()
        self.load_events()
        self.load_dashboard()
        messagebox.showinfo("Success", "Event Added Successfully")

    def update_event(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select event to update")
            return

        event_id = self.tree.item(selected)['values'][0]

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE events SET title=%s,description=%s,event_date=%s,event_time=%s WHERE id=%s",
            (self.title.get(), self.desc.get(),
             self.date.get(), self.time.get(), event_id)
        )
        conn.commit()
        conn.close()
        self.load_events()
        self.load_dashboard()
        messagebox.showinfo("Updated", "Event Updated Successfully")

    def delete_event(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select event to delete")
            return

        event_id = self.tree.item(selected)['values'][0]

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM events WHERE id=%s", (event_id,))
        conn.commit()
        conn.close()
        self.load_events()
        self.load_dashboard()
        messagebox.showinfo("Deleted", "Event Deleted Successfully")

    def load_events(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM events ORDER BY event_date")
        for row in cursor.fetchall():
            self.tree.insert("", tk.END, values=row)
        conn.close()

    def search_event(self):
        keyword = self.search_entry.get()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM events WHERE title LIKE %s",
            ('%' + keyword + '%',)
        )
        records = cursor.fetchall()
        conn.close()

        self.tree.delete(*self.tree.get_children())
        for row in records:
            self.tree.insert("", tk.END, values=row)

    def load_dashboard(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT title,event_date
            FROM events
            WHERE event_date >= CURDATE()
            ORDER BY event_date
            LIMIT 5
        """)
        records = cursor.fetchall()
        conn.close()

        text = ""
        for r in records:
            text += f"{r[0]} - {r[1]}\n"

        self.dashboard_text.config(text=text)

    def check_reminders(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M")

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT title,event_date,event_time FROM events")
        events = cursor.fetchall()
        conn.close()

        for event in events:
            dt = datetime.strptime(
                f"{event[1]} {event[2]}",
                "%Y-%m-%d %H:%M:%S"
            )
            if dt.strftime("%Y-%m-%d %H:%M") == now:
                winsound.Beep(1000, 1000)
                messagebox.showinfo("Reminder",
                                    f"{event[0]} is happening now!")

        self.root.after(60000, self.check_reminders)

    def select_event(self, event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected)['values']
            self.title.delete(0, tk.END)
            self.title.insert(0, values[1])
            self.desc.delete(0, tk.END)
            self.desc.insert(0, values[2])
            self.date.set_date(values[3])
            self.time.delete(0, tk.END)
            self.time.insert(0, values[4])


# ================= RUN =================
root = tk.Tk()
app = EventReminderApp(root)
root.mainloop()
