import tkinter as tk
from core.storage import load_passwords
from ui.create_dialog import CreateDialog
from core.storage import load_passwords, save_passwords

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

        for index, password in enumerate(passwords):
            frame_entry = tk.Frame(self.frame_body, bg="white")
            frame_entry.pack(fill="x", padx=10, pady=5)

            tk.Label(frame_entry, text=password["site"], bg="white", font=("Arial", 10, "bold")).pack(anchor="w")
            tk.Label(frame_entry, text=f"login: {password['login']}", bg="white").pack(anchor="w")
            frame_password = tk.Frame(frame_entry, bg="white")
            frame_password.pack(fill="x", anchor="w")
            tk.Label(frame_password, text=f"password: {'•' * 8}", bg="white").pack(side="left")
            tk.Button(frame_password, text="COPY", command=lambda p=password["senha"]: self._copy_password(p)).pack(side="left", padx=5)
            tk.Button(frame_password, text="DELETE", command=lambda i=index: self._delete_password(i)).pack(side="left", padx=5)

    def _open_create_dialog(self):
        CreateDialog(self)
    
    def _copy_password(self, password):
        self.clipboard_clear()
        self.clipboard_append(password)

    def _delete_password(self, index):
        passwords = load_passwords()
        passwords.pop(index)
        save_passwords(passwords)
        self._render_passwords()