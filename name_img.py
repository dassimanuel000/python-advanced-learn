import os
import shutil

def comparer_dossiers(img_verifier, pire_mg, nouveau_dossier):
    # Créer le nouveau dossier s'il n'existe pas déjà
    if not os.path.exists(nouveau_dossier):
        os.makedirs(nouveau_dossier)

    # Obtenir la liste des fichiers dans chaque dossier
    fichiers_dossier1 = os.listdir(img_verifier)
    fichiers_pire_mg = os.listdir(pire_mg)

    # Parcourir les fichiers du dossier 1
    for fichier in fichiers_dossier1:
        chemin_fichier1 = os.path.join(img_verifier, fichier)
        chemin_fichier_nouveau = os.path.join(nouveau_dossier, fichier)

        # Vérifier si le fichier existe dans le dossier 2
        if fichier not in fichiers_pire_mg:
            # Copier le fichier dans le nouveau dossier
            shutil.copy2(chemin_fichier1, chemin_fichier_nouveau)

    # Parcourir les fichiers du dossier 2
    for fichier in fichiers_pire_mg:
        chemin_fichier2 = os.path.join(pire_mg, fichier)
        chemin_fichier_nouveau = os.path.join(nouveau_dossier, fichier)

        # Vérifier si le fichier existe dans le dossier 1
        if fichier not in fichiers_dossier1:
            # Copier le fichier dans le nouveau dossier
            shutil.copy2(chemin_fichier2, chemin_fichier_nouveau)

# Exemple d'utilisation
img_verifier = "e:\Morgane\img_verifier"
pire_mg = "e:\Morgane\pire_img"
nouveau_dossier = "e:\Morgane"

comparer_dossiers(img_verifier, pire_mg, nouveau_dossier)
