import ctypes
import os
import tkinter as tk
from tkinter import messagebox

# Define constants from the Windows API
SHERB_NOCONFIRMATION = 0x00000001  # No confirmation dialog
SHERB_NOPROGRESSUI = 0x00000002    # No progress UI
SHERB_NOSOUND = 0x00000004         # No sound

# Empty Recycle Bin function using ctypes to call the Windows API
def empty_recycle_bin():
    try:
        # SHEmptyRecycleBinA is the function from the Windows API
        ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, SHERB_NOCONFIRMATION | SHERB_NOPROGRESSUI | SHERB_NOSOUND)
        print("Recycle Bin emptied successfully.")
        messagebox.showinfo("Success", "Recycle Bin emptied successfully!")
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Failed to empty Recycle Bin. Error: {e}")

# Function to show confirmation dialog
def confirm_and_empty():
    result = messagebox.askyesno("Confirm", "Do you want to empty the Recycle Bin?")
    if result:  # If user clicks 'Yes'
        empty_recycle_bin()
    else:
        print("Recycle Bin cleaning canceled.")

# Create the tkinter window to show the popup
def create_popup():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    confirm_and_empty()
    root.mainloop()

if __name__ == "__main__":
    create_popup()
