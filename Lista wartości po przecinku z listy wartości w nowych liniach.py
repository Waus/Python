try:
    import tkinter as tk
    from tkinter import scrolledtext, messagebox, Checkbutton
    import pyperclip
except ImportError as e:
    module_name = str(e).split("'")[1]
    print(f"Proszę zainstalować brakujący moduł: {module_name}")
    print("Użyj: pip install {module_name}")
else:
    class App:
        def __init__(self, root):
            self.root = root
            root.title("Lista wartości")

            # Centrowanie okna
            root_width = 600
            root_height = 450
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width / 2) - (root_width / 2)
            y = (screen_height / 2) - (root_height / 2)
            root.geometry('%dx%d+%d+%d' % (root_width, root_height, x, y))

            self.label = tk.Label(root, text="Wklej listę wartości w nowych liniach")
            self.label.pack()

            self.txt = scrolledtext.ScrolledText(root, undo=True, height=10)
            self.txt['font'] = ('consolas', '12')
            self.txt.pack(expand=True, fill='both', pady=10)

            # Checkboxes
            self.sort_var = tk.BooleanVar()
            self.unique_var = tk.BooleanVar()
            self.sort_checkbox = Checkbutton(root, text="Posortowane", variable=self.sort_var)
            self.sort_checkbox.pack()
            self.unique_checkbox = Checkbutton(root, text="Unikalne i posortowane", variable=self.unique_var)
            self.unique_checkbox.pack()

            self.ok_button = tk.Button(root, text='OK', command=self.process_data, height=2, width=20)
            self.ok_button.pack(pady=10)

        def process_data(self):
            content = self.txt.get('1.0', tk.END)
            lines = content.split('\n')
            try:
                numbers = [int(line) for line in lines if line.strip() != '']
                if self.unique_var.get():
                    numbers = list(set(numbers))  # Usuwa duplikaty
                if self.sort_var.get():
                    numbers = sorted(numbers)  # Sortuje wartości

                count = len(numbers)

                pyperclip.copy(', '.join(map(str, numbers)))
                messagebox.showinfo("Wynik", f"Lista wartości została skopiowana do schowka. Liczba wartości: {count}")
                self.root.destroy()

            except ValueError:
                messagebox.showerror("Błąd", "Upewnij się, że wszystkie wprowadzone wartości są liczbami całkowitymi.")

    if __name__ == "__main__":
        root = tk.Tk()
        app = App(root)
        root.mainloop()