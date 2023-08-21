import os
import requests
from tkinter import filedialog, Tk, Button, Label

# Funzione per scaricare il file da GitHub
def download_file(url, file_path):
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)

# Funzione chiamata quando si fa clic su "Applica Patch"
def apply_patch():
    localization_path = os.path.join(waven_path, 'localization.en_us')
    backup_path = os.path.join(waven_path, 'localization.en_us.backup')
    
    # Crea una copia di backup del file originale se non esiste già
    if not os.path.exists(backup_path):
        os.rename(localization_path, backup_path)
    
    # Scarica e sostituisci il file
    localization_url = "https://raw.githubusercontent.com/BrucoGianluco/wavenItalianTranslation/main/localization.en_us"
    download_file(localization_url, localization_path)
    print("File localization.en_us scaricato e applicato correttamente.")

# Creazione della finestra GUI
root = Tk()
root.title("Waven Italian Translation Patch")

# Etichetta e selettore di percorso
path_label = Label(root, text="Seleziona la cartella di installazione di Waven (contents):")
path_label.pack()

def select_waven_path():
    global waven_path
    waven_path = filedialog.askdirectory(title="Seleziona la cartella contents di installazione di Waven")
    if check_waven_path(waven_path):
        apply_button.config(state="normal")
        restore_button.config(state="normal")

path_select_button = Button(root, text="Scegli percorso", command=select_waven_path)
path_select_button.pack()

# Pulsanti
apply_button = Button(root, text="Applica Patch", state="disabled", command=apply_patch)
apply_button.pack()

def restore_backup():
    localization_path = os.path.join(waven_path, 'localization.en_us')
    backup_path = os.path.join(waven_path, 'localization.en_us.backup')
    
    if os.path.exists(backup_path):
        os.rename(backup_path, localization_path)
        print("Backup ripristinato correttamente.")

restore_button = Button(root, text="Ripristina", state="disabled", command=restore_backup)
restore_button.pack()

# Verifica se il percorso è valido
def check_waven_path(waven_path):
    return os.path.exists(waven_path)

root.mainloop()
