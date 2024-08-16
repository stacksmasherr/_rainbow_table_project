import tkinter as tk
from tkinter import messagebox
from rainbow_table import RainbowTable

class RainbowTableGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rainbow Table Generator")
        
        self.rainbow_table = RainbowTable()

        self.label = tk.Label(root, text="Enter Passwords (comma separated):")
        self.label.pack()

        self.entry = tk.Entry(root, width=50)
        self.entry.pack()

        self.generate_button = tk.Button(root, text="Generate Rainbow Table", command=self.generate_rainbow_table)
        self.generate_button.pack()

        self.lookup_label = tk.Label(root, text="Enter Hash to Lookup:")
        self.lookup_label.pack()

        self.lookup_entry = tk.Entry(root, width=50)
        self.lookup_entry.pack()

        self.lookup_button = tk.Button(root, text="Lookup", command=self.lookup_hash)
        self.lookup_button.pack()

    def generate_rainbow_table(self):
        passwords = self.entry.get().split(',')
        passwords = [pwd.strip() for pwd in passwords]
        self.rainbow_table.generate_table(passwords)
        self.rainbow_table.save_table()
        messagebox.showinfo("Info", "Rainbow Table Generated and Saved!")

    def lookup_hash(self):
        hash_value = self.lookup_entry.get().strip()
        result = self.rainbow_table.lookup(hash_value)
        if result:
            messagebox.showinfo("Result", f"Password found: {result}")
        else:
            messagebox.showerror("Error", "Password not found in Rainbow Table!")

if __name__ == "__main__":
    root = tk.Tk()
    app = RainbowTableGUI(root)
    root.mainloop()
