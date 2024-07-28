import tkinter as tk
from tkinter import messagebox
import pyperclip

# Sprawdzenie, czy moduł pyperclip jest zainstalowany
try:
    import pyperclip
except ImportError:
    raise ImportError("Moduł 'pyperclip' nie jest zainstalowany. Zainstaluj go używając 'pip install pyperclip'")

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.title("Alternating List Merger")

        # Ustawienie rozmiaru i pozycji okna
        window_width = 500
        window_height = 300
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        # Tworzenie pól tekstowych
        self.text_area1 = tk.Text(self, height=10, width=25)
        self.text_area1.grid(row=0, column=0, padx=10, pady=10)
        self.text_area2 = tk.Text(self, height=10, width=25)
        self.text_area2.grid(row=0, column=1, padx=10, pady=10)

        # Przycisk OK
        ok_button = tk.Button(self, text="OK", command=self.merge_lists, height=2, width=10)
        ok_button.grid(row=1, column=0, columnspan=2, pady=10)

    def merge_lists(self):
        # Pobranie danych z pól tekstowych i konwersja na listy
        list1 = self.text_area1.get("1.0", "end-1c").split("\n")
        list2 = self.text_area2.get("1.0", "end-1c").split("\n")

        # Mieszanie list
        mixed_list = [val for pair in zip(list1, list2) for val in pair if val]

        # Przygotowanie wyniku do skopiowania do schowka
        result = ', '.join(mixed_list)

        # Kopiowanie wyniku do schowka
        pyperclip.copy(result)

        # Wyświetlenie komunikatu o sukcesie
        messagebox.showinfo("Sukces", f"Łączna liczba wartości: {len(mixed_list)}\nWynik został skopiowany do schowka.")
        self.destroy()

# Uruchomienie aplikacji 
if __name__ == "__main__":
    app = Application()
    app.mainloop()