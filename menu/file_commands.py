import tkinter as tk
from tkinter import filedialog


class File(tk.Frame):
    def __init__(self, root=None, text_window=None):
        super().__init__(root)
        self.root = root
        self.text_window = text_window

    def new(self, event=None):
        self.root.title("New File - EditPy")
        self.text_window.delete("1.0", "end")

    def save(self, event=None, file_path=None):
        if file_path == None:
            save_path = filedialog.asksaveasfilename(
                filetypes=(("Text Document", "*.txt"), ("Python", "*.py")),
                defaultextension=".txt",
                title=("Choose name for File"),
            )
        with open(save_path, 'w') as file_to_save:
            file_to_save.write(self.text_window.get("1.0", "end-1c"))

    def save_as(self):
        pass

    def open_file(self):
        pass
