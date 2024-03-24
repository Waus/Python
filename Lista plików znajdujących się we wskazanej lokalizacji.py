import tkinter as tk
from tkinter import messagebox
import os
import pyperclip

try:
    import tkinter as tk
    from tkinter import messagebox
    import pyperclip
except ImportError as e:
    print(f"Błąd podczas importowania modułu: {e.name}. Upewnij się, że jest zainstalowany.")

def kopiuj_pliki_do_schowka_i_zamknij(event=None):
    sciezka = wejscie_pliki.get()
    if os.path.exists(sciezka) and os.path.isdir(sciezka):
        lista_plikow = [plik for plik in os.listdir(sciezka) if os.path.isfile(os.path.join(sciezka, plik))]
        pyperclip.copy("\n".join(lista_plikow))
        messagebox.showinfo("Sukces", "Lista plików została skopiowana do schowka.")
        root.quit()  # Zamknięcie aplikacji po skopiowaniu plików
    else:
        messagebox.showerror("Błąd", "Podana ścieżka jest nieprawidłowa lub nie jest folderem.")

def srodek_okna(okno, szerokosc, wysokosc):
    szerokosc_ekranu = okno.winfo_screenwidth()
    wysokosc_ekranu = okno.winfo_screenheight()

    x = (szerokosc_ekranu - szerokosc) // 2
    y = (wysokosc_ekranu - wysokosc) // 2

    okno.geometry(f"{szerokosc}x{wysokosc}+{x}+{y}")

root = tk.Tk()
root.title("Lista plików do schowka")

srodek_okna(root, 400, 200)

etykieta = tk.Label(root, text="Podaj ścieżkę do folderu:")
etykieta.pack(pady=10)

wejscie_pliki = tk.Entry(root, width=50)
wejscie_pliki.pack()
wejscie_pliki.focus_set()  # Ustawienie fokusu na polu wejściowym

przycisk = tk.Button(root, text="OK", command=kopiuj_pliki_do_schowka_i_zamknij, width=20)
przycisk.pack(pady=10)

# Ustawienie działania przycisku Enter jako zatwierdzenie
root.bind('<Return>', kopiuj_pliki_do_schowka_i_zamknij)

root.mainloop()