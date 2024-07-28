try:
    import tkinter as tk
    from tkinter import scrolledtext, messagebox, Checkbutton, BooleanVar, Button, Label, StringVar
    import pyperclip
except ImportError as e:
    module_name = str(e).split("'")[1]
    print(f"Proszę zainstalować brakujący moduł: {module_name}")
    print("Użyj: pip install {module_name}")
    exit(1)  # Zakończenie programu, jeśli moduły nie są dostępne

class App:
    def __init__(self, root2):
        self.root = root2
        root.title("Lista wartości")

        # Centrowanie okna
        root_width = 600
        root_height = 450
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (root_width / 2)
        y = (screen_height / 2) - (root_height / 2)
        root.geometry('%dx%d+%d+%d' % (root_width, root_height, x, y))

        self.label = Label(root, text="Wklej listę wartości w nowych liniach")
        self.label.pack()

        self.text = scrolledtext.ScrolledText(root, undo=True, height=10)
        self.text['font'] = ('consolas', '12')
        self.text.pack(expand=True, fill='both', pady=10)

        self.sort_var = BooleanVar()
        self.sort_checkbox = Checkbutton(root, text="Posortowane", variable=self.sort_var)
        self.sort_checkbox.pack()

        self.unique_var = BooleanVar()
        self.unique_checkbox = Checkbutton(root, text="Unikalne i posortowane", variable=self.unique_var)
        self.unique_checkbox.pack()

        self.reverse_var = BooleanVar()
        self.reverse_checkbox = Checkbutton(root, text="W odwróconej kolejności", variable=self.reverse_var)
        self.reverse_checkbox.pack()

        self.auto_close_var = BooleanVar(value=True)
        self.checkbox_auto_close = tk.Checkbutton(root, text="Zamknij aplikację po zakończeniu", variable=self.auto_close_var)
        self.checkbox_auto_close.pack()

        self.ok_button = Button(root, text='OK', command=self.process_data, height=2, width=20)
        self.ok_button.pack(pady=10)

    def process_data(self):
        content = self.text.get('1.0', tk.END)
        lines = content.split('\n')
        try:
            numbers = [int(line) for line in lines if line.strip() != '']
            if self.unique_var.get():
                numbers = sorted(list(set(numbers)))  # Usuwa duplikaty i sortuje
            elif self.sort_var.get():
                numbers = sorted(numbers)  # Sortuje wartości
            if self.reverse_var.get(): # Wypisuje od tyłu
                numbers.reverse()

            count = len(numbers)

            pyperclip.copy(', '.join(map(str, numbers)))
            messagebox.showinfo("Wynik", f"Lista wartości została skopiowana do schowka. Liczba wartości: {count}")
            if self.auto_close_var.get():
                self.root.quit()  # Zamknięcie aplikacji po skopiowaniu plików, jeśli zaznaczono opcję

        except ValueError:
            messagebox.showerror("Błąd", "Upewnij się, że wszystkie wprowadzone wartości są liczbami całkowitymi.")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()