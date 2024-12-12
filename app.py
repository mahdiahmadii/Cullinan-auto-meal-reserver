import os
import subprocess
import kalinan
import setup
import tkinter as tk
from tkinter import messagebox

def check_env_file():
    """Check if .env file exists in the current directory."""
    return os.path.exists(".env")

def run_setup():
    """Run the setup.py script."""
    setup.main()

def run_kalinan():
    """Run the kalinan.py script."""
    kalinan.main_def()



def ask_to_reserve_food():
    def yes():
        root.destroy()
        main()

    def no():
        root.destroy()
        print("Exiting application.")

    root = tk.Tk()
    root.title("Food Reservation")
    root.geometry("400x200")  # Set the window size to 400x200 pixels

    label = tk.Label(root, text="Do you want to reserve food?", font=("Arial", 24))  # Increase the font size
    label.pack(pady=50)  # Add some padding around the label

    frame = tk.Frame(root)
    frame.pack(pady=20)  # Add some padding around the frame

    yes_button = tk.Button(frame, text="Yes", command=yes, font=("Arial", 18), width=10, height=2)  # Increase the font size and button size
    yes_button.pack(side=tk.LEFT, padx=20)  # Add some padding around the button

    no_button = tk.Button(frame, text="No", command=no, font=("Arial", 18), width=10, height=2)  # Increase the font size and button size
    no_button.pack(side=tk.LEFT, padx=20)  # Add some padding around the button

    root.mainloop()
    
    
def main():
    if check_env_file():
        print(".env file found. Running kalinan.py...")
        run_kalinan()
    else:
        print(".env file not found. Running setup.py...")
        run_setup()
        print("Setup complete.")
        ask_to_reserve_food()
        

if __name__ == "__main__":
    main()