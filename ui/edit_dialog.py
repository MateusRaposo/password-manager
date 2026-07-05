import tkinter as tk
from core.generator import generate_password
from core.storage import load_passwords, save_passwords

class EditDialog(tk.Toplevel):
    def __init__(self, parent, index, password):
        super().__init__(parent)
        self.title("Edit Password")
        self.geometry("300x400")
        self.resizable(False, False)
        self.parent = parent
        self.index = index
        self.password = password
        self._create_fields()
        self._create_buttons()

    def _create_fields(self):
        tk.Label(self, text="Site:").pack(anchor="w", padx=10, pady=5)
        self.entry_site = tk.Entry(self)
        self.entry_site.pack(fill="x", padx=10)
        self.entry_site.insert(0, self.password["site"])

        tk.Label(self, text="Login:").pack(anchor="w", padx=10, pady=5)
        self.entry_login = tk.Entry(self)
        self.entry_login.pack(fill="x", padx=10)
        self.entry_login.insert(0, self.password["login"])

        tk.Label(self, text="Length:").pack(anchor="w", padx=10, pady=5)
        self.entry_length = tk.Entry(self)
        self.entry_length.pack(fill="x", padx=10)
        self.entry_length.insert(0, "12")

        tk.Label(self, text="Options:").pack(anchor="w", padx=10, pady=5)

        self.var_uppercase = tk.BooleanVar(value=True)
        self.var_numbers = tk.BooleanVar(value=True)
        self.var_symbols = tk.BooleanVar(value=True)

        tk.Checkbutton(self, text="Uppercase", variable=self.var_uppercase).pack(anchor="w", padx=10)
        tk.Checkbutton(self, text="Numbers", variable=self.var_numbers).pack(anchor="w", padx=10)
        tk.Checkbutton(self, text="Symbols", variable=self.var_symbols).pack(anchor="w", padx=10)

    def _create_buttons(self):
        tk.Label(self, text="Generated Password:").pack(anchor="w", padx=10, pady=5)
        self.entry_password = tk.Entry(self)
        self.entry_password.pack(fill="x", padx=10)
        self.entry_password.insert(0, self.password["senha"])

        tk.Button(self, text="GENERATE", command=self._generate).pack(pady=10)
        tk.Button(self, text="SAVE", command=self._save).pack()

    def _generate(self):
        password = generate_password(
            int(self.entry_length.get()),
            self.var_uppercase.get(),
            self.var_numbers.get(),
            self.var_symbols.get()
        )
        self.entry_password.delete(0, tk.END)
        self.entry_password.insert(0, password)

    def _save(self):
        passwords = load_passwords()

        passwords[self.index] = {
            "site": self.entry_site.get(),
            "login": self.entry_login.get(),
            "senha": self.entry_password.get()
        }

        save_passwords(passwords)
        self.parent._render_passwords()
        self.destroy()