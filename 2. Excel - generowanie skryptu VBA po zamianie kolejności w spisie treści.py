import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_vba():
    mapping_str = text_area.get("1.0", tk.END)
    mappings = [line.strip().split(" -> ") for line in mapping_str.split("\n") if " -> " in line and len(line.strip().split(" -> ")) == 2]
    vba_code = "Sub ZmienTekst()\n    Dim ws As Worksheet\n\n    For Each ws In ThisWorkbook.Sheets\n"
    
    # Pierwsza seria zamian: "#1" na "#0001", "#2" na "#0002", itd.
    vba_code += "        ' Pierwsza seria zamian: \"#1\" na \"#0001\", \"#2\" na \"#0002\", itd.\n"
    for old, new in mappings:
        search = f'"""{old}"""'
        replace = f'"""XXX{old[1:]}"""'
        vba_code += f"        ws.Cells.Replace What:={search}, Replacement:={replace}, LookAt:=xlPart, _\n        SearchOrder:=xlByRows, MatchCase:=False, SearchFormat:=False, _\n        ReplaceFormat:=False\n"

    # Druga seria zamian: konkretnie określone zmiany
    vba_code += "        ' Druga seria zamian: konkretnie określone zmiany\n"
    for old, new in mappings:
        search = f'"""XXX{old[1:]}"""'
        replace = f'"""{new}"""'
        vba_code += f"        ws.Cells.Replace What:={search}, Replacement:={replace}, LookAt:=xlPart, _\n        SearchOrder:=xlByRows, MatchCase:=False, SearchFormat:=False, _\n        ReplaceFormat:=False\n"

    vba_code += "    Next ws\nEnd Sub"

    # Zamiana podwójnych cudzysłowów na potrójne w kodzie VBA
    # vba_code = vba_code.replace('""', '"""')

    pyperclip.copy(vba_code)
    
    messagebox.showinfo("Kopiowanie zakończone", "Kod VBA został skopiowany do schowka!")
    root.destroy()

# Utworzenie interfejsu użytkownika
root = tk.Tk()
root.title("Generator kodu VBA")

# Wyśrodkowanie okna
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

text_area = tk.Text(root, height=20, width=80)
text_area.pack()

generate_button = tk.Button(root, text="Generuj kod VBA", command=generate_vba)
generate_button.pack()

root.mainloop()