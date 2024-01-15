import os
import tkinter as tk
from tkinter import filedialog
from pygoogle_image import image as pi

def download_images():
    search_terms = entry.get().split(',')
    num_images = int(entry2.get())
    download_path = filedialog.askdirectory()
    os.chdir(download_path) # Change the path to the user-selected directory
    
    for search_term in search_terms:
        pi.download(search_term.strip(), limit=num_images) # Download the images

window = tk.Tk()
window.title("Download Images")

label = tk.Label(window, text="Enter search terms (separated by commas):")
label.pack()

entry = tk.Entry(window, width=50)
entry.pack()

label2 = tk.Label(window, text="Enter number of images:")
label2.pack()

entry2 = tk.Entry(window)
entry2.pack()

button = tk.Button(window, text="Download", command=download_images)
button.pack()

window.mainloop()
