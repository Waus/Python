import ctypes
import time
import subprocess

ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

# Funkcja do zapobiegania uśpieniu systemu
def prevent_sleep():
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED)

# Funkcja do symulacji ruchu myszki
def move_mouse():
    ctypes.windll.user32.mouse_event(0x0001, 1, 0, 0, 0)  # Przesunięcie myszki o 1 piksel w prawo
    time.sleep(0.1)
    ctypes.windll.user32.mouse_event(0x0001, -1, 0, 0, 0)  # Przesunięcie myszki o 1 piksel w lewo

# Uruchomienie polecenia ping i przekierowanie jego wyjścia do głównego okna konsoli
ping_process = subprocess.Popen(['ping', '8.8.8.8', '-t'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

while True:
    prevent_sleep()
    move_mouse()
    # Odczytywanie i wyświetlanie wyjścia z polecenia ping
    output = ping_process.stdout.readline()
    if output:
        print(output.strip())
    time.sleep(1)  # Czekaj 1 sekundę, aby zapobiec nadmiernemu obciążeniu CPU