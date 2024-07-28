import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import openpyxl

# Globalna zmienna do przechowywania skoroszytu
global_wb = None																														

def save_workbook(wb, filename):
    try:
        wb.save(filename)
        messagebox.showinfo("Sukces", "Plik zapisany pomyślnie!")
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie można zapisać pliku: {e}")

def perform_replacement(wb, mappings):
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for cell in row:
                if cell.value:
                    original_value = str(cell.value)
                    for old, new in mappings:
                        old2 = '"'+old+'"'
                        xxxold = '"XXX'+old+'"'
                        if old in original_value:
                            cell.value = original_value.replace(old2, xxxold)
            for cell in row:
                if cell.value:
                    original_value = str(cell.value)
                    for old, new in mappings:
                        new2 = '"'+new+'"'
                        xxxold = '"XXX'+old+'"'
                        if xxxold in original_value:
                            cell.value = original_value.replace(xxxold, new2)


def select_file():
    global global_wb
    filename = filedialog.askopenfilename()
    try:
        global_wb = openpyxl.load_workbook(filename)
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się załadować pliku: {e}")
        return None

    messagebox.showinfo("Sukces", f"Załadowano plik: {filename}")

def on_submit():
    global global_wb
    if not global_wb:
        messagebox.showerror("Błąd", "Brak załadowanego pliku. Proszę wybrać plik.")
        return

    before = before_text.get("1.0", tk.END)
    after = after_text.get("1.0", tk.END)
    mapping_str = generate_mapping(before, after)

    if not mapping_str:
        messagebox.showerror("Błąd", "Nie udało się wygenerować mapowania.")
        return

    mappings = [line.strip().split(" -> ") for line in mapping_str.split("\n") if " -> " in line and len(line.strip().split(" -> ")) == 2]
    
    perform_replacement(global_wb, mappings)
    
    save_filename = filedialog.asksaveasfilename(defaultextension=".xlsx")
    if save_filename:
        save_workbook(global_wb, save_filename)

def generate_mapping(before, after):
    mapping_result = ""
    before_lines = before.strip().split("\n")
    after_lines = after.strip().split("\n")

										  
    before_mapping = {item: str(index + 1) for index, item in enumerate(before_lines) if item.strip()}
    after_mapping = {item: str(index + 1) for index, item in enumerate(after_lines) if item.strip()}

												  
    for item, before_index in before_mapping.items():
        after_index = after_mapping.get(item)
        if after_index:
            mapping_result += f"#{before_index} -> #{after_index}\n"
        else:
            mapping_result += f"#{before_index} -> brak odpowiednika\n"

    return mapping_result.strip()

def center_window(root):
    root.update_idletasks()
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width - window_width) / 2)
    y = int((screen_height - window_height) / 2)
    root.geometry(f'+{x}+{y}')

def main():
    global before_text, after_text, root
    root = tk.Tk()
    root.title("Zamiana odwołań w Excelu po zamianie kolejności w spisie treści")

    tk.Label(root, text="Podaj listę identyfikatorów przed zmianą:").pack()
    before_text = scrolledtext.ScrolledText(root, width=60, height=10)
    before_text.pack()

    tk.Label(root, text="Podaj listę identyfikatorów po zmianie:").pack()
    after_text = scrolledtext.ScrolledText(root, width=60, height=10)
    after_text.pack()

    select_file_button = tk.Button(root, text="Wybierz plik", command=select_file)
    select_file_button.pack()

    submit_button = tk.Button(root, text="Zapisz plik po zmianach", command=on_submit)
    submit_button.pack()

    center_window(root)

    root.mainloop()

if __name__ == "__main__":
    main()
