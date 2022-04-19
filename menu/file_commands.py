import tkinter as tk
from menu import data
from tkinter import INSERT, filedialog


class File(tk.Frame):
    def __init__(self, root=None, text_window=None):
        super().__init__(root)
        self.root = root
        self.text_window = text_window

    def new(self, event=None):
        self.root.title("New File - EditPy")
        self.text_window.delete("1.0", "end")

    def save(self, event=None):
        # Check filepath to see if its empty
        if data.save_path == None:
            # If empty, ask for file path
            save_path = filedialog.asksaveasfilename(
                filetypes=(("Text Document", "*.txt"), ("Python", "*.py")),
                defaultextension=".txt",
                title=("Save File..."),
            )
            # Save path for futher saves
            data.save_path = save_path
        # Save file
        with open(data.save_path, 'w') as file_to_save:
            file_to_save.write(self.text_window.get("1.0", "end-1c"))

    def save_as(self, event=None):
        # If empty, ask for file path
        save_path = filedialog.asksaveasfilename(
            filetypes=(("Text Document", "*.txt"), ("Python", "*.py")),
            defaultextension=".txt",
            title=("Save File..."),
        )
        # Save path for futher saves
        data.save_path = save_path
        # Save file
        with open(data.save_path, 'w') as file_to_save:
            file_to_save.write(self.text_window.get("1.0", "end-1c"))

    def open_file(self, event=None):
        data.save_path = filedialog.askopenfilename()
        print(data.save_path)
        self.text_window.delete("1.0", "end")
        with open(data.save_path,'r') as file:
            file_text = file.read()
            self.text_window.insert(INSERT, file_text)
