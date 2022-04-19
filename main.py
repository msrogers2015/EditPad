from menu import data
import tkinter as tk
from menu import file_commands, edit


class EditPad(tk.Frame):
    def __init__(self, root=None):
        # Import frame information for use within the class
        super().__init__(root)
        data.frame_title = 'New File - Edit Py'
        self.root = root
        data.save_path = None
        self.window()
        self.fc = file_commands.File(root=self.root, text_window=self.text)
        self.edit = edit.Edit(root=self.root, text_window=self.text)
        self.menu()
        self.key_binding()
        root.config(menu=self.menubar)

    def update_title(self, even=None):
        self.root.title(f'* {data.frame_title}')

    def key_binding(self):
        # File Menu Shortcuts
        self.root.bind("<Control-n>", self.fc.new)
        self.root.bind('<KeyRelease>', self.update_title)
        self.root.bind("<Control-s>", self.fc.save)
        self.root.bind("<Control-S>", self.fc.save_as)
        self.root.bind("<Control-o>", self.fc.open_file)
        self.root.bind('<Control-q>', quit)
        # Edit Menu Shortcuts
        #self.root.bind("<Control-z>", self.edit.undo)

    def window(self):
        """This created the main frame of the app
        where users can edit text documents"""
        self.text = tk.Text(self.root, wrap="none", undo=True, autoseparators=True)
        self.text.pack(fill="both", expand=True)

    def menu(self):
        """Menu and submenus will be created and displayed"""
        # Create Menu bars
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.formatmenu = tk.Menu(self.menubar, tearoff=0)
        self.codemenu = tk.Menu(self.menubar, tearoff=0)
        # Add options to submenus
        # File menu options
        self.filemenu.add_command(label="New              (Ctrl+N)", command=self.fc.new)
        self.filemenu.add_command(label="New Window (Ctrl+Shift+N)")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Save             (Ctrl+S)", command=self.fc.save)
        self.filemenu.add_command(label="Save As...     (Ctrl+Shift+S)")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Open             (Ctrl+O)", command=self.fc.open_file)
        self.filemenu.add_command(label="Exit               (Ctrl+Q)", command=quit)
        # Edit Menu
        self.editmenu.add_command(label="Undo       (Ctrl+Z)")
        self.editmenu.add_command(label="Redo       (Ctrl+Y)")
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Cut")
        self.editmenu.add_command(label="Delete")
        self.editmenu.add_command(label="Copy")
        self.editmenu.add_command(label="Paste")
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Find")
        self.editmenu.add_command(label="Find All")
        self.editmenu.add_command(label="Replace")
        self.editmenu.add_command(label="Select All")
        # Format Menu
        self.formatmenu.add_command(label="Font")
        self.formatmenu.add_command(label="Highlighting")
        # Code Menu
        self.codemenu.add_command(label="Python - Black")
        self.codemenu.add_command(label="Python - Flake8")

        # make menus visible in app
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.menubar.add_cascade(label="Format", menu=self.formatmenu)
        self.menubar.add_cascade(label="Coding", menu=self.codemenu)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("New File - EditPy")
    root.geometry("800x600")
    app = EditPad(root=root)
    app.mainloop()
