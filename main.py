import tkinter as tk
from tkinter import messagebox
import random
import string
# Bonus : import pyperclip si tu veux ajouter le copier-coller
# import pyperclip

# === FONCTION POUR GENERER LE MOT DE PASSE ===
def generer_mot_de_passe():
    # 1. Récupérer la longueur demandée depuis l'Entry
    # 2. Vérifier les options cochées (chiffres, majuscules, symboles)
    # 3. Construire le pool de caractères selon les choix
    # 4. Générer un mot de passe aléatoire
    # 5. Afficher le résultat dans le champ prévu (Label ou Entry)
    pass  # À compléter

# === FONCTION POUR COPIER DANS LE PRESSE-PAPIER (OPTIONNEL) ===
def copier_dans_presse_papier():
    # Récupérer le mot de passe affiché et le copier dans le presse-papier
    pass  # À compléter

# === CREATION DE L'INTERFACE ===
root = tk.Tk()
root.title("Générateur de Mot de Passe Sécurisé")

# === Titre ===
label_titre = tk.Label(root, text="Générateur de Mot de Passe", font=("Arial", 16))
label_titre.pack(pady=10)

# === Entrée pour la longueur du mot de passe ===
frame_length = tk.Frame(root)
frame_length.pack(pady=5)
tk.Label(frame_length, text="Longueur : ").pack(side="left")
entry_length = tk.Entry(frame_length, width=5)
entry_length.pack(side="left")

# === Options (Checkboxes) ===
# Astuce : Utilise des IntVar() pour récupérer les valeurs des Checkbuttons
include_digits = tk.IntVar()
include_uppercase = tk.IntVar()
include_symbols = tk.IntVar()

frame_options = tk.Frame(root)
frame_options.pack(pady=5)

tk.Checkbutton(frame_options, text="Chiffres", variable=include_digits).pack(side="left")
tk.Checkbutton(frame_options, text="Majuscules", variable=include_uppercase).pack(side="left")
tk.Checkbutton(frame_options, text="Symboles", variable=include_symbols).pack(side="left")

# === Bouton Générer ===
btn_generer = tk.Button(root, text="Générer", command=generer_mot_de_passe)
btn_generer.pack(pady=10)

# === Zone d'affichage du mot de passe généré ===
label_resultat = tk.Label(root, text="", font=("Arial", 14), fg="green")
label_resultat.pack(pady=10)

# === Bouton Copier (Optionnel) ===
btn_copier = tk.Button(root, text="Copier", command=copier_dans_presse_papier)
btn_copier.pack(pady=5)

# === Lancement de l'interface ===
root.mainloop()
