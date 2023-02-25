import unittest
from tkinter import Tk
from contactbook import ContactBook

class TestContactBook(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.contact_book = ContactBook(self.root)

    def test_login_with_correct_password(self):
        self.contact_book.password_entry.insert(0, "1030")
        self.contact_book.login()
        self.assertIsNotNone(self.contact_book.contacts_frame)

    def test_login_with_incorrect_password(self):
        self.contact_book.password_entry.insert(0, "wrong_password")
        with self.assertRaises(tk.messagebox.showerror):
            self.contact_book.login()

    def test_add_contact(self):
        self.contact_book.password_entry.insert(0, "1030")
        self.contact_book.login()
        initial_contacts_count = len(self.contact_book.contacts)
        self.contact_book.add_contact_window = Tk()
        self.contact_book.name_entry.insert(0, "John")
        self.contact_book.phone_entry.insert(0, "1234567890")
        self.contact_book.save_contact()
        self.assertEqual(len(self.contact_book.contacts), initial_contacts_count + 1)

    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()
