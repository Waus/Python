import tkinter as tk
import pyperclip
import os
from tkinter import messagebox

def copy_folder_names():
    try:
        folder_path = folder_entry.get()
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            folder_names = [name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))]
            folder_names_str = '\n'.join(folder_names)
            pyperclip.copy(folder_names_str)
            messagebox.showinfo("Sukces", "Nazwy folderów zostały skopiowane do schowka.")
            root.destroy()
        else:
            raise FileNotFoundError("Podana ścieżka nie jest poprawnym katalogiem.")
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd: {e}")

try:
    import tkinter as tk
    import pyperclip
    import os
    from tkinter import messagebox
except ImportError as e:
    print("Błąd importu modułu:", e)
    exit()

root = tk.Tk()
root.title("Kopiowanie Nazw Folderów")

# Obliczanie pozycji, aby wyśrodkować okno
window_width = 350
window_height = 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)

root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

folder_label = tk.Label(root, text="Wprowadź ścieżkę do folderu:")
folder_label.pack()

folder_entry = tk.Entry(root, width=50)
folder_entry.pack()

ok_button = tk.Button(root, text="OK", width=15, height=2, command=copy_folder_names)
ok_button.pack()

root.mainloop()
