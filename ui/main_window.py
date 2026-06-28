import tkinter as tk
from core.storage import load_passwords
from ui.create_dialog import CreateDialog

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager")
        self.geometry("400x500")
        self._create_top()
        self._create_body()
        self._render_passwords()

    def _create_top(self):
        self.frame_top = tk.Frame(self, bg="white", pady=10)
        self.frame_top.pack(fill="x")

        btn_create = tk.Button(self.frame_top, text="CREATE PASSWORD", command=self._open_create_dialog)
        btn_create.pack(padx=10)
    
    def _create_body(self):
        self.frame_body = tk.Frame(self, bg="white")
        self.frame_body.pack(fill="both", expand=True)

        label_title = tk.Label(self.frame_body, text="YOUR PASSWORDS", bg="white", anchor="w")
        label_title.pack(fill="x", padx=10, pady=10)

    def _render_passwords(self):
        for widget in self.frame_body.winfo_children():
            widget.destroy()

        label_title = tk.Label(self.frame_body, text="YOUR PASSWORDS", bg="white", anchor="w")
        label_title.pack(fill="x", padx=10, pady=10)

        passwords = load_passwords()

        for password in passwords:
            frame_entry = tk.Frame(self.frame_body, bg="white")
            frame_entry.pack(fill="x", padx=10, pady=5)

            tk.Label(frame_entry, text=password["site"], bg="white", font=("Arial", 10, "bold")).pack(anchor="w")
            tk.Label(frame_entry, text=f"login: {password['login']}", bg="white").pack(anchor="w")
            tk.Label(frame_entry, text=f"password: {'•' * 8}", bg="white").pack(anchor="w")
    
    def _open_create_dialog(self):
        CreateDialog(self)