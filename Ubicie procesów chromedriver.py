import os
import signal

# Sprawdzenie, czy psutil jest zainstalowane
try:
    import psutil
except ImportError:
    print("Biblioteka 'psutil' nie jest zainstalowana. Zainstaluj ją poleceniem: pip install psutil")
    input("Naciśnij Enter, aby zamknąć...")
    exit(1)  # Zakończenie programu z kodem błędu

# Funkcja, która ubija procesy o danej nazwie
def kill_process_by_name(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            try:
                os.kill(proc.info['pid'], signal.SIGTERM)
                print(f"Zakończono proces: {proc.info['name']} (PID: {proc.info['pid']})")
            except Exception as e:
                print(f"Nie udało się zakończyć procesu: {proc.info['name']} (PID: {proc.info['pid']}). Błąd: {e}")

# Ubijanie procesu chromedriver.exe
kill_process_by_name("chromedriver.exe")

# Zatrzymanie programu przed zamknięciem
input("Naciśnij Enter, aby zamknąć...")
