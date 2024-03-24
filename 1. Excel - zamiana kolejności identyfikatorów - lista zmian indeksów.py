import tkinter as tk
from tkinter import scrolledtext, messagebox
try:
    import pyperclip
except ImportError:
    messagebox.showerror("Błąd", "Moduł pyperclip nie jest zainstalowany. Zainstaluj go używając 'pip install pyperclip'.")

def generate_mapping(before, after):
    mapping_result = ""
    before_lines = before.strip().split("\n")
    after_lines = after.strip().split("\n")

    # Tworzenie map indeksów dla obu list
    before_mapping = {item: str(index + 1) for index, item in enumerate(before_lines) if item.strip()}
    after_mapping = {item: str(index + 1) for index, item in enumerate(after_lines) if item.strip()}

    # Porównywanie indeksów i generowanie wyniku
    for item, before_index in before_mapping.items():
        after_index = after_mapping.get(item)
        if after_index:
            mapping_result += f"#{before_index} -> #{after_index}\n"
        else:
            mapping_result += f"#{before_index} -> brak odpowiednika\n"

    return mapping_result.strip()

def on_submit():
    before = before_text.get("1.0", tk.END)
    after = after_text.get("1.0", tk.END)
    result = generate_mapping(before, after)
    if result:
        pyperclip.copy(result)
        messagebox.showinfo("Skopiowano", "Wynik został skopiowany do schowka.")
        root.destroy()
    else:
        messagebox.showerror("Błąd", "Nie udało się wygenerować mapowania.")

def main():
    global before_text, after_text, root
    root = tk.Tk()
    root.title("Mapowanie identyfikatorów")

    tk.Label(root, text="Podaj listę identyfikatorów przed zmianą:").pack()
    before_text = scrolledtext.ScrolledText(root, width=60, height=10)
    before_text.pack()

    tk.Label(root, text="Podaj listę identyfikatorów po zmianie:").pack()
    after_text = scrolledtext.ScrolledText(root, width=60, height=10)
    after_text.pack()

    submit_button = tk.Button(root, text="OK", command=on_submit)
    submit_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
    
'''
lista identyfikatorów przed zmianą:
'''  
    
'''
ADRES_APLIKACJI
UŻYTKOWNIK_GŁÓWNY_LOGIN
UŻYTKOWNIK_GŁÓWNY_HASŁO
NAZWA_PLIKU_DO_WGRANIA
USE_END_DATE_NEXT
USE_END_DATE
OPERATOR_ID
NAZWA_POBRANEGO_PLIKU
USE_BEGIN_DATE_NEXT
PLIK_ZBIORCZO_WSZYSTKIE_REKORDY_DO_IMPORTU_ŚCIEŻKA
PLIK_ZBIORCZO_WSZYSTKIE_REKORDY_PO_EKSPORCIE_ŚCIEŻKA
PLIK_50_REKORDÓW_Z_OSTRZEŻENIEM_DO_IMPORTU_ŚCIEŻKA
LISTA_ISTNIEJĄCYCH_USE_ID
LISTA_ISTNIEJĄCYCH_USE_ID_JAKO_STRING
USE_ID
pusta1
pusta2
PLIK_100K_REKORDÓW_DO_IMPORTU_ŚCIEŻKA
PLIK_100K_REKORDÓW_PO_EKSPORCIE_ŚCIEŻKA
PLIK_50_REKORDÓW_Z_OSTRZEŻENIEM_PO_EKSPORCIE_ŚCIEŻKA
PLIK_50_REKORDÓW_Z_OSTRZEŻENIEM_ZAIMPORTOWANE_DO_BAZY_ŚCIEŻKA
PLIK_ZBIORCZO_WSZYSTKIE_REKORDY_ZAIMPORTOWANE_DO_BAZY_OD_RAZU_ŚCIEŻKA
PLIK_ZBIORCZO_WSZYSTKIE_REKORDY_ZAIMPORTOWANE_DO_BAZY_Z_OSTRZEŻENIEM_ŚCIEŻKA
PLIK_1_REKORD_BEZ_BŁĘDÓW_ANI_OSTRZEŻEŃ_DO_IMPORTU_ŚCIEŻKA
PLIK_1_REKORD_BEZ_BŁĘDÓW_ANI_OSTRZEŻEŃ_PO_EKSPORCIE_ŚCIEŻKA
PLIK_1_REKORD_BEZ_BŁĘDÓW_ANI_OSTRZEŻEŃ_ZAIMPORTOWANE_DO_BAZY_OD_RAZU_ŚCIEŻKA
PLIK_1_REKORD_BEZ_BŁĘDÓW_ANI_OSTRZEŻEŃ_ZAIMPORTOWANE_DO_BAZY_Z_OSTRZEŻENIEM_ŚCIEŻKA
'''

