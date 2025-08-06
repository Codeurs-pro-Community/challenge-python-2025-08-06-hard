# challenge-python-2025-08-06-hard
Python hard Challenge

# Challenge Python Difficile : Générateur de Mot de Passe Sécurisé 🔐

### Objectif :

Créer une **application Python avec interface graphique (Tkinter)** qui génère des mots de passe sécurisés selon les critères définis par l’utilisateur.

---

## Ce que tu dois faire :

1. Créer une interface graphique simple (Tkinter) avec :

   * Champ pour entrer la **longueur** du mot de passe.
   * Cases à cocher pour inclure : **Chiffres, Lettres Majuscules, Symboles**.
   * Bouton **Générer**.
   * Champ d’affichage du mot de passe généré.
   * Bouton **Copier dans le presse-papier**.

2. Implémenter la logique pour générer le mot de passe de manière aléatoire en fonction des critères choisis.

3. Bonus :

   * Afficher un indicateur de niveau de sécurité (faible, moyen, fort).
   * Design amélioré (couleurs, polices).

---

## Étapes recommandées :

1. Créer l’interface avec **Tkinter (Label, Entry, Checkbutton, Button)**.
2. Écrire la fonction de génération de mot de passe (modules `random` et `string`).
3. Lier la génération aux boutons et affichage.
4. Utiliser le module **pyperclip** pour copier le mot de passe dans le presse-papier.
5. Bonus : Ajouter une barre de niveau de sécurité.

---

## Exemple attendu :

![password-generator-example](https://github.com/fschuermeyer/password-generator)

---

## démarrage :

  * `main.py` (structure de base avec interface Tkinter créée)

---

## Comment participer ?

1. Fork ce repository.
2. Crée ton dossier sous la forme : `nom_prenom/`
3. Développe ta solution dans ton dossier.
4. Fait une Pull Request pour soumettre ton code.

---

## Bonus :

* Niveau de sécurité visuel (faible, moyen, fort)
* Sauvegarde du mot de passe dans un fichier texte local

---
