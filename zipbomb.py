import zipfile
import os

# Funzione per creare la file structure
def create_zip_bomb(folder_name, depth, num_files):
    if depth == 0:
        return

    # Creazione directory
    os.makedirs(folder_name, exist_ok=True)

    # Creazione file in quantita'
    for i in range(num_files):
        zip_file_name = os.path.join(folder_name, f'file_{i}.zip')
        with zipfile.ZipFile(zip_file_name, 'w') as zipf:
            # Aggiungere un piccolo file di testo
            zipf.write('small_file.txt', f'file_{i}.txt')

        # Ricorsione per ricreare una sotto cartella
        subfolder_name = os.path.join(folder_name, f'subfolder_{i}')
        create_zip_bomb(subfolder_name, depth - 1, num_files)

# Creazione del piccolo file di testo
with open('small_file.txt', 'w') as file:
    file.write('SEI STATO ZIPBOMBATO')

# Scegli i parametri tipo nome profondita' e numero di file per directory
bomb_folder = 'zip_bomb'
depth = 5  
num_files = 5  

# Creazione della zip bomb
create_zip_bomb(bomb_folder, depth, num_files)

print(f'Zip bomb creata nella cartella "{bomb_folder}"')
