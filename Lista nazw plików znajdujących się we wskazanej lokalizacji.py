try:
    import tkinter as tk
    from tkinter import messagebox
    import os
    import pyperclip
except ImportError as e:
    print(f"Błąd podczas importowania modułu: {e.name}. Upewnij się, że jest zainstalowany.")

def copy_files_to_clipboard_and_close(event=None):
    global root
    path = input_files_var.get()
    search_subdirectories = search_subdirectories_var.get()
    auto_close = auto_close_var.get()
    file_list = []
    if os.path.exists(path) and os.path.isdir(path):
        if search_subdirectories:
            for root_dir, dirs, files in os.walk(path):
                for file in files:
                    file_list.append(file)  # Dodawanie tylko nazwy pliku
        else:
            file_list = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
        pyperclip.copy("\n".join(file_list))
        messagebox.showinfo("Sukces", "Lista plików została skopiowana do schowka.")
        if auto_close:
            root.quit()  # Zamknięcie aplikacji po skopiowaniu plików, jeśli zaznaczono opcję
    else:
        messagebox.showerror("Błąd", "Podana ścieżka jest nieprawidłowa lub nie jest folderem.")

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

def bind_undo_redo(entry, var):
    entry.undo_stack = []
    entry.redo_stack = []
    entry.last_value = var.get()  # Przechowuje początkową wartość

    def on_write(*args):
        current_value = var.get()
        if entry.last_value != current_value:
            entry.undo_stack.append(entry.last_value)
            entry.redo_stack.clear()  # Czyść stos redo przy każdej nowej zmianie
            entry.last_value = current_value

    var.trace_add('write', on_write)

    def undo(event):
        if entry.undo_stack:
            entry.redo_stack.append(var.get())  # Zapisz obecną wartość do redo przed cofnięciem
            value = entry.undo_stack.pop()  # Pobierz ostatnią wartość
            entry.last_value = value  # Zapobiegaj dodawaniu wartości do stosu undo podczas cofania
            var.set(value)  # Ustaw wartość bez wywoływania dodatkowego zapisu

    def redo(event):
        if entry.redo_stack:
            entry.undo_stack.append(var.get())  # Zapisz obecną wartość do undo przed redo
            value = entry.redo_stack.pop()  # Pobierz ostatnią wartość
            entry.last_value = value  # Zapobiegaj dodawaniu wartości do stosu redo podczas powtarzania
            var.set(value)  # Ustaw wartość bez wywoływania dodatkowego zapisu

    entry.bind('<Control-z>', undo)
    entry.bind('<Control-y>', redo)

    entry.config(textvariable=var)

root = tk.Tk()
root.title("Lista plików do schowka")

center_window(root, 400, 300)

label = tk.Label(root, text="Podaj ścieżkę do folderu:")
label.pack(pady=10)

input_files_var = tk.StringVar(value=None)
input_files = tk.Entry(root, width=50, textvariable=input_files_var)
input_files.pack()
input_files.focus_set()
bind_undo_redo(input_files, input_files_var)

search_subdirectories_var = tk.BooleanVar(value=False)
checkbox_search_subdirectories = tk.Checkbutton(root, text="Przeszukaj podfoldery", variable=search_subdirectories_var)
checkbox_search_subdirectories.pack()

auto_close_var = tk.BooleanVar(value=True)
checkbox_auto_close = tk.Checkbutton(root, text="Zamknij aplikację po zakończeniu", variable=auto_close_var)
checkbox_auto_close.pack()

button = tk.Button(root, text="OK", command=copy_files_to_clipboard_and_close, width=20)
button.pack(pady=10)

root.bind('<Return>', copy_files_to_clipboard_and_close)

root.mainloop()
