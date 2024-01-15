import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pygoogle_image import image as pi

class ImageOperationsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Operations")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        self.current_frame = None

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=20)

        self.download_button = tk.Button(self.main_frame, text="Download Images", command=self.show_download_frame)
        self.download_button.pack(pady=10)

        self.rename_button = tk.Button(self.main_frame, text="Rename Images", command=self.show_rename_frame)
        self.rename_button.pack(pady=10)

    def show_download_frame(self):
        if self.current_frame:
            self.current_frame.pack_forget()

        self.download_frame = tk.Frame(self.root)
        self.download_frame.pack(pady=20)

        label1 = tk.Label(self.download_frame, text="Enter search terms (separated by commas):")
        label1.pack(pady=5)

        self.entry1 = tk.Entry(self.download_frame, width=30)
        self.entry1.pack(pady=5)

        label2 = tk.Label(self.download_frame, text="Enter number of images:")
        label2.pack(pady=5)

        self.entry2 = tk.Entry(self.download_frame)
        self.entry2.pack(pady=5)

        button_download_action = tk.Button(self.download_frame, text="Download", command=self.download_images)
        button_download_action.pack(pady=20)

        back_button = tk.Button(self.download_frame, text="Back", command=self.show_main_frame)
        back_button.pack(pady=10)

        self.current_frame = self.download_frame

    def download_images(self):
        search_terms = self.entry1.get().split(',')
        num_images = int(self.entry2.get())
        download_path = filedialog.askdirectory()
        os.chdir(download_path)

        for search_term in search_terms:
            pi.download(search_term.strip(), limit=num_images)

        messagebox.showinfo("Success", "Download completed!")
        self.show_main_frame()

    def show_rename_frame(self):
        if self.current_frame:
            self.current_frame.pack_forget()

        self.rename_frame = tk.Frame(self.root)
        self.rename_frame.pack(pady=20)

        label3 = tk.Label(self.rename_frame, text="Enter folder path:")
        label3.pack(pady=5)

        self.entry3 = tk.Entry(self.rename_frame, width=30)
        self.entry3.pack(pady=5)

        label4 = tk.Label(self.rename_frame, text="Enter new name:")
        label4.pack(pady=5)

        self.entry4 = tk.Entry(self.rename_frame)
        self.entry4.pack(pady=5)

        button_rename_action = tk.Button(self.rename_frame, text="Rename", command=self.change_file_names)
        button_rename_action.pack(pady=20)

        back_button = tk.Button(self.rename_frame, text="Back", command=self.show_main_frame)
        back_button.pack(pady=10)

        self.current_frame = self.rename_frame

    def change_file_names(self):
        folder_path = self.entry3.get()
        new_name = self.entry4.get()
        os.chdir(folder_path)
        i = 1
        for file in os.listdir():
            src = file
            dst = f"{new_name}{i}.png"
            os.rename(src, dst)
            i += 1
        messagebox.showinfo("Success", "Rename completed!")
        self.show_main_frame()

    def show_main_frame(self):
        if self.current_frame:
            self.current_frame.pack_forget()

        self.main_frame.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageOperationsApp(root)
    root.mainloop()
