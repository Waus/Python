import os

# Zdefiniowanie katalogu z plikami - zmień na odpowiednią ścieżkę
directory = r'C:\Users\muranski\OneDrive - SFP-ZAPA\Pulpit\Testy - Import użyć ZAPA-10193\Aktualizacje użyć kwotowych\Aktualizacje z błędami'

# Zdefiniowanie wartości, o którą zwiększamy lub zmniejszamy
increase_or_decrease_by = -1 
    
if not os.path.exists(directory):
    print(f"Katalog {directory} nie istnieje.")
else:
    print(f"Przeszukiwanie katalogu: {directory}")

    files_found = False

    # Przechodzenie przez wszystkie pliki w katalogu
    for filename in os.listdir(directory):
        if filename.startswith("Aktualizacja użyć z błędem "):
            files_found = True
            print(f"Znaleziono plik: {filename}")
            # Rozdzielenie nazwy pliku na części
            parts = filename.split(' - ')
            first_part = parts[0]
            # Znalezienie numeru w nazwie i zwiększenie go o 13
            number = int(first_part.split(' ')[-1])
            updated_number = number + increase_or_decrease_by
            # Tworzenie nowej nazwy pliku
            new_filename = first_part.replace(str(number), str(updated_number)) + ' - ' + ' - '.join(parts[1:])
            # Pełna ścieżka starych i nowych plików
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            # Zmiana nazwy pliku
            os.rename(old_file, new_file)
            print(f"Zmieniono nazwę {filename} na {new_filename}")
        
    if not files_found:
        print("Nie znaleziono plików do zmiany.")

# Czekaj na wprowadzenie danych przez użytkownika przed zamknięciem
input("Naciśnij Enter, aby zamknąć...")