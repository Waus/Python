try:
    import tkinter as tk
    from tkinter import messagebox, scrolledtext
    import pyperclip
except ImportError as e:
    print(f"Błąd podczas importowania modułów: {e}")
    exit(1)

def generate_order_by(values):
    cleaned_values = [value.strip() for value in values if value.strip()]
    values_string = ', '.join(cleaned_values)
    column_name = id_column_var.get() 
    where_and_order_by_clause = f"WHERE {column_name} IN ({values_string})\n"
    where_and_order_by_clause += f"ORDER BY \n   CASE {column_name}\n"
    for index, value in enumerate(values, start=1):
        where_and_order_by_clause += f"       WHEN {value.strip()} THEN {index}\n"
    where_and_order_by_clause += "   END;"
    return where_and_order_by_clause

def on_ok():
    auto_close = auto_close_var.get()
    input_values = text_input.get('1.0', tk.END).split(',')
    order_by_clause = generate_order_by(input_values)
    pyperclip.copy(order_by_clause)
    messagebox.showinfo("Sukces", "ORDER BY zostało skopiowane do schowka.")
    if auto_close:
            root.quit()

def center_window(root):
    root.update_idletasks()
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width - window_width) / 2)
    y = int((screen_height - window_height) / 2)
    root.geometry(f'+{x}+{y}')

root = tk.Tk()
root.title("Generator ORDER BY")

center_window(root)

label = tk.Label(root, text="Wklej listę ID oddzielonych przecinkami")
label.pack(pady=10)

text_input = scrolledtext.ScrolledText(root, width=40, height=10)
text_input.pack(pady=10)

label = tk.Label(root, text="Podaj nazwę kolumny z ID")
label.pack(pady=10)

id_column_var = tk.StringVar()
id_column_entry = tk.Entry(root, width=50, textvariable=id_column_var)
id_column_entry.pack(pady=10)

auto_close_var = tk.BooleanVar(value=True)
checkbox_auto_close = tk.Checkbutton(root, text="Zamknij aplikację po zakończeniu", variable=auto_close_var)
checkbox_auto_close.pack()

ok_button = tk.Button(root, text="OK", command=on_ok, height=2, width=10)
ok_button.pack(pady=10)

root.mainloop()