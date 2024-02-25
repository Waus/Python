input_file_path = r'C:\Python\Pliki testowe input\duza tabela.txt'  # ścieżka do pliku wejściowego
output_file_path = r'C:\Python\Pliki testowe output\duza tabela.txt'  # ścieżka, gdzie zostanie zapisany plik wyjściowy

with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', newline='', encoding='utf-8') as outfile:
    for line in infile:
        fields = line.strip().split(';')  # Dzielenie linii na pola przy użyciu średnika jako separatora
        
        # Modyfikacja pierwszego pola
        fields[0] = '= "' + fields[0]
        
        # Przetwarzanie pola nr 5
        if fields[4] not in ['3000-01-01', '2000-12-31', '', 'Invalid date']:
            fields[4] = '" &X.WYSZUKAJ("#5";\'Lista identyfikatorów\'!$A$2:$A$100;\'Lista identyfikatorów\'!$C$2:$C$100;FAŁSZ) & "'
        
        # Przetwarzanie ostatniego pola (#30)
        fields[29] = '" &X.WYSZUKAJ("#7";\'Lista identyfikatorów\'!$A$2:$A$100;\'Lista identyfikatorów\'!$C$2:$C$100;FAŁSZ)'
        
        # Zapis do pliku wyjściowego bez używania csv.writer
        outfile.write(';'.join(fields) + '\n')