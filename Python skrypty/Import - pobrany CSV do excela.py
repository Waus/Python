import pyperclip

# Przykładowe dane
dane_csv = "Brak użytkownika w bazie dla tego kontraktu.;Błąd;;2021-01-01;2022-01-09;6;;1115;1;;4;;1447; ;12;;;;238,7363;;146,8281;;;40,3497;20,1751;8,9667;8,9667;13,45;;muranski"

# Przetwarzanie danych
pola = dane_csv.split(";")
pola[4] = '"&X.WYSZUKAJ("#5";\'Lista identyfikatorów\'!$A$2:$A$100;\'Lista identyfikatorów\'!$C$2:$C$100;FAŁSZ)&"'
pola[29] = '"&X.WYSZUKAJ("#7";\'Lista identyfikatorów\'!$A$2:$A$100;\'Lista identyfikatorów\'!$C$2:$C$100;FAŁSZ)'

# Tworzenie linii CSV z przetworzonymi danymi
przetworzone_dane_csv = '="' + ';'.join(pola) + '"'

# Kopiowanie do schowka
pyperclip.copy(przetworzone_dane_csv)