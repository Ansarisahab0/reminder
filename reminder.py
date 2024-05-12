import datetime
import tkinter as tk
from tkinter import messagebox

class Reminder:
    def __init__(self, root):
        self.root = root
        self.root.title("Remind Me")
        self.root.geometry("300x200")

        # Create labels and entry fields
        self.label_title = tk.Label(root, text="Title:")
        self.label_title.pack()
        self.entry_title = tk.Entry(root, width=30)
        self.entry_title.pack()

        self.label_date = tk.Label(root, text="Date (YYYY-MM-DD):")
        self.label_date.pack()
        self.entry_date = tk.Entry(root, width=30)
        self.entry_date.pack()

        self.label_time = tk.Label(root, text="Time (HH:MM):")
        self.label_time.pack()
        self.entry_time = tk.Entry(root, width=30)
        self.entry_time.pack()

        self.label_message = tk.Label(root, text="Message:")
        self.label_message.pack()
        self.entry_message = tk.Entry(root, width=30)
        self.entry_message.pack()

        # Create buttons
        self.button_set_reminder = tk.Button(root, text="Set Reminder", command=self.set_reminder)
        self.button_set_reminder.pack()

        self.button_clear = tk.Button(root, text="Clear", command=self.clear_fields)
        self.button_clear.pack()

    def set_reminder(self):
        title = self.entry_title.get()
        date = self.entry_date.get()
        time = self.entry_time.get()
        message = self.entry_message.get()

        if title and date and time and message:
            reminder_time = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
            current_time = datetime.datetime.now()

            if reminder_time > current_time:
                messagebox.showinfo("Reminder Set", "Reminder set successfully!")
                self.root.after((reminder_time - current_time).total_seconds() * 1000, lambda: messagebox.showinfo("Reminder", message))
            else:
                messagebox.showerror("Invalid Time", "Reminder time must be in the future.")
        else:
            messagebox.showerror("Invalid Input", "Please fill in all fields.")

    def clear_fields(self):
        self.entry_title.delete(0, tk.END)
        self.entry_date.delete(0, tk.END)
        self.entry_time.delete(0, tk.END)
        self.entry_message.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    reminder = Reminder(root)
    root.mainloop()
