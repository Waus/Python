try:
    import os
    import json
    import tkinter as tk
    import tkinter.messagebox as messagebox
except ImportError as e:
    module_name = str(e).split("'")[1]
    print(f"Proszę zainstalować brakujący moduł: {module_name}")
    print("Użyj: pip install {module_name}")
    exit(1)  # Zakończenie programu, jeśli moduły nie są dostępne

# Ścieżka do pliku z ustawieniami
settings_file = os.path.join(os.path.expanduser('~'), 'Zmiana numerów w nazwach plików.settings.json')

def save_settings():
    settings = {
        'directory': directory_var.get(),
        'starts_with': starts_with_var.get(),
        'increase_or_decrease_by': int(increase_or_decrease_by_var.get())
    }
    try:
        with open(settings_file, 'w') as file:
            json.dump(settings, file)
    except PermissionError:
        print("Brak uprawnień do zapisu w lokalizacji pliku.")
    except Exception as e:
        print(f"Błąd podczas zapisu ustawień: {e}")

def load_settings():
    try:
        with open(settings_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            'directory': '',
            'starts_with': '',
            'increase_or_decrease_by': 0
        }

def rename_files(operation):
    directory = directory_var.get()
    starts_with = starts_with_var.get()
    try:
        modify_value = int(increase_or_decrease_by_var.get())
    except ValueError:
        messagebox.showerror("Błąd", "Wartość do zmiany musi być liczbą.")
        return

    if operation == 'subtract':
        modify_value = -modify_value

    if not os.path.exists(directory):
        messagebox.showerror("Błąd", f"Katalog {directory} nie istnieje.")
        return

    print(f"Przeszukiwanie katalogu: {directory}")
    files_found = False

    for filename in os.listdir(directory):
        if filename.startswith(starts_with):
            files_found = True
            parts = filename.split(' - ', 1)
            if len(parts) > 1:
                first_part, rest = parts
                number_index = first_part.rfind(' ')
                if number_index != -1:
                    number_part = first_part[number_index + 1:]
                    try:
                        number = int(number_part)
                        updated_number = number + modify_value

                        if updated_number < 0 or updated_number > 99:
                            continue

                        updated_number_str = f"{updated_number:02}"
                        new_first_part = first_part[:number_index + 1] + updated_number_str
                        new_filename = new_first_part + ' - ' + rest
                        old_file = os.path.join(directory, filename)
                        new_file = os.path.join(directory, new_filename)
                        os.rename(old_file, new_file)
                        print(f"Zmieniono nazwę {filename} na {new_filename}")
                    except ValueError:
                        continue  # Przechodzi do kolejnego pliku jeśli konwersja nie powiodła się

    if not files_found:
        messagebox.showinfo("Informacja", "Nie znaleziono plików do zmiany.")

def center_window(root, width=600, height=300):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry(f'{width}x{height}+{x}+{y}')

root = tk.Tk()
root.title("Zmiana numerów w nazwach plików")
center_window(root)

settings = load_settings()

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



def setup_validation(entry_widget):
    def only_digits(char):
        return char.isdigit()  # Zwraca True tylko jeśli char jest cyfrą   
    validate_cmd = entry_widget.register(only_digits)  # Rejestruje funkcję walidacji
    entry_widget.config(validate="key", validatecommand=(validate_cmd, '%S'))  # Ustawia walidację na wpisywanie (key) i przekazuje tylko wpisywany znak ('%S')


# Tworzenie StringVar i przypisanie do Entry
directory_var = tk.StringVar(value=settings.get('directory', ''))
directory_entry = tk.Entry(root, width=50, textvariable=directory_var)
directory_entry.grid(row=0, column=1, padx=10, pady=10)
bind_undo_redo(directory_entry, directory_var)

starts_with_var = tk.StringVar(value=settings.get('starts_with', ''))
starts_with_entry = tk.Entry(root, width=50, textvariable=starts_with_var)
starts_with_entry.grid(row=1, column=1, padx=10, pady=10)
bind_undo_redo(starts_with_entry, starts_with_var)

increase_or_decrease_by_var = tk.StringVar(value=str(settings.get('increase_or_decrease_by', 0)))
increase_or_decrease_by_entry = tk.Entry(root, width=50, textvariable=increase_or_decrease_by_var)
increase_or_decrease_by_entry.grid(row=2, column=1, padx=10, pady=10)
bind_undo_redo(increase_or_decrease_by_entry, increase_or_decrease_by_var)
setup_validation(increase_or_decrease_by_entry)

tk.Label(root, text="Katalog:").grid(row=0, column=0, sticky=tk.W)
tk.Label(root, text="Początek nazwy pliku:").grid(row=1, column=0, sticky=tk.W)
tk.Label(root, text="Zwiększ/zmniejsz o:").grid(row=2, column=0, sticky=tk.W)

tk.Button(root, text="Dodaj", width=20, command=lambda: rename_files('add')).grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
tk.Button(root, text="Odejmij", width=20, command=lambda: rename_files('subtract')).grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)
tk.Button(root, text="Zapisz", width=20, command=save_settings).grid(row=3, column=1, padx=10, pady=10, sticky=tk.E)

root.mainloop()