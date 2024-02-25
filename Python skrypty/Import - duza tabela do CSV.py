import csv

input_file_path = r'C:\Python\Pliki testowe input\duza tabela.txt'  # ścieżka do pliku wejściowego
output_file_path = r'C:\Python\Pliki testowe output\duza tabela.txt'  # ścieżka, gdzie zostanie zapisany plik wyjściowy

with open(input_file_path, mode='r', encoding='utf-8') as infile, open(output_file_path, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile, delimiter=';')
    writer = csv.writer(outfile, delimiter=';')
    
    for row in reader:
        # Dopisz na początku każdej linii '= "'
        processed_row = ['= "' + row[0]]
        
        # Przetwarzanie pola nr 5
        if row[4] not in ['3000-01-01', '2000-12-31', '', 'Invalid date']:
            row[4] = '" &X.WYSZUKAJ("#5";\'Lista identyfikatorów\'!$A$2:$A$100;\'Lista identyfikatorów\'!$C$2:$C$100;FAŁSZ) & "'
        
        # Przetwarzanie ostatniego pola (#30)
        row[29] = '" &X.WYSZUKAJ("#7";\'Lista identyfikatorów\'!$A$2:$A$100;\'Lista identyfikatorów\'!$C$2:$C$100;FAŁSZ)'
        
        processed_row.extend(row[1:])
        writer.writerow(processed_row)