'''
lista identyfikatorów po zmianie:
'''

'''
ADRES_APLIKACJI
UŻYTKOWNIK_GŁÓWNY_LOGIN
UŻYTKOWNIK_GŁÓWNY_HASŁO
NAZWA_PLIKU_DO_WGRANIA
USE_END_DATE_NEXT
USE_END_DATE
OPERATOR_ID
NAZWA_POBRANEGO_PLIKU
USE_BEGIN_DATE_NEXT
LISTA_ISTNIEJĄCYCH_USE_ID
LISTA_ISTNIEJĄCYCH_USE_ID_JAKO_STRING
USE_ID
PLIK_ZBIORCZO_WSZYSTKIE_REKORDY_DO_IMPORTU_ŚCIEŻKA
PLIK_ZBIORCZO_WSZYSTKIE_REKORDY_PO_EKSPORCIE_ŚCIEŻKA
PLIK_ZBIORCZO_WSZYSTKIE_REKORDY_ZAIMPORTOWANE_DO_BAZY_OD_RAZU_ŚCIEŻKA
PLIK_ZBIORCZO_WSZYSTKIE_REKORDY_ZAIMPORTOWANE_DO_BAZY_Z_OSTRZEŻENIEM_ŚCIEŻKA
PLIK_50_REKORDÓW_Z_OSTRZEŻENIEM_DO_IMPORTU_ŚCIEŻKA
PLIK_50_REKORDÓW_Z_OSTRZEŻENIEM_PO_EKSPORCIE_ŚCIEŻKA
PLIK_50_REKORDÓW_Z_OSTRZEŻENIEM_ZAIMPORTOWANE_DO_BAZY_ŚCIEŻKA
PLIK_100K_REKORDÓW_DO_IMPORTU_ŚCIEŻKA
PLIK_100K_REKORDÓW_PO_EKSPORCIE_ŚCIEŻKA
PLIK_1_REKORD_BEZ_BŁĘDÓW_ANI_OSTRZEŻEŃ_DO_IMPORTU_ŚCIEŻKA
PLIK_1_REKORD_BEZ_BŁĘDÓW_ANI_OSTRZEŻEŃ_PO_EKSPORCIE_ŚCIEŻKA
PLIK_1_REKORD_BEZ_BŁĘDÓW_ANI_OSTRZEŻEŃ_ZAIMPORTOWANE_DO_BAZY_OD_RAZU_ŚCIEŻKA
PLIK_1_REKORD_BEZ_BŁĘDÓW_ANI_OSTRZEŻEŃ_ZAIMPORTOWANE_DO_BAZY_Z_OSTRZEŻENIEM_ŚCIEŻKA
pusta1
pusta2
'''

'''
otrzymamy wynik:
'''

'''
#1 -> #1
#2 -> #2
#3 -> #3
#4 -> #4
#5 -> #5
#6 -> #6
#7 -> #7
#8 -> #8
#9 -> #9
#10 -> #13
#11 -> #14
#12 -> #17
#13 -> #10
#14 -> #11
#15 -> #12
#16 -> #26
#17 -> #27
#18 -> #20
#19 -> #21
#20 -> #18
#21 -> #19
#22 -> #15
#23 -> #22
#24 -> #24
#25 -> #25
#26 -> #16
#27 -> #17
'''