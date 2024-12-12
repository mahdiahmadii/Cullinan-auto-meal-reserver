import os
import tkinter as tk
from tkinter import messagebox

class KalinanCredentialsGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Kalinan Credentials GUI")

        # Create labels and entry fields
        tk.Label(self.window, text="Kalinan Username (Student Number):").grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = tk.Entry(self.window, width=30)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.window, text="Kalinan Password:").grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(self.window, width=30, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Create button to create .env file
        tk.Button(self.window, text="Create .env File", command=self.create_env_file).grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def create_env_file(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password.")
            return

        env_file_path = ".env"
        with open(env_file_path, "w") as file:
            file.write(f"STUDENT_NUMBER={username}\n")
            file.write(f"PASSWORD_KALINAN={password}\n")

        messagebox.showinfo("Success", f".env file created at {os.path.abspath(env_file_path)}")
        self.window.destroy()  # Close the Tk window

    def run(self):
        self.window.mainloop()

def main():
    gui = KalinanCredentialsGUI()
    gui.run()
if __name__ == "__main__":
    main()