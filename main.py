from logging import root
import tkinter as tk

class EditPad(tk.Frame):
    def __init__(self, root=None):
        # Import frame information for use within the class
        super().__init__(root)
        self.root = root
        self.window()
        self.menu()
        root.config(menu=self.menubar)
    
    def window(self):
        '''This created the main frame of the app where users can edit text documents'''
        self.text = tk.Text(self.root)
        self.text.pack(fill="both", expand=True)
    
    def menu(self):
        '''Menu and submenus will be created and displayed'''
        # Create Menu bars
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.formatmenu = tk.Menu(self.menubar, tearoff=0)
        self.codemenu = tk.Menu(self.menubar, tearoff=0)
        # Add options to submenus
        # File menu options
        self.filemenu.add_command(label='New              (Ctrl+N)')
        self.filemenu.add_command(label='New Window (Ctrl+Shift+N)')
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Save             (Ctrl+S)')
        self.filemenu.add_command(label='Save As...     (Ctrl+Shift+S)')
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Open             (Ctrl+O)')
        self.filemenu.add_command(label='Exit               (Ctrl+Q)')
        # Edit Menu
        self.editmenu.add_command(label='Undo       (Ctrl+Z)')
        self.editmenu.add_command(label='Redo       (Ctrl+Y)')
        self.editmenu.add_separator()
        self.editmenu.add_command(label='Cut')
        self.editmenu.add_command(label='Delete')
        self.editmenu.add_command(label='Copy')
        self.editmenu.add_command(label='Paste')
        self.editmenu.add_separator()
        self.editmenu.add_command(label='Find')
        self.editmenu.add_command(label='Find All')
        self.editmenu.add_command(label='Replace')
        self.editmenu.add_command(label='Select All')
        # Format Menu
        self.formatmenu.add_command(label='Font')
        self.formatmenu.add_command(label='Highlighting')
        # Code Menu
        self.codemenu.add_command(label='Python - Black')
        self.codemenu.add_command(label='Python - Flake8')

        # make menus visible in app
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.menubar.add_cascade(label="Format", menu=self.formatmenu)
        self.menubar.add_cascade(label="Coding", menu=self.codemenu)

if __name__ == "__main__":
    root = tk.Tk()
    root.title('EditPy')
    root.geometry('800x600')
    app = EditPad(root=root)
    app.mainloop()