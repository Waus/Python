import os
import zipfile

def unzip_files_in_directory(directory):
    # Przejdź przez wszystkie pliki w podanym katalogu
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.zip'):
                # Pełna ścieżka do pliku ZIP
                file_path = os.path.join(root, file)
                # Folder docelowy do wypakowania (można go zmienić, jeśli potrzebne)
                output_dir = os.path.join(root, file.replace('.zip', ''))
                
                # Tworzenie folderu docelowego, jeśli nie istnieje
                os.makedirs(output_dir, exist_ok=True)
                
                # Wypakowanie pliku ZIP
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(output_dir)
                
                print(f'Wypakowano: {file_path} do {output_dir}')

# Przykład użycia:
# Podaj tutaj ścieżkę do katalogu, w którym znajdują się pliki ZIP
directory = r'C:\Users\Kamil Muranski\Desktop\Wiedźmin 3 dodatki'
unzip_files_in_directory(directory)
