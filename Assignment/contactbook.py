import tkinter as tk
import sqlite3

class ContactBook:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")
        self.master.geometry("400x400")

        self.password_label = tk.Label(self.master, text="Password:", fg="white",  bg="light blue")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.master, text="Login", fg="white", bg="light blue", command=self.login)
        self.login_button.pack()

        self.contacts_frame = tk.Frame(self.master)

    def login(self):
        password = self.password_entry.get()

        if password == "1030":
            self.password_label.destroy()
            self.password_entry.destroy()
            self.login_button.destroy()

            self.load_contacts()
            self.contacts_frame.pack()

        else:
            tk.messagebox.showerror("Error", "Incorrect password")

    def load_contacts(self):
        self.contacts = []
        self.connection = sqlite3.connect("contacts.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone TEXT)")

        self.add_contact_button = tk.Button(self.contacts_frame, text="Add Contact", fg="pink", bg="black", command=self.add_contact)
        self.add_contact_button.pack()

        for row in self.cursor.execute("SELECT * FROM contacts"):
            self.contacts.append(row)
            contact_label = tk.Label(self.contacts_frame, text=row[0] + " - " + row[1], fg="brown")
            contact_label.pack()

    def add_contact(self):
        self.add_contact_window = tk.Toplevel(self.master)
        self.add_contact_window.title("Add Contact")
        self.add_contact_window.geometry("600x250")

        self.name_label = tk.Label(self.add_contact_window, text="Name:", fg="brown")
        self.name_label.pack()

        self.name_entry = tk.Entry(self.add_contact_window)
        self.name_entry.pack()

        self.phone_label = tk.Label(self.add_contact_window, text="Phone:", fg="brown")
        self.phone_label.pack()

        self.phone_entry = tk.Entry(self.add_contact_window)
        self.phone_entry.pack()

        self.save_button = tk.Button(self.add_contact_window, text="Save", fg="white", bg="brown", command=self.save_contact)
        self.save_button.pack()

    def save_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        self.cursor.execute("INSERT INTO contacts VALUES (?, ?)", (name, phone))
        self.connection.commit()

        self.contacts.append((name, phone))
        contact_label = tk.Label(self.contacts_frame, text=name + " - " + phone, fg="beige")
        contact_label.pack()

        self.add_contact_window.destroy()

root = tk.Tk()
contact_book = ContactBook(root)
root.mainloop()
