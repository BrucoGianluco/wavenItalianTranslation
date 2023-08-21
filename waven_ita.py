import os
import requests
import tkinter as tk
from tkinter import filedialog, messagebox

# Funzione per scaricare il file da GitHub
def download_file(url, file_path):
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)

# Funzione chiamata quando si fa clic su "Applica Patch"
def apply_patch():
    localization_path = os.path.join(waven_path, 'localization.en-us')
    backup_path = os.path.join(waven_path, 'localization.en-us.backup')
    
    try:
        # Crea una copia di backup del file originale se non esiste già
        if not os.path.exists(backup_path):
            os.rename(localization_path, backup_path)
        
        # Scarica e sostituisci il file
        localization_url = "https://raw.githubusercontent.com/BrucoGianluco/wavenItalianTranslation/main/localization.en-us"
        download_file(localization_url, localization_path)
        
        result_label.config(text="Patch applicata con successo.", foreground="green")
    except Exception as e:
        result_label.config(text=f"Errore durante l'applicazione della patch: {str(e)}", foreground="red")

# Funzione chiamata quando si fa clic su "Ripristina"
def restore_backup():
    localization_path = os.path.join(waven_path, 'localization.en-us')
    backup_path = os.path.join(waven_path, 'localization.en-us.backup')
    
    try:
        if os.path.exists(backup_path):
            # Elimina il file di destinazione se esiste
            if os.path.exists(localization_path):
                os.remove(localization_path)
            os.rename(backup_path, localization_path)
            result_label.config(text="Backup ripristinato correttamente.", foreground="green")
        else:
            result_label.config(text="Backup non trovato.", foreground="red")
    except Exception as e:
        result_label.config(text=f"Errore durante il ripristino del backup: {str(e)}", foreground="red")

# Creazione della finestra GUI
root = tk.Tk()
root.title("Waven Italian Translation Patch")
root.geometry("250x100")  # Imposta la dimensione della finestra a 500x500

# Colore di sfondo per lo stile scuro
background_color = "#333"

# Funzione per aggiungere uno stile uniforme agli elementi dell'interfaccia
def apply_custom_style(widget, fg_color="white", bg_color=background_color):
    widget.config(foreground=fg_color, background=bg_color)

# Etichetta e selettore di percorso
path_label = tk.Label(root, text="Seleziona la cartella di installazione di Waven:")
apply_custom_style(path_label)
path_label.pack(anchor="w")

def select_waven_path():
    global waven_path
    waven_path = filedialog.askdirectory(title="Seleziona la cartella di installazione di Waven")
    if check_waven_path(waven_path):
        apply_button.config(state="normal")
        restore_button.config(state="normal")
        result_label.config(text="")

path_select_button = tk.Button(root, text="Scegli percorso", command=select_waven_path)
apply_custom_style(path_select_button)
path_select_button.pack(anchor="w")

# Pulsanti
button_frame = tk.Frame(root)
button_frame.pack(anchor="w")

apply_button = tk.Button(button_frame, text="Applica Patch", state="disabled", command=apply_patch)
apply_custom_style(apply_button, bg_color="#444")
apply_button.pack(side="left")

restore_button = tk.Button(button_frame, text="Ripristina", state="disabled", command=restore_backup)
apply_custom_style(restore_button, bg_color="#444")
restore_button.pack(side="left")

# Etichetta per mostrare il risultato
result_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
apply_custom_style(result_label)
result_label.pack(anchor="w")

# Verifica se il percorso è valido
def check_waven_path(waven_path):
    return os.path.exists(waven_path)

root.mainloop()
