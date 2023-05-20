import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self):
        self.root = tk.Tk()
        font_size = 20
        self.root.title("Text Editor")
        self.text_entry = tk.Text(self.root, height=30, width=80,bg='#1d302b',fg="white",font=(font_size))
        self.text_entry.pack()
        self.create_menu()
    
    def create_menu(self):
        font_size = 20
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0,bg='#4fa891',fg="white",font=(font_size))
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)
        menu_bar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menu_bar, tearoff=0,bg='#4fa891',fg="white",font=(font_size))
        edit_menu.add_command(label="Cut", command=self.cut_text)
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        self.root.config(menu=menu_bar)

        help_menu = tk.Menu(menu_bar, tearoff=0,bg='#4fa891',fg="white",font=(font_size))
        help_menu.add_command(label="About", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

    def show_about(self):
        messagebox.showinfo("About", "Text Editor\nClass: Second Year\nCreated by: Shreya Chavan")
    def exit_app(self):
        result = self.check_file_saved()
        if result != "cancel":
            self.root.destroy()
            
    def new_file(self):
        result = self.check_file_saved()
        if result == "cancel":
            return
        self.text_entry.delete("1.0", tk.END)

    def open_file(self):
        result = self.check_file_saved()
        if result == "cancel":
            return
        filepath = filedialog.askopenfilename(title="Open File")
        if filepath:
            try:
                with open(filepath, "r") as file:
                    text = file.read()
                    self.text_entry.delete("1.0", tk.END)
                    self.text_entry.insert(tk.END, text)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {str(e)}")

    def save_file(self):
        filepath = getattr(self, "filepath", None)
        if filepath:
            self.save_content(filepath)
        else:
            self.save_file_as()

    def save_file_as(self):
        filepath = filedialog.asksaveasfilename(title="Save File")
        if filepath:
            self.save_content(filepath)

    def save_content(self, filepath):
        try:
            text = self.text_entry.get("1.0", tk.END)
            with open(filepath, "w") as file:
                file.write(text)
            self.filepath = filepath
            messagebox.showinfo("Success", "File saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {str(e)}")

    def check_file_saved(self):
        filepath = getattr(self, "filepath", None)
        if filepath:
            text = self.text_entry.get("1.0", tk.END)
            with open(filepath, "r") as file:
                if file.read() == text:
                    return "saved"
                else:
                    result = messagebox.askyesnocancel("Save changes", "Do you want to save changes?")
                    if result:
                        self.save_file()
                        return "saved"
                    elif result is None:
                        return "cancel"
        return "not_saved"

    def cut_text(self):
        self.text_entry.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_entry.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_entry.event_generate("<<Paste>>")

    def run(self):
        
        self.root.mainloop()
        
editor = TextEditor()
editor.run()
