import os
import tkinter as tk
from tkinter import messagebox

def rename_folders():
    try:
        folder_path = folder_path_entry.get()
        old_names = old_names_entry.get("1.0", tk.END).splitlines()
        new_names = new_names_entry.get("1.0", tk.END).splitlines()

        if len(old_names) != len(new_names):
            raise ValueError("Liczba starych nazw nie zgadza się z liczbą nowych nazw.")

        for old_name, new_name in zip(old_names, new_names):
            old_path = os.path.join(folder_path, old_name)
            new_path = os.path.join(folder_path, new_name)
            if os.path.exists(old_path):
                os.rename(old_path, new_path)

        messagebox.showinfo("Sukces", "Nazwy folderów zostały zmienione.")
        root.destroy()

    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd: {e}")

root = tk.Tk()
root.title("Zmiana Nazw Folderów")

folder_path_label = tk.Label(root, text="Ścieżka do folderu:")
folder_path_label.grid(row=0, column=0, padx=10, pady=10)

folder_path_entry = tk.Entry(root, width=50)
folder_path_entry.grid(row=0, column=1, padx=10, pady=10)

old_names_label = tk.Label(root, text="Stare nazwy folderów:")
old_names_label.grid(row=1, column=0, padx=10, pady=10)

old_names_entry = tk.Text(root, width=50, height=10)
old_names_entry.grid(row=1, column=1, padx=10, pady=10)

new_names_label = tk.Label(root, text="Nowe nazwy folderów:")
new_names_label.grid(row=2, column=0, padx=10, pady=10)

new_names_entry = tk.Text(root, width=50, height=10)
new_names_entry.grid(row=2, column=1, padx=10, pady=10)

ok_button = tk.Button(root, text="OK", width=20, height=2, command=rename_folders)
ok_button.grid(row=3, columnspan=2, padx=10, pady=10)

# Automatyczne dostosowanie rozmiaru okna i wyśrodkowanie go na ekranie
root.update()  # Aktualizacja root, aby uzyskać dokładne wymiary
width = root.winfo_width()
height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

root.mainloop()
