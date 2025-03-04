import tkinter as tk
from tkinter import messagebox

def main_window():
    root = tk.Tk()
    root.title("Inventory Management")
    
    label = tk.Label(root, text="Welcome to Inventory App", font=("Arial", 14))
    label.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main_window()
