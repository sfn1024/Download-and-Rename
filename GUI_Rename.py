import os
import tkinter as tk
from tkinter import filedialog, messagebox

def change_file_names():
    folder_path = entry.get()
    new_name = entry2.get()
    os.chdir(folder_path)
    i = 1
    for file in os.listdir():
        src = file
        dst = f"{new_name}{i}.png"
        os.rename(src, dst)
        i += 1
    messagebox.showinfo("Success", "Rename completed!")

root = tk.Tk()

label1 = tk.Label(root, text="Enter folder path:")
label1.grid(row=0, column=0)

entry = tk.Entry(root)
entry.grid(row=0, column=1)

label2 = tk.Label(root, text="Enter new name:")
label2.grid(row=1, column=0)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

button = tk.Button(root, text="Change file names", command=change_file_names)
button.grid(row=2, column=1)

root.mainloop()
