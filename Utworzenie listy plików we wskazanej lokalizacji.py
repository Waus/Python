import tkinter as tk
from tkinter import messagebox, scrolledtext
import os

def create_files():
    path = input_path.get()
    file_names = input_file_names.get("1.0", tk.END).splitlines()
    
    if not os.path.exists(path) or not os.path.isdir(path):
        messagebox.showerror("Błąd", "Podana ścieżka jest nieprawidłowa lub nie jest folderem.")
        return
    
    all_files_created = True

    for file_name in file_names:
        if file_name:  # Pomijamy puste linie
            full_path = os.path.join(path, file_name)
            if not os.path.exists(full_path):
                with open(full_path, 'w') as file:
                    file.write('')  # Tworzymy pusty plik
            else:
                all_files_created = False
                messagebox.showwarning("Ostrzeżenie", f"Plik {file_name} już istnieje.")
    
    if all_files_created:
        messagebox.showinfo("Sukces", "Wszystkie pliki zostały utworzone.")
    else:
        messagebox.showinfo("Informacja", "Niektóre pliki mogły nie zostać utworzone, ponieważ już istnieją.")

def center_window(window, width, height):
										   
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk()
root.title("Tworzenie Plików")

center_window(root, 400, 300)

tk.Label(root, text="Podaj ścieżkę do folderu:").pack(pady=10)

input_path = tk.Entry(root, width=50)
input_path.pack()
input_path.focus_set()

tk.Label(root, text="Wprowadź nazwy plików (każda w nowej linii):").pack(pady=10)

input_file_names = scrolledtext.ScrolledText(root, height=10)
input_file_names.pack()

button = tk.Button(root, text="Utwórz Pliki", command=create_files, width=20)
button.pack(pady=10)

root.mainloop()