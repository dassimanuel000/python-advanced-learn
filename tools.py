import os
import shutil
import time
import pandas as pd
from openpyxl import load_workbook
import xlsxwriter
import linecache
import requests
import json
import urllib.request

import csv

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Image
from io import BytesIO
from PIL import Image as PILImage
import base64
import tempfile

def append_new_line(file_name, text_to_append):
    with open(file_name, "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(text_to_append)

        
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

    #comparer_dossiers(img_verifier, pire_mg, nouveau_dossier)




def extraire_f():
    def extraire_texte_entre_virgule_et_tiret(nom_fichier):
        texte_extraits = []  # Une liste pour stocker les textes extraits
        
        # Ouvrir le fichier texte en mode lecture
        with open(nom_fichier, 'r') as fichier:
            # Lire chaque ligne du fichier
            for ligne in fichier:
                # Trouver l'index de la virgule (,) et du double tiret (--)
                index_virgule = ligne.find(',')
                index_tiret = ligne.find('--')
                
                # Vérifier si la virgule et le double tiret existent dans la ligne
                if index_virgule != -1 and index_tiret != -1:
                    # Extraire le texte entre la virgule et le double tiret
                    texte_entre_virgule_et_tiret = ligne[index_virgule + 1:index_tiret].strip()
                    
                    # Ajouter le texte extrait à la liste
                    texte_extraits.append(texte_entre_virgule_et_tiret)
        
        return texte_extraits

    # Utilisation de la fonction
    noms_fichier = 'd:/Documents/Website/therapeute.net/RECENSEMENT/tn.txt'  # Remplacez par le nom de votre fichier
    resultats = extraire_texte_entre_virgule_et_tiret(noms_fichier)

    # Afficher les résultats
    for resultat in resultats:
        print(resultat)
        append_new_line("prof.txt", resultat)


        
def creer_dossiers_a_partir_fichier_texte(nom_fichier):
    if os.path.exists(nom_fichier):
        with open(nom_fichier, 'r') as file:
            for ligne in file:
                ligne = ligne.strip()
                if ligne:
                    try:
                        os.mkdir(ligne)
                        print(f"Dossier '{ligne}' créé avec succès.")
                    except FileExistsError:
                        print(f"Le dossier '{ligne}' existe déjà.")
                    except Exception as e:
                        print(f"Erreur lors de la création du dossier '{ligne}': {str(e)}")
    else:
        print(f"Le fichier '{nom_fichier}' n'existe pas.")

    # Utilisation de la fonction avec votre fichier texte
    fichier_texte = './SUIVI-ATTESTATION/noms.txt'
    creer_dossiers_a_partir_fichier_texte(fichier_texte)





def nettoyer_fichier(fichier_entree, fichier_sortie):
    # Ouverture du fichier en mode lecture
    with open(fichier_entree, 'r') as fichier_lecture:
        # Lecture de toutes les lignes du fichier dans une liste
        lignes = fichier_lecture.readlines()

    # Ouverture du fichier en mode écriture
    with open(fichier_sortie, 'w') as fichier_ecriture:
        # Parcours de toutes les lignes lues
        for ligne in lignes:
            # Remplacement des tirets par des espaces
            nouvelle_ligne = ligne.replace('-', '  ')
            # Suppression de ".com" et ".fr"
            nouvelle_ligne = nouvelle_ligne.replace('.com', '').replace('.fr', '')
            # Écriture de la nouvelle ligne dans le fichier de sortie
            fichier_ecriture.write(nouvelle_ligne)

    print("Opération terminée. Les tirets, '.com' et '.fr' ont été remplacés ou supprimés dans le fichier de sortie.")


    # Appel de la fonction en spécifiant les noms de fichier d'entrée et de sortie
    #nettoyer_fichier('./mot-dns.txt', 'nouveau_fichier.txt')



# Fonction pour lire un fichier de mots et générer des liens
def generer_liens_depuis_fichier(nom_fichier_entree, nom_fichier_sortie, url_base):
    # Liste pour stocker les mots lus depuis le fichier
    mots = []

    # Lecture des mots depuis le fichier d'entrée
    with open(nom_fichier_entree, 'r') as fichier:
        mots = fichier.read().splitlines()

    # Fonction pour générer les liens
    def generer_liens(mots, url_base):
        liens = []
        for mot in mots:
            # Remplacez les espaces par des "+" dans le mot
            mot_formatte = mot.replace(' ', '+')
            # Créez l'URL complète en ajoutant le mot à l'URL de base
            lien = f"{url_base}{mot_formatte}"
            liens.append(lien)
        return liens

    # Génère les liens en utilisant la fonction
    liens = generer_liens(mots, url_base)

    # Écrit les liens dans le fichier de sortie
    with open(nom_fichier_sortie, 'w') as fichier_sortie:
        for lien in liens:
            fichier_sortie.write(lien + '\n')

    print(f"Les liens ont été enregistrés dans {nom_fichier_sortie}")

    # Nom du fichier contenant les mots
    nom_fichier_entree = "./nouveau_fichier.txt"

    # Nom du fichier de sortie pour les liens
    nom_fichier_sortie = "liens.txt"

    # URL de base
    url_base = "https://fr.semrush.com/analytics/keywordmagic/?q="

    # Appel de la fonction pour générer les liens à partir du fichier et les enregistrer
    generer_liens_depuis_fichier(nom_fichier_entree, nom_fichier_sortie, url_base)


    # Nom du fichier contenant les liens d'entrée
    nom_fichier_liens_entree = "liens.txt"
    # Nom du fichier de sortie pour les liens modifiés
    nom_fichier_liens_sortie = "liens_modifies.txt"

    # Fonction pour lire les liens depuis le fichier, ajouter "&db=fr" à la fin, et les enregistrer dans un nouveau fichier
    def modifier_et_enregistrer_liens(nom_fichier_entree, nom_fichier_sortie):
        with open(nom_fichier_entree, 'r') as fichier_entree:
            liens = fichier_entree.read().splitlines()
            liens_modifies = [lien + "&db=fr" for lien in liens]

        with open(nom_fichier_sortie, 'w') as fichier_sortie:
            for lien_modifie in liens_modifies:
                fichier_sortie.write(lien_modifie + '\n')

        print(f"Les liens modifiés ont été enregistrés dans {nom_fichier_sortie}")

    # Appel de la fonction pour modifier et enregistrer les liens
    modifier_et_enregistrer_liens(nom_fichier_liens_entree, nom_fichier_liens_sortie)







"""
# Chemin du dossier contenant les fichiers Excel à fusionner
dossier = 'D:/Documents/SUIVI-DNS/EXCEL-KEYWORD-DNS/.'


# Liste pour stocker les DataFrames de chaque feuille Excel
dataframes = []

# Parcourir tous les fichiers Excel dans le dossier
for fichier in os.listdir(dossier):
    if fichier.endswith('.xlsx'):  # Vous pouvez ajuster l'extension si nécessaire
        chemin_fichier = os.path.join(dossier, fichier)
        xls = pd.ExcelFile(chemin_fichier)
        for sheet_name in xls.sheet_names:
            # Charger chaque feuille dans un DataFrame
            df = xls.parse(sheet_name)
            dataframes.append(df)

# Créer un nouveau classeur Excel
classeur_final = pd.ExcelWriter('classeur_final.xlsx', engine='openpyxl')

# Écrire chaque DataFrame dans une feuille distincte
for i, df in enumerate(dataframes):
    df.to_excel(classeur_final, sheet_name=f'Feuille_{i}', index=False)

# Enregistrer le classeur final
classeur_final._save()
"""

def voir_doublonmail():
    def detecter_doublons_email(nom_fichier):
        unique_emails = set()
        
        with open(nom_fichier, 'r') as file:
            lines = file.readlines()
        
        doublons = []
        
        for line in lines:
            email = line.strip()
            if email in unique_emails:
                doublons.append(email)
            else:
                unique_emails.add(email)
        
        return doublons
        
    nom_fichier = 'd:/Documents/Website/therapeute.net/nom-doublons.txt'
    doublons = detecter_doublons_email(nom_fichier)

    if doublons:
        print("Doublons détectés :")
        for doublon in doublons:
            append_new_line("Doublons-found.txt", str(doublon))
    else:
        print("Doublons aaaaaaaaaaaaaaa :")
# Utilisation de la fonction


def Classeur_fusionne():
    folder_path = 'D:/Documents/SUIVI-DNS/EXCEL-KEYWORD-DNS/.'

    # Créer un nouveau classeur Excel dans lequel vous allez fusionner tous les fichiers
    writer = pd.ExcelWriter('Classeur_fusionné.xlsx', engine='xlsxwriter')

    # Parcourir tous les fichiers dans le dossier
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.xlsx') or file_name.endswith('.csv'):
            # Construire le chemin complet du fichier
            file_path = os.path.join(folder_path, file_name)
            
            # Vérifier le type de fichier et charger le fichier dans un DataFrame Pandas
            if file_name.endswith('.xlsx'):
                df = pd.read_excel(file_path)
            else: # Si le fichier est un CSV
                df = pd.read_csv(file_path)
            
            # Écrire le DataFrame dans une nouvelle feuille du fichier de destination
            # Utiliser le nom du fichier sans l'extension pour le nom de la feuille
            sheet_name = os.path.splitext(file_name)[0]
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    # Enregistrer le nouveau fichier Excel
    writer._save()


def renommer_fichiers(dossier):
    # Parcourir tous les fichiers dans le dossier
    for file_name in os.listdir(dossier):
        # Séparer le nom du fichier de son extension
        nom_base, extension = os.path.splitext(file_name)

        # Supprimer la chaîne spécifique du nom du fichier
        nom_modifie = nom_base.replace("_all-keywords_fr_2023-11-07", "")

        # Tronquer le nom du fichier si sa longueur dépasse 31 caractères (sans compter l'extension)
        if len(nom_modifie) > 31:
            nom_modifie = nom_modifie[:31]

        # Construire le nouveau nom du fichier avec l'extension
        nouveau_nom = f"{nom_modifie}{extension}"

        # Construire le chemin complet vers l'ancien et le nouveau fichier
        ancien_fichier = os.path.join(dossier, file_name)
        nouveau_fichier = os.path.join(dossier, nouveau_nom)

        # Renommer le fichier
        os.rename(ancien_fichier, nouveau_fichier)
        print(f"Renommé: {file_name} en {nouveau_nom}")

    # Utiliser la fonction sur le dossier souhaité
    # Remplacez 'chemin/vers/le/dossier' par le chemin réel du dossier contenant vos fichiers
    renommer_fichiers('D:/Documents/SUIVI-DNS/EXCEL-KEYWORD-DNS/.')



def get_infor_from_url(url):
    try:
        # Effectuer la demande HTTP
        response = requests.get(url)

        # Vérifier si la demande s'est bien passée (code de statut 200)
        if response.status_code == 200:
            # Extraire le contenu JSON de la réponse
            data = json.loads(response.text)
            time.sleep(0.5)
            # Vérifier si la liste contient des éléments
            if len(data) > 0:
                name = data[0].get("name")
                role = data[0].get("role")
                TEACHER = data[0].get("id_creator")
                organisme  = data[0].get("organisme")
                MAIL = data[0].get("email")
                
                if role:
                    append_new_line("info-found.txt", str(name)+ '--'+ str(role)+ '--'+ str(TEACHER)+ '--'+ str(organisme)+ '--'+ str(MAIL))
                    return role
                else:
                    append_new_line("info-found.txt", str("-----------------"))
                    return "Aucun rôle trouvé dans les données JSON."
            else:
                append_new_line("info-found.txt", str("-----------------"))
                return "Aucune donnée JSON trouvée dans la réponse."
        else:
            append_new_line("info-found.txt", str("-----------------"))
            return "La demande HTTP a échoué avec le code de statut : " + str(response.status_code)
    except Exception as e:
        append_new_line("info-found.txt", str("-----------------"))
        return "0000"




def get_role_from_url(url):
    try:
        # Effectuer la demande HTTP
        response = requests.get(url)
        time.sleep(0.2)
        # Vérifier si la demande s'est bien passée (code de statut 200)
        if response.status_code == 200:
            # Extraire le contenu JSON de la réponse
            data = json.loads(response.text)
            
            # Vérifier si la liste contient des éléments
            if len(data) > 0:
                #role = data[0].get("role")
                role = data[0].get("img")
                
                if role:
                    return role
                else:
                    return "Aucun rôle trouvé dans les données JSON."
            else:
                return "Aucune donnée JSON trouvée dans la réponse."
        else:
            return "La demande HTTP a échoué avec le code de statut : " + str(response.status_code)
    except Exception as e:
        return "0000"
    
def zefee():

    dernier_etape_processus = "not-found.txt-step.txt"
    try:
        with open(dernier_etape_processus, 'r') as file:
            etape_processus = str(file.read())
    except FileNotFoundError:
        etape_processus = 0


    for item in range(int(etape_processus), 168):
        linkkk = linecache.getline(r"d:/Documents/Website/therapeute.net/not-found.txt", item)
        linkkk = linkkk.replace('\n', '')
        get_infor_from_url(linkkk)
        with open(dernier_etape_processus, 'w') as file:
            file.write(str(item))
            

def GET_SIGNATURE_WITH_ID():

    for item in range(int(0), 1711):
        linkkk = linecache.getline(r"d:/Documents/Website/therapeute.net/id-jan.txt", item)
        role = get_role_from_url(linkkk)
        
        append_new_line("signa-id-jan.txt", str(role))
        print(item)


def GET_ID_WITH_MAIL():

    dernier_etape_processus = "MAIL-jan-step.txt"
    try:
        with open(dernier_etape_processus, 'r') as file:
            etape_processus = str(file.read())
    except FileNotFoundError:
        etape_processus = 1


    for item in range(int(etape_processus), 1425):
        linkkk = linecache.getline(r"d:/Documents/Website/therapeute.net/MAIL-jan.txt", item)
        role = get_role_from_url(linkkk)
        with open(dernier_etape_processus, 'w') as file:
            file.write(str(item))
        append_new_line("ID-MAIL-jan.txt", str(role))
        print(item)


def lire_fichier_csv(nom_fichier):
    donnees = []
    with open(nom_fichier, newline='', encoding='utf-8') as csvfile:
        lecteur_csv = csv.reader(csvfile)
        for ligne in lecteur_csv:
            donnees.append(ligne)
    return donnees

        

def recherche_ligne_texte(chemin_fichier, texte_recherche):
    try:
        with open(chemin_fichier, "r") as fichier:
            lignes = fichier.readlines()
            for ligne in lignes:
                if texte_recherche in ligne:
                    return 1  # Le texte a été trouvé
            return 0  # Le texte n'a pas été trouvé dans le fichier
    except FileNotFoundError:
        return 0  # Le fichier n'existe pas




# Chargez une police TrueType personnalisée
    
def generer_EV_pdf(ids , nom, prenom, consultante, date_debut, date_fin, signature):

    fichier_pdf = f"{nom}-{prenom}-{ids}--EEVV-ATTESTATION-SYNTHESE.pdf"
    doc = SimpleDocTemplate(fichier_pdf, pagesize=letter, 
                            rightMargin=72, leftMargin=72, 
                            topMargin=72, bottomMargin=18)
    styles = getSampleStyleSheet()

    contenu = []
    contenu.append(Spacer(0.5, 1))

    # Titre
    style_titre = styles['Title']
    style_titre.fontName = 'Helvetica'
    style_titre.fontSize = 18
    style_titre.spaceAfter = 20
    style_titre.textColor = colors.HexColor('#37456c')
    titre = Paragraph("ATTESTATION DE REMISE DE SYNTHESE DE BILAN DE COMPETENCES", style_titre)

    # Créer un tableau avec une seule cellule pour le titre
    tableau_titre = Table([[titre]], colWidths=[6 * inch], rowHeights=[1 * inch])

    # Appliquer un style au tableau pour ajouter une bordure
    style_tableau = TableStyle([('ALIGN', (0,0), (-1,-1), 'CENTER'),
                                ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
                                ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#37456c'))])  # 1 est l'épaisseur de la bordure

    tableau_titre.setStyle(style_tableau)

    # Ajouter le tableau du titre au contenu
    contenu.append(tableau_titre)
    contenu.append(Spacer(1.5, 25))
    # Corps du texte
    style_texte = styles['BodyText']
    style_texte.fontName = 'Helvetica'
    style_texte.fontSize = 12
    style_texte.textColor = colors.HexColor('#37456c')
    style_texte.leading = 24
    style_texte.alignment = 4

    styles2 = getSampleStyleSheet()
    style_texteCenter = styles2['BodyText']
    style_texteCenter.fontName = 'Helvetica'
    style_texteCenter.fontSize = 7
    style_texteCenter.textColor = colors.HexColor('#37456c')
    style_texteCenter.leading = 5
    style_texteCenter.alignment = 1

    styles3 = getSampleStyleSheet()
    style_texteLeft = styles3['BodyText']
    style_texteLeft.fontName = 'Helvetica'
    style_texteLeft.fontSize = 11
    style_texteLeft.textColor = colors.HexColor('#37456c')
    style_texteLeft.leading = 5
    style_texteLeft.alignment = 2

    """
    
    contenu.append(Paragraph(f"Nom: {nom}", style_texte))
    contenu.append(Paragraph(f"Prénom: {prenom}", style_texte))
    contenu.append(Paragraph(f"Âge: {age}", style_texte))
    """
    

    texte = f"""
    Je soussignée,  {consultante} , consultante en bilan de compétences au sein de l’organisme de formation EVOLUTION PROFESSIONNELLE, enregistré sous le numéro de déclaration d’activité 11756182775 auprès de la DIRECCTE (Direction régionale des entreprises, de la concurrence, de la consommation, du travail et de l’emploi) de l’Ile-de-France,
    """

    texte2 = f"""
    Certifie avoir accompagné {prenom} {nom} lors d’un bilan de compétences du {date_debut} au {date_fin}, conformément aux dispositions légales en vigueur, notamment celles prévues par le Code du travail.
    """
    
    texte3 = f"""
    À l'issue de cette démarche, le {date_fin}, une synthèse a été élaborée en collaboration. Elle reflète l'analyse des compétences, des aptitudes et des motivations de la personne concernée.
    """

    
    texte4 = f"""
    La synthèse du bilan de compétences a été présentée et transmise à {prenom} {nom} le {date_fin}.
    """

    texte5 = f"""
    Fait à Paris, le {date_fin}.
    """

    texte6 = f"""
    Mme {consultante}, 
    """
    texte61 =  f"""
    Consultante en Bilan de compétences
    """
    
    texte7 = f"""
    EVOLUTION PROFESSIONNELLE - 128 rue de la Boétie 75008 Paris
    """

    texte71 = f"""
    N° SIRET 87789243000019 - N° Déclaration d'activité 11756182775
    """

    texte72 = f"""
    Organisme de Formation non assujetti à la TVA
    """

    
    # Ajouter le texte à la liste du contenu
    contenu.append(Paragraph(texte, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte2, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte3, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte4, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte5, style_texte))
    contenu.append(Spacer(0.5, 15))
    contenu.append(Paragraph(texte6, style_texteLeft))
    contenu.append(Paragraph(texte61, style_texteLeft))

    contenu.append(Spacer(0.5, 15))
    image = Image(signature, width=100, height=60)
    image.hAlign = 'RIGHT'
    contenu.append(image)

    contenu.append(Spacer(0.5, 15))
    contenu.append(Paragraph(texte7, style_texteCenter))
    contenu.append(Paragraph(texte71, style_texteCenter))
    contenu.append(Paragraph(texte72, style_texteCenter))



    # Générez le PDF
    doc.build(contenu)
    return fichier_pdf


def generer_EVpdfEMARGEMENT(ids , nom, prenom, consultante, date_debut, date_two, date_three, date_fin, signature , role, vocation):

    fichier_pdf = f"{nom}-{prenom}-{ids}--EEVV-EMARGEMENT.pdf"
    doc = SimpleDocTemplate(fichier_pdf, pagesize=letter, 
                        rightMargin=50, leftMargin=50, 
                        topMargin=10, bottomMargin=10)


    styles = getSampleStyleSheet()

    contenu = []

    # Ajoutez une image (logo)
    
    if role == 'T1T':
        color = '37aff0'
        link = 'https://bilan.trouver-un-therapeute.fr'
        platformd = "https://i.ibb.co/5YqHDRb/therapeute.png"
    elif role == 'TS':
        # Talents-Solutions https://talents-solutions.com/
        color = '2153C1'
        link = 'https://talents.espace-competences.com/'
        platformd = "https://talents.espace-competences.com/wp-content/uploads/2023/05/Logo-talents-Solutions-1.png"
    elif role == 'TNET':
        color = '018B7F'
        link = 'https://espace-competences.com/'
        platformd = "https://i.ibb.co/3z7WJwg/image.png"
    elif role == 'ET':
        # EMPLOI TALENT https://emploi-talent.com/
        color = '094FA3'
        link = 'https://bilan.emploi-talent.com/'
        platformd = "https://i.ibb.co/cvM9g9C/image.png"
    elif role == 'FFR':
        color = '08b9e1'
        link = 'https://bilan.freelance-france.com/'
        platformd = "https://i.ibb.co/P1xScyk/image.png"
    else:
        color = '2153C1'
        link = 'https://bilan.trouver-un-candidat.com/'
        platformd = "https://i.ibb.co/YjrkZVn/image.png"



    #chemin_local = "./logo1.png"
    #urllib.request.urlretrieve(platformd, chemin_local)
    """image0 = Image(platformd, width=200, height=70)
    image0.hAlign = 'CENTER'
    contenu.append(image0)"""


    contenu.append(Spacer(0.5, 10))

    # Titre
    style_titre = styles['Title']
    style_titre.fontName = 'Helvetica'
    style_titre.fontSize = 22
    style_titre.spaceAfter = 20
    style_titre.textColor = colors.white
    titre = f""" FEUILLE D'EMARGEMENT \n Bilan de Compétences \n {date_debut} au {date_fin} """
    #titre = Paragraph(titre, style_titre)

    # Créer un tableau avec une seule cellule pour le titre
    tableau_titre = Table([[titre]], colWidths=[6 * inch], rowHeights=[1 * inch])

    style_tableau = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#' + color)),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#' + color)),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('FONTSIZE', (0, 0), (-1, -1), 22),
        ('LEADING', (0, 0), (-1, -1), 24)
    ])
    
    tableau_titre.setStyle(style_tableau)

    # Ajouter le tableau du titre au contenu
    contenu.append(tableau_titre)
    contenu.append(Spacer(1.5, 10))
    # Corps du texte
    style_texte = styles['BodyText']
    style_texte.fontName = 'Helvetica'
    style_texte.fontSize = 11
    style_texte.textColor = colors.HexColor('#37456c')
    style_texte.leading = 20
    style_texte.alignment = 4

    styles2 = getSampleStyleSheet()
    style_texteCenter = styles2['BodyText']
    style_texteCenter.fontName = 'Helvetica'
    style_texteCenter.fontSize = 10
    style_texteCenter.textColor = colors.HexColor('#37456c')
    style_texteCenter.leading = 15
    style_texteCenter.alignment = 1

    styles3 = getSampleStyleSheet()
    style_texteLeft = styles3['BodyText']
    style_texteLeft.fontName = 'Helvetica'
    style_texteLeft.fontSize = 11
    style_texteLeft.textColor = colors.HexColor('#37456c')
    style_texteLeft.leading = 5
    style_texteLeft.alignment = 2

    styles4 = getSampleStyleSheet()
    small_texteCenter = styles4['BodyText']
    small_texteCenter.fontName = 'Helvetica'
    small_texteCenter.fontSize = 7
    small_texteCenter.textColor = colors.HexColor('#37456c')
    small_texteCenter.leading = 3
    small_texteCenter.alignment = 1


        
    texte1 = f"""
    Nom et Prénom du titulaire : <b>{prenom} {nom} </b>
    """


    contenu.append(Paragraph(texte1, style_texte))
    contenu.append(Spacer(0.5, 5))

        
    texte2 = f"""
    <b>Rendez-vous avec la consultante</b>
    """
    texte3 = f"""
    <b>Signature</b>
    """
    texte4 = f"""
    {date_debut} <br /> Rdv 1 <br /><b>Mon itinéraire professionnel</b>
    """
    texte5 = f"""
    {date_two} <br /> Rdv 2 <br /><b>Mes motivations, ma personnalité</b>
    """
    texte6 = f"""
    {date_three} <br /> Rdv 3 <br /><b>Mes aspirations et mes freins</b>
    """
    texte7 = f"""
    {date_fin} <br /> Rdv 4 <br /><b>Mon projet professionnel </b>
    """



    #imaaaaaaaaaaaagegeeeeeeeeeeee
    
    if "data:image" in signature:
        signature = signature
    else:
        signature = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAABCAQAAABeK7cBAAAA9klEQVR42mJ4//8/Axjs4bJiXKAwM7OxsiHqFAiJi//8/Azn5z4/H//8/AwMDAwM7OxM7Tz/b/AzEwszMRM7hEM/z/BwAKXVH4QVHtQ//8/MRAszPxAI3Hw/f/AwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwMA5R1TcQ8YmQAAAAASUVORK5CYII="
    # Obtenez les données binaires de l'image depuis le lien de données
    image_data = signature.split(",")[1].strip()
    image_bytes = base64.b64decode(image_data)
    temp_image = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    temp_image.write(image_bytes)
    temp_image.close()
    signature = temp_image.name

    # Données pour le tableau
    
    image = Image(signature, width=60, height=25)
    nom_prenom = f"""{prenom} {nom}
    """
    image_with_text0 = [
        image,
        Paragraph(nom_prenom, small_texteCenter)
    ]

    data = [[Paragraph(texte2, style_texteCenter), Paragraph(texte3, style_texteCenter)],
            [Paragraph(texte4, style_texteCenter), image_with_text0],
            [Paragraph(texte5, style_texteCenter), image_with_text0],
            [Paragraph(texte6, style_texteCenter), image_with_text0],
            [Paragraph(texte7, style_texteCenter), image_with_text0]]

    # Créez le tableau
    table = Table(data, colWidths=[250, 250], rowHeights=65)

    # Définir le style du tableau
    style_tableau = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOX', (0, 0), (-1, -1), 1, colors.grey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('TEXTCOLOR', (0, 0), (1, 1), colors.black),  # Couleur du texte dans les deux premières cellules
        ('FONTSIZE', (0, 0), (1, 1), 12),  # Taille de la police dans les deux premières cellules
    ])

    table.setStyle(style_tableau)
    contenu.append(table)


    
    texte8 = f"""
    J’atteste m'être connecté(e) et avoir suivi les ateliers présents sur la plateforme d’e-learning {link}
    """
    contenu.append(Paragraph(texte8, style_texte))



    texte22 = f"""
    <b>Connexion à la plateforme d’e-learning</b>
    """
    texte23 = f"""
    <b>Signature</b>
    """
    texte71 = f"""
    Inter Rendez-vous <br /> Semaine du {date_debut} au {date_fin} 
    """

    image = Image(signature, width=60, height=25)
    nom_prenom = f"""{prenom} {nom}
    """
    image_with_text = [
        image,
        Paragraph("Signé(e) par "+nom_prenom, small_texteCenter)
    ]

    data2 = [[Paragraph(texte22, style_texteCenter), Paragraph(texte23, style_texteCenter)],
            [Paragraph(texte71, style_texteCenter), image_with_text]]

    # Créez le tableau50
    table2 = Table(data2, colWidths=[250, 250], rowHeights=50)
    style_tableau2 = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOX', (0, 0), (-1, -1), 1, colors.grey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('TEXTCOLOR', (0, 0), (1, 1), colors.black),  # Couleur du texte dans les deux premières cellules
        ('FONTSIZE', (0, 0), (1, 1), 12),  # Taille de la police dans les deux premières cellules
    ])

    


    table2.setStyle(style_tableau2)
    contenu.append(table2)

    texte70 = f"""
    EVOLUTION PROFESSIONNELLE - 128 rue de la Boétie 75008 Paris
    """

    texte72 = f"""
    N° SIRET 87789243000019 - N° Déclaration d'activité 11756182775
    """

    texte73 = f"""
    Organisme de Formation non assujetti à la TVA
    """

    contenu.append(Spacer(0.5, 85))
    contenu.append(Paragraph(texte70, small_texteCenter))
    contenu.append(Paragraph(texte72, small_texteCenter))
    contenu.append(Paragraph(texte73, small_texteCenter))


    # Générez le PDF
    doc.build(contenu)
    return fichier_pdf


def generer_EVpdfFORMATION(ids , nom, prenom, consultante, date_debut, date_fin,  signatureGerant, signatureSTAGIARE , role, vocation):

    fichier_pdf = f"{nom}-{prenom}-{ids}--EEVV-ATTESTATION-FIN.pdf"
    doc = SimpleDocTemplate(fichier_pdf, pagesize=letter, 
                        rightMargin=50, leftMargin=50, 
                        topMargin=10, bottomMargin=10)


    styles = getSampleStyleSheet()

    contenu = []

    # Ajoutez une image (logo)
    
    if role == 'T1T':
        color = '37aff0'
        link = 'https://bilan.trouver-un-therapeute.fr'
        platformd = "https://i.ibb.co/5YqHDRb/therapeute.png"
    elif role == 'TS':
        # Talents-Solutions https://talents-solutions.com/
        color = '2153C1'
        link = 'https://talents.espace-competences.com/'
        platformd = "https://talents.espace-competences.com/wp-content/uploads/2023/05/Logo-talents-Solutions-1.png"
    elif role == 'TNET':
        color = '018B7F'
        link = 'https://espace-competences.com/'
        platformd = "https://i.ibb.co/3z7WJwg/image.png"
    elif role == 'ET':
        # EMPLOI TALENT https://emploi-talent.com/
        color = '094FA3'
        link = 'https://bilan.emploi-talent.com/'
        platformd = "https://i.ibb.co/cvM9g9C/image.png"
    elif role == 'FFR':
        color = '08b9e1'
        link = 'https://bilan.freelance-france.com/'
        platformd = "https://i.ibb.co/P1xScyk/image.png"
    else:
        color = '2153C1'
        link = 'https://bilan.trouver-un-candidat.com/'
        platformd = "https://i.ibb.co/YjrkZVn/image.png"



    #chemin_local = "./logo1.png"
    #urllib.request.urlretrieve(platformd, chemin_local)
    """image0 = Image(platformd, width=200, height=70)
    image0.hAlign = 'CENTER'
    contenu.append(image0)"""


    contenu.append(Spacer(0.5, 40))

    # Titre
    style_titre = styles['Title']
    style_titre.fontName = 'Helvetica'
    style_titre.fontSize = 22
    style_titre.spaceAfter = 20
    style_titre.textColor = colors.white
    titre = Paragraph("ATTESTATION INDIVIDUELLE DE FIN DE FORMATION ", style_titre)

    # Créer un tableau avec une seule cellule pour le titre
    tableau_titre = Table([[titre]], colWidths=[6 * inch], rowHeights=[1 * inch])

    style_tableau = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#' + color)),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#' + color))
    ])
    
    tableau_titre.setStyle(style_tableau)

    # Ajouter le tableau du titre au contenu
    contenu.append(tableau_titre)
    contenu.append(Spacer(1.5, 55))
    # Corps du texte
    style_texte = styles['BodyText']
    style_texte.fontName = 'Helvetica'
    style_texte.fontSize = 11
    style_texte.textColor = colors.HexColor('#37456c')
    style_texte.leading = 20
    style_texte.alignment = 4

    styles2 = getSampleStyleSheet()
    style_texteCenter = styles2['BodyText']
    style_texteCenter.fontName = 'Helvetica'
    style_texteCenter.fontSize = 7
    style_texteCenter.textColor = colors.HexColor('#37456c')
    style_texteCenter.leading = 5
    style_texteCenter.alignment = 1

    styles3 = getSampleStyleSheet()
    style_texteLeft = styles3['BodyText']
    style_texteLeft.fontName = 'Helvetica'
    style_texteLeft.fontSize = 11
    style_texteLeft.textColor = colors.HexColor('#37456c')
    style_texteLeft.leading = 5
    style_texteLeft.alignment = 2

    styles4 = getSampleStyleSheet()
    style_sooulign = styles4['BodyText']
    style_sooulign.fontName = 'Helvetica'
    style_sooulign.fontSize = 11
    style_sooulign.textColor = colors.HexColor('#37456c')
    style_sooulign.leading = 20
    style_sooulign.alignment = 4
    style_sooulign.textDecoration = 'underline'


        
    texte1 = f"""
    Je soussigné(e) Monsieur Florent COVILETTE, représentant(e) légal(e) de l’organisme de formation EVOLUTION PROFESSIONNELLE enregistré sous le numéro de déclaration d’activité 11756182775 auprès de la DIRECCTE (Direction régionale des entreprises, de la concurrence, de la consommation, du travail et de l’emploi) de l’Ile-de-France atteste que {prenom} {nom}, {vocation} a suivi le Bilan de Compétences sur la période du {date_debut} au {date_fin}.
    """

    texte2 = f"""
    <u>Durée du Bilan de compétences : 24h00</u>
    """

    texte3 = f"""
    Intervenant(e) : Madame {consultante}
    """

    texte4 = f"""
    <u>Objectifs pédagogiques mentionnés dans le programme de formation :</u>
    """

    texte5 = f"""
    Le bilan de compétences est une réflexion professionnelle pour repérer les atouts, les axes de développement, et les traduire en objectifs de changement. Les bénéficiaires apprendront à mieux se connaître au travers de questionnaires de personnalité, à valoriser l’estime de soi et ainsi comprendre les choix, les causes de changement, les différentes expériences, les formations effectuées ou suivies qu’ils ont fait lors de leurs parcours professionnels.
    """

    texte6 = f"""
    Lors de la deuxième phase, l’exploration de l’histoire professionnelle et personnelle permettra d’identifier les compétences construites et de rédiger un portfolio de compétences.
    """

    texte61 =  f"""
    Identifier, clarifier et valider un projet de développement de compétences, ainsi que la rédaction d’un plan d’action en lien avec le développement de compétences.
    """

    texte7 = f"""
    Enfin, lors de la dernière phase du bilan de compétences, la consultante délivrera aux bénéficiaires les informations recueillies via leurs travaux effectués au préalable, analysera en synergie avec les stagiaires les compétences révélées et pour finir rédigera la synthèse du bilan de compétences.
    """

    texte71 = f"""
    EVOLUTION PROFESSIONNELLE - 128 rue de la Boétie 75008 Paris
    """

    texte72 = f"""
    N° SIRET 87789243000019 - N° Déclaration d'activité 11756182775
    """

    texte73 = f"""
    Organisme de Formation non assujetti à la TVA
    """

    

    texte74 = f"""
    <u>Résultats de l’évaluation des acquis :</u>
    """

    texte75 = f"""
    Le participant a appris à mieux se connaître au travers des questionnaires de personnalité, à valoriser l’estime de soi et ainsi comprendre ses choix, les causes de changement, ses différentes expériences, ses formations effectuées ou suivies qu’il a fait lors de son parcours professionnel.
    """

    texte76 = f"""
    Le bilan de compétences a permis au bénéficiaire de valider son projet réaliste et réalisable et ainsi définir son plan d’actions pour la concrétisation de celui-ci.
    """

    texte77 = f"""
    Fait à Paris, le {date_fin}.
    """

    texte78 = f"""
    EVOLUTION PROFESSIONNELLE
    """

    texte79 = f"""
    Monsieur Florent COVILETTE
    """

    texte710 = f"""
    Gérant(e)
    """

    texte711 = f"""
    Signature
    """


    texte712 = f"""
    {prenom} {nom}
    """

    texte713 = f"""
    Signature
    """


    texte71 = f"""
    EVOLUTION PROFESSIONNELLE - 128 rue de la Boétie 75008 Paris
    """

    texte72 = f"""
    N° SIRET 87789243000019 - N° Déclaration d'activité 11756182775
    """

    texte73 = f"""
    Organisme de Formation non assujetti à la TVA
    """

    # Ajouter le texte à la liste du contenu
    contenu.append(Paragraph(texte1, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte2, style_sooulign))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte3, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte4, style_sooulign))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte5, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte6, style_texte))
    contenu.append(Paragraph(texte61, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte7, style_texte))
    contenu.append(Spacer(0.5, 45))
    contenu.append(Paragraph(texte71, style_texteCenter))
    contenu.append(Paragraph(texte72, style_texteCenter))
    contenu.append(Paragraph(texte73, style_texteCenter))
    contenu.append(Spacer(0.5, 80))
    contenu.append(Paragraph(texte74, style_sooulign))
    contenu.append(Paragraph(texte75, style_texte))
    contenu.append(Paragraph(texte76, style_texte))
    contenu.append(Spacer(0.5, 20))
    contenu.append(Paragraph(texte77, style_texte))
    contenu.append(Spacer(0.5, 30))
    contenu.append(Paragraph(texte78, style_texte))
    contenu.append(Paragraph(texte79, style_texte))
    contenu.append(Spacer(0.5, -15))
    contenu.append(Paragraph(texte710, style_texte))
    contenu.append(Spacer(0.5, -15))
    contenu.append(Paragraph(texte711, style_texte))
    

    image0 = Image('https://i.ibb.co/wNT9TNK/signature-colivette.png', width=120, height=70)
    image0.hAlign = 'LEFT'
    contenu.append(image0)
    image0 = Image(signatureGerant, width=120, height=80)
    image0.hAlign = 'LEFT'
    contenu.append(image0)

    


    contenu.append(Paragraph(texte712, style_texteLeft))
    contenu.append(Paragraph(texte713, style_texteLeft))
    contenu.append(Spacer(0.5, 5))

    if "data:image" in signatureSTAGIARE:
        signatureSTAGIARE = signatureSTAGIARE
    else:
        signatureSTAGIARE = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAABCAQAAABeK7cBAAAA9klEQVR42mJ4//8/Axjs4bJiXKAwM7OxsiHqFAiJi//8/Azn5z4/H//8/AwMDAwM7OxM7Tz/b/AzEwszMRM7hEM/z/BwAKXVH4QVHtQ//8/MRAszPxAI3Hw/f/AwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwMA5R1TcQ8YmQAAAAASUVORK5CYII="
    # Obtenez les données binaires de l'image depuis le lien de données
    image_data = signatureSTAGIARE.split(",")[1].strip()
    image_bytes = base64.b64decode(image_data)
    temp_image = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    temp_image.write(image_bytes)
    temp_image.close()


    image1 = Image(temp_image.name, width=150, height=70)
    image1.hAlign = 'RIGHT'
    contenu.append(image1)


    contenu.append(Spacer(0.5, 40))
    contenu.append(Paragraph(texte71, style_texteCenter))
    contenu.append(Paragraph(texte72, style_texteCenter))
    contenu.append(Paragraph(texte73, style_texteCenter))


    # Générez le PDF
    doc.build(contenu)
    return fichier_pdf




def generer_pdf_PM_EMARGEMENT(ids , nom, prenom, consultante, date_debut, date_two, date_three, date_fin, signature , role, vocation):

    fichier_pdf = f"{nom}-{prenom}-{ids}--PPMM-EMARGEMENT.pdf"
    doc = SimpleDocTemplate(fichier_pdf, pagesize=letter, 
                        rightMargin=50, leftMargin=50, 
                        topMargin=10, bottomMargin=10)


    styles = getSampleStyleSheet()

    contenu = []

    # Ajoutez une image (logo)
    
    if role == 'T1T':
        color = '37aff0'
        link = 'https://bilan.trouver-un-therapeute.fr'
        platformd = "https://i.ibb.co/5YqHDRb/therapeute.png"
    elif role == 'TS':
        # Talents-Solutions https://talents-solutions.com/
        color = '2153C1'
        link = 'https://talents.espace-competences.com/'
        platformd = "https://talents.espace-competences.com/wp-content/uploads/2023/05/Logo-talents-Solutions-1.png"
    elif role == 'TNET':
        color = '018B7F'
        link = 'https://espace-competences.com/'
        platformd = "https://i.ibb.co/3z7WJwg/image.png"
    elif role == 'ET':
        # EMPLOI TALENT https://emploi-talent.com/
        color = '094FA3'
        link = 'https://bilan.emploi-talent.com/'
        platformd = "https://i.ibb.co/cvM9g9C/image.png"
    elif role == 'FFR':
        color = '08b9e1'
        link = 'https://bilan.freelance-france.com/'
        platformd = "https://i.ibb.co/P1xScyk/image.png"
    else:
        color = '2153C1'
        link = 'https://bilan.trouver-un-candidat.com/'
        platformd = "https://i.ibb.co/YjrkZVn/image.png"



    #chemin_local = "./logo1.png"
    #urllib.request.urlretrieve(platformd, chemin_local)
    """image0 = Image(platformd, width=200, height=70)
    image0.hAlign = 'CENTER'
    contenu.append(image0)"""


    contenu.append(Spacer(0.5, 10))

    # Titre
    style_titre = styles['Title']
    style_titre.fontName = 'Helvetica'
    style_titre.fontSize = 22
    style_titre.spaceAfter = 20
    style_titre.textColor = colors.white
    titre = f""" FEUILLE D'EMARGEMENT \n Bilan de Compétences \n {date_debut} au {date_fin} """
    #titre = Paragraph(titre, style_titre)

    # Créer un tableau avec une seule cellule pour le titre
    tableau_titre = Table([[titre]], colWidths=[6 * inch], rowHeights=[1 * inch])

    style_tableau = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#' + color)),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#' + color)),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('FONTSIZE', (0, 0), (-1, -1), 22),
        ('LEADING', (0, 0), (-1, -1), 24)
    ])
    
    tableau_titre.setStyle(style_tableau)

    # Ajouter le tableau du titre au contenu
    contenu.append(tableau_titre)
    contenu.append(Spacer(1.5, 10))
    # Corps du texte
    style_texte = styles['BodyText']
    style_texte.fontName = 'Helvetica'
    style_texte.fontSize = 11
    style_texte.textColor = colors.HexColor('#37456c')
    style_texte.leading = 20
    style_texte.alignment = 4

    styles2 = getSampleStyleSheet()
    style_texteCenter = styles2['BodyText']
    style_texteCenter.fontName = 'Helvetica'
    style_texteCenter.fontSize = 10
    style_texteCenter.textColor = colors.HexColor('#37456c')
    style_texteCenter.leading = 15
    style_texteCenter.alignment = 1

    styles3 = getSampleStyleSheet()
    style_texteLeft = styles3['BodyText']
    style_texteLeft.fontName = 'Helvetica'
    style_texteLeft.fontSize = 11
    style_texteLeft.textColor = colors.HexColor('#37456c')
    style_texteLeft.leading = 5
    style_texteLeft.alignment = 2

    styles4 = getSampleStyleSheet()
    small_texteCenter = styles4['BodyText']
    small_texteCenter.fontName = 'Helvetica'
    small_texteCenter.fontSize = 7
    small_texteCenter.textColor = colors.HexColor('#37456c')
    small_texteCenter.leading = 3
    small_texteCenter.alignment = 1


        
    texte1 = f"""
    Nom et Prénom du titulaire : <b>{prenom} {nom} </b>
    """


    contenu.append(Paragraph(texte1, style_texte))
    contenu.append(Spacer(0.5, 5))

        
    texte2 = f"""
    <b>Rendez-vous avec la consultante</b>
    """
    texte3 = f"""
    <b>Signature</b>
    """
    texte4 = f"""
    {date_debut} <br /> Rdv 1 <br /><b>Mon itinéraire professionnel</b>
    """
    texte5 = f"""
    {date_two} <br /> Rdv 2 <br /><b>Mes motivations, ma personnalité</b>
    """
    texte6 = f"""
    {date_three} <br /> Rdv 3 <br /><b>Mes aspirations et mes freins</b>
    """
    texte7 = f"""
    {date_fin} <br /> Rdv 4 <br /><b>Mon projet professionnel </b>
    """



    #imaaaaaaaaaaaagegeeeeeeeeeeee
    
    if "data:image" in signature:
        signature = signature
    else:
        signature = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAABCAQAAABeK7cBAAAA9klEQVR42mJ4//8/Axjs4bJiXKAwM7OxsiHqFAiJi//8/Azn5z4/H//8/AwMDAwM7OxM7Tz/b/AzEwszMRM7hEM/z/BwAKXVH4QVHtQ//8/MRAszPxAI3Hw/f/AwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwMA5R1TcQ8YmQAAAAASUVORK5CYII="
    # Obtenez les données binaires de l'image depuis le lien de données
    image_data = signature.split(",")[1].strip()
    image_bytes = base64.b64decode(image_data)
    temp_image = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    temp_image.write(image_bytes)
    temp_image.close()
    signature = temp_image.name

    # Données pour le tableau
    
    image = Image(signature, width=60, height=25)
    nom_prenom = f"""{prenom} {nom}
    """
    image_with_text0 = [
        image,
        Paragraph(nom_prenom, small_texteCenter)
    ]

    data = [[Paragraph(texte2, style_texteCenter), Paragraph(texte3, style_texteCenter)],
            [Paragraph(texte4, style_texteCenter), image_with_text0],
            [Paragraph(texte5, style_texteCenter), image_with_text0],
            [Paragraph(texte6, style_texteCenter), image_with_text0],
            [Paragraph(texte7, style_texteCenter), image_with_text0]]

    # Créez le tableau
    table = Table(data, colWidths=[250, 250], rowHeights=65)

    # Définir le style du tableau
    style_tableau = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOX', (0, 0), (-1, -1), 1, colors.grey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('TEXTCOLOR', (0, 0), (1, 1), colors.black),  # Couleur du texte dans les deux premières cellules
        ('FONTSIZE', (0, 0), (1, 1), 12),  # Taille de la police dans les deux premières cellules
    ])

    table.setStyle(style_tableau)
    contenu.append(table)


    
    texte8 = f"""
    J’atteste m'être connecté(e) et avoir suivi les ateliers présents sur la plateforme d’e-learning {link}
    """
    contenu.append(Paragraph(texte8, style_texte))



    texte22 = f"""
    <b>Connexion à la plateforme d’e-learning</b>
    """
    texte23 = f"""
    <b>Signature</b>
    """
    texte71 = f"""
    Inter Rendez-vous <br /> Semaine du {date_debut} au {date_fin} 
    """

    image = Image(signature, width=60, height=25)
    nom_prenom = f"""{prenom} {nom}
    """
    image_with_text = [
        image,
        Paragraph("Signé(e) par "+nom_prenom, small_texteCenter)
    ]

    data2 = [[Paragraph(texte22, style_texteCenter), Paragraph(texte23, style_texteCenter)],
            [Paragraph(texte71, style_texteCenter), image_with_text]]

    # Créez le tableau50
    table2 = Table(data2, colWidths=[250, 250], rowHeights=50)
    style_tableau2 = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOX', (0, 0), (-1, -1), 1, colors.grey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('TEXTCOLOR', (0, 0), (1, 1), colors.black),  # Couleur du texte dans les deux premières cellules
        ('FONTSIZE', (0, 0), (1, 1), 12),  # Taille de la police dans les deux premières cellules
    ])

    


    table2.setStyle(style_tableau2)
    contenu.append(table2)

    texte70 = f"""
    PM GROUPE FRANCE - 128 rue de la Boétie 75008 Paris
    """

    texte72 = f"""
    N° SIRET 79127535700030 - N° Déclaration d'activité 11755175375
    """

    texte73 = f"""
    Organisme de Formation non assujetti à la TVA
    """

    contenu.append(Spacer(0.5, 85))
    contenu.append(Paragraph(texte70, small_texteCenter))
    contenu.append(Paragraph(texte72, small_texteCenter))
    contenu.append(Paragraph(texte73, small_texteCenter))


    # Générez le PDF
    doc.build(contenu)
    return fichier_pdf


def generer_PMpdf(ids , nom, prenom, consultante, date_debut, date_fin, signature):

    fichier_pdf = f"{nom}-{prenom}-{ids}-PPMM--ATTESTATION-SYNTHESE.pdf"
    doc = SimpleDocTemplate(fichier_pdf, pagesize=letter, 
                            rightMargin=72, leftMargin=72, 
                            topMargin=72, bottomMargin=18)
    styles = getSampleStyleSheet()

    contenu = []
    contenu.append(Spacer(0.5, 1))

    # Titre
    style_titre = styles['Title']
    style_titre.fontName = 'Helvetica'
    style_titre.fontSize = 18
    style_titre.spaceAfter = 20
    style_titre.textColor = colors.HexColor('#37456c')
    titre = Paragraph("ATTESTATION DE REMISE DE SYNTHESE DE BILAN DE COMPETENCES", style_titre)

    # Créer un tableau avec une seule cellule pour le titre
    tableau_titre = Table([[titre]], colWidths=[6 * inch], rowHeights=[1 * inch])

    # Appliquer un style au tableau pour ajouter une bordure
    style_tableau = TableStyle([('ALIGN', (0,0), (-1,-1), 'CENTER'),
                                ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
                                ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#37456c'))])  # 1 est l'épaisseur de la bordure

    tableau_titre.setStyle(style_tableau)

    # Ajouter le tableau du titre au contenu
    contenu.append(tableau_titre)
    contenu.append(Spacer(1.5, 25))
    # Corps du texte
    style_texte = styles['BodyText']
    style_texte.fontName = 'Helvetica'
    style_texte.fontSize = 12
    style_texte.textColor = colors.HexColor('#37456c')
    style_texte.leading = 24
    style_texte.alignment = 4

    styles2 = getSampleStyleSheet()
    style_texteCenter = styles2['BodyText']
    style_texteCenter.fontName = 'Helvetica'
    style_texteCenter.fontSize = 7
    style_texteCenter.textColor = colors.HexColor('#37456c')
    style_texteCenter.leading = 5
    style_texteCenter.alignment = 1

    styles3 = getSampleStyleSheet()
    style_texteLeft = styles3['BodyText']
    style_texteLeft.fontName = 'Helvetica'
    style_texteLeft.fontSize = 11
    style_texteLeft.textColor = colors.HexColor('#37456c')
    style_texteLeft.leading = 5
    style_texteLeft.alignment = 2

    """
    
    contenu.append(Paragraph(f"Nom: {nom}", style_texte))
    contenu.append(Paragraph(f"Prénom: {prenom}", style_texte))
    contenu.append(Paragraph(f"Âge: {age}", style_texte))
    """
    

    texte = f"""
    Je soussignée,  {consultante} , consultante en bilan de compétences au sein de l’organisme de formation PM GROUPE FRANCE, enregistré sous le numéro de déclaration d’activité 11755175375 auprès de la DIRECCTE (Direction régionale des entreprises, de la concurrence, de la consommation, du travail et de l’emploi) de l’Ile-de-France,
    """

    texte2 = f"""
    Certifie avoir accompagné {prenom} {nom} lors d’un bilan de compétences du {date_debut} au {date_fin}, conformément aux dispositions légales en vigueur, notamment celles prévues par le Code du travail.
    """
    
    texte3 = f"""
    À l'issue de cette démarche, le {date_fin}, une synthèse a été élaborée en collaboration. Elle reflète l'analyse des compétences, des aptitudes et des motivations de la personne concernée.
    """

    
    texte4 = f"""
    La synthèse du bilan de compétences a été présentée et transmise à {prenom} {nom} le {date_fin}.
    """

    texte5 = f"""
    Fait à Paris, le {date_fin}.
    """

    texte6 = f"""
    Mme {consultante}, 
    """
    texte61 =  f"""
    Consultante en Bilan de compétences
    """
    
    texte7 = f"""
    PM GROUPE FRANCE - 128 rue de la Boétie 75008 Paris
    """
    texte71 = f"""
    N° SIRET 79127535700030 - N° Déclaration d'activité 11755175375
    """
    texte72 = f"""
    Organisme de Formation non assujetti à la TVA
    """

    
    # Ajouter le texte à la liste du contenu
    contenu.append(Paragraph(texte, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte2, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte3, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte4, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte5, style_texte))
    contenu.append(Spacer(0.5, 15))
    contenu.append(Paragraph(texte6, style_texteLeft))
    contenu.append(Paragraph(texte61, style_texteLeft))

    contenu.append(Spacer(0.5, 15))
    image = Image(signature, width=100, height=60)
    image.hAlign = 'RIGHT'
    contenu.append(image)

    contenu.append(Spacer(0.5, 15))
    contenu.append(Paragraph(texte7, style_texteCenter))
    contenu.append(Paragraph(texte71, style_texteCenter))
    contenu.append(Paragraph(texte72, style_texteCenter))



    # Générez le PDF
    doc.build(contenu)
    return fichier_pdf


def generer_PMpdfFORMATION(ids , nom, prenom, consultante, date_debut, date_fin,  signatureGerant, signatureSTAGIARE , role, vocation):

    fichier_pdf = f"{nom}-{prenom}-{ids}--PPMM-ATTESTATION-FIN.pdf"
    doc = SimpleDocTemplate(fichier_pdf, pagesize=letter, 
                        rightMargin=50, leftMargin=50, 
                        topMargin=10, bottomMargin=10)


    styles = getSampleStyleSheet()

    contenu = []

    # Ajoutez une image (logo)
    
    if role == 'T1T':
        color = '37aff0'
        link = 'https://bilan.trouver-un-therapeute.fr'
        platformd = "https://i.ibb.co/5YqHDRb/therapeute.png"
    elif role == 'TS':
        # Talents-Solutions https://talents-solutions.com/
        color = '2153C1'
        link = 'https://talents.espace-competences.com/'
        platformd = "https://talents.espace-competences.com/wp-content/uploads/2023/05/Logo-talents-Solutions-1.png"
    elif role == 'TNET':
        color = '018B7F'
        link = 'https://espace-competences.com/'
        platformd = "https://i.ibb.co/3z7WJwg/image.png"
    elif role == 'ET':
        # EMPLOI TALENT https://emploi-talent.com/
        color = '094FA3'
        link = 'https://bilan.emploi-talent.com/'
        platformd = "https://i.ibb.co/cvM9g9C/image.png"
    elif role == 'FFR':
        color = '08b9e1'
        link = 'https://bilan.freelance-france.com/'
        platformd = "https://i.ibb.co/P1xScyk/image.png"
    else:
        color = '2153C1'
        link = 'https://bilan.trouver-un-candidat.com/'
        platformd = "https://i.ibb.co/YjrkZVn/image.png"



    #chemin_local = "./logo1.png"
    #urllib.request.urlretrieve(platformd, chemin_local)
    """image0 = Image(platformd, width=200, height=70)
    image0.hAlign = 'CENTER'
    contenu.append(image0)"""


    contenu.append(Spacer(0.5, 40))

    # Titre
    style_titre = styles['Title']
    style_titre.fontName = 'Helvetica'
    style_titre.fontSize = 22
    style_titre.spaceAfter = 20
    style_titre.textColor = colors.white
    titre = Paragraph("ATTESTATION INDIVIDUELLE DE FIN DE FORMATION ", style_titre)

    # Créer un tableau avec une seule cellule pour le titre
    tableau_titre = Table([[titre]], colWidths=[6 * inch], rowHeights=[1 * inch])

    style_tableau = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#' + color)),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#' + color))
    ])
    
    tableau_titre.setStyle(style_tableau)

    # Ajouter le tableau du titre au contenu
    contenu.append(tableau_titre)
    contenu.append(Spacer(1.5, 55))
    # Corps du texte
    style_texte = styles['BodyText']
    style_texte.fontName = 'Helvetica'
    style_texte.fontSize = 11
    style_texte.textColor = colors.HexColor('#37456c')
    style_texte.leading = 20
    style_texte.alignment = 4

    styles2 = getSampleStyleSheet()
    style_texteCenter = styles2['BodyText']
    style_texteCenter.fontName = 'Helvetica'
    style_texteCenter.fontSize = 7
    style_texteCenter.textColor = colors.HexColor('#37456c')
    style_texteCenter.leading = 5
    style_texteCenter.alignment = 1

    styles3 = getSampleStyleSheet()
    style_texteLeft = styles3['BodyText']
    style_texteLeft.fontName = 'Helvetica'
    style_texteLeft.fontSize = 11
    style_texteLeft.textColor = colors.HexColor('#37456c')
    style_texteLeft.leading = 5
    style_texteLeft.alignment = 2

    styles4 = getSampleStyleSheet()
    style_sooulign = styles4['BodyText']
    style_sooulign.fontName = 'Helvetica'
    style_sooulign.fontSize = 11
    style_sooulign.textColor = colors.HexColor('#37456c')
    style_sooulign.leading = 20
    style_sooulign.alignment = 4
    style_sooulign.textDecoration = 'underline'


        
    texte1 = f"""
    Je soussigné(e) Monsieur Florent COVILETTE, représentant(e) légal(e) de l’organisme de formation PM GROUPE FRANCE enregistré sous le numéro de déclaration d’activité 11755175375 auprès de la DIRECCTE (Direction régionale des entreprises, de la concurrence, de la consommation, du travail et de l’emploi) de l’Ile-de-France atteste que {prenom} {nom}, {vocation} a suivi le Bilan de Compétences sur la période du {date_debut} au {date_fin}.
    """

    texte2 = f"""
    <u>Durée du Bilan de compétences : 24h00</u>
    """

    texte3 = f"""
    Intervenant(e) : Madame {consultante}
    """

    texte4 = f"""
    <u>Objectifs pédagogiques mentionnés dans le programme de formation :</u>
    """

    texte5 = f"""
    Le bilan de compétences est une réflexion professionnelle pour repérer les atouts, les axes de développement, et les traduire en objectifs de changement. Les bénéficiaires apprendront à mieux se connaître au travers de questionnaires de personnalité, à valoriser l’estime de soi et ainsi comprendre les choix, les causes de changement, les différentes expériences, les formations effectuées ou suivies qu’ils ont fait lors de leurs parcours professionnels.
    """

    texte6 = f"""
    Lors de la deuxième phase, l’exploration de l’histoire professionnelle et personnelle permettra d’identifier les compétences construites et de rédiger un portfolio de compétences.
    """

    texte61 =  f"""
    Identifier, clarifier et valider un projet de développement de compétences, ainsi que la rédaction d’un plan d’action en lien avec le développement de compétences.
    """

    texte7 = f"""
    Enfin, lors de la dernière phase du bilan de compétences, la consultante délivrera aux bénéficiaires les informations recueillies via leurs travaux effectués au préalable, analysera en synergie avec les stagiaires les compétences révélées et pour finir rédigera la synthèse du bilan de compétences.
    """

    texte71 = f"""
    PM GROUPE FRANCE - 128 rue de la Boétie 75008 Paris
    """

    texte72 = f"""
    N° SIRET 79127535700030 - N° Déclaration d'activité 11755175375
    """

    texte73 = f"""
    Organisme de Formation non assujetti à la TVA
    """

    

    texte74 = f"""
    <u>Résultats de l’évaluation des acquis :</u>
    """

    texte75 = f"""
    Le participant a appris à mieux se connaître au travers des questionnaires de personnalité, à valoriser l’estime de soi et ainsi comprendre ses choix, les causes de changement, ses différentes expériences, ses formations effectuées ou suivies qu’il a fait lors de son parcours professionnel.
    """

    texte76 = f"""
    Le bilan de compétences a permis au bénéficiaire de valider son projet réaliste et réalisable et ainsi définir son plan d’actions pour la concrétisation de celui-ci.
    """

    texte77 = f"""
    Fait à Paris, le {date_fin}.
    """

    texte78 = f"""
    PM GROUPE FRANCE
    """

    texte79 = f"""
    Monsieur Florent COVILETTE
    """

    texte710 = f"""
    Gérant(e)
    """

    texte711 = f"""
    Signature
    """


    texte712 = f"""
    {prenom} {nom}
    """

    texte713 = f"""
    Signature
    """


    texte71 = f"""
    PM GROUPE FRANCE - 128 rue de la Boétie 75008 Paris
    """

    texte72 = f"""
    N° SIRET 79127535700030 - N° Déclaration d'activité 11755175375
    """

    texte73 = f"""
    Organisme de Formation non assujetti à la TVA
    """

    # Ajouter le texte à la liste du contenu
    contenu.append(Paragraph(texte1, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte2, style_sooulign))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte3, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte4, style_sooulign))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte5, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte6, style_texte))
    contenu.append(Paragraph(texte61, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte7, style_texte))
    contenu.append(Spacer(0.5, 45))
    contenu.append(Paragraph(texte71, style_texteCenter))
    contenu.append(Paragraph(texte72, style_texteCenter))
    contenu.append(Paragraph(texte73, style_texteCenter))
    contenu.append(Spacer(0.5, 80))
    contenu.append(Paragraph(texte74, style_sooulign))
    contenu.append(Paragraph(texte75, style_texte))
    contenu.append(Paragraph(texte76, style_texte))
    contenu.append(Spacer(0.5, 20))
    contenu.append(Paragraph(texte77, style_texte))
    contenu.append(Spacer(0.5, 30))
    contenu.append(Paragraph(texte78, style_texte))
    contenu.append(Paragraph(texte79, style_texte))
    contenu.append(Spacer(0.5, -15))
    contenu.append(Paragraph(texte710, style_texte))
    contenu.append(Spacer(0.5, -15))
    contenu.append(Paragraph(texte711, style_texte))
    

    image0 = Image('https://i.ibb.co/wNT9TNK/signature-colivette.png', width=120, height=70)
    image0.hAlign = 'LEFT'
    contenu.append(image0)
    image0 = Image(signatureGerant, width=120, height=80)
    image0.hAlign = 'LEFT'
    contenu.append(image0)

    


    contenu.append(Paragraph(texte712, style_texteLeft))
    contenu.append(Paragraph(texte713, style_texteLeft))
    contenu.append(Spacer(0.5, 5))

    if "data:image" in signatureSTAGIARE:
        signatureSTAGIARE = signatureSTAGIARE
    else:
        signatureSTAGIARE = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAABCAQAAABeK7cBAAAA9klEQVR42mJ4//8/Axjs4bJiXKAwM7OxsiHqFAiJi//8/Azn5z4/H//8/AwMDAwM7OxM7Tz/b/AzEwszMRM7hEM/z/BwAKXVH4QVHtQ//8/MRAszPxAI3Hw/f/AwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwMA5R1TcQ8YmQAAAAASUVORK5CYII="
    # Obtenez les données binaires de l'image depuis le lien de données
    image_data = signatureSTAGIARE.split(",")[1].strip()
    image_bytes = base64.b64decode(image_data)
    temp_image = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    temp_image.write(image_bytes)
    temp_image.close()


    image1 = Image(temp_image.name, width=150, height=70)
    image1.hAlign = 'RIGHT'
    contenu.append(image1)


    contenu.append(Spacer(0.5, 40))
    contenu.append(Paragraph(texte71, style_texteCenter))
    contenu.append(Paragraph(texte72, style_texteCenter))
    contenu.append(Paragraph(texte73, style_texteCenter))


    # Générez le PDF
    doc.build(contenu)
    return fichier_pdf




def generer_AC_pdf(ids , nom, prenom, consultante, date_debut, date_fin, signature):

    fichier_pdf = f"{nom}-{prenom}-{ids}-AACC-ATTESTATION-SYNTHESE.pdf"
    doc = SimpleDocTemplate(fichier_pdf, pagesize=letter, 
                            rightMargin=72, leftMargin=72, 
                            topMargin=72, bottomMargin=18)
    styles = getSampleStyleSheet()

    contenu = []
    contenu.append(Spacer(0.5, 1))

    # Titre
    style_titre = styles['Title']
    style_titre.fontName = 'Helvetica'
    style_titre.fontSize = 18
    style_titre.spaceAfter = 20
    style_titre.textColor = colors.HexColor('#37456c')
    titre = Paragraph("ATTESTATION DE REMISE DE SYNTHESE DE BILAN DE COMPETENCES", style_titre)

    # Créer un tableau avec une seule cellule pour le titre
    tableau_titre = Table([[titre]], colWidths=[6 * inch], rowHeights=[1 * inch])

    # Appliquer un style au tableau pour ajouter une bordure
    style_tableau = TableStyle([('ALIGN', (0,0), (-1,-1), 'CENTER'),
                                ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
                                ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#37456c'))])  # 1 est l'épaisseur de la bordure

    tableau_titre.setStyle(style_tableau)

    # Ajouter le tableau du titre au contenu
    contenu.append(tableau_titre)
    contenu.append(Spacer(1.5, 25))
    # Corps du texte
    style_texte = styles['BodyText']
    style_texte.fontName = 'Helvetica'
    style_texte.fontSize = 12
    style_texte.textColor = colors.HexColor('#37456c')
    style_texte.leading = 24
    style_texte.alignment = 4

    styles2 = getSampleStyleSheet()
    style_texteCenter = styles2['BodyText']
    style_texteCenter.fontName = 'Helvetica'
    style_texteCenter.fontSize = 7
    style_texteCenter.textColor = colors.HexColor('#37456c')
    style_texteCenter.leading = 5
    style_texteCenter.alignment = 1

    styles3 = getSampleStyleSheet()
    style_texteLeft = styles3['BodyText']
    style_texteLeft.fontName = 'Helvetica'
    style_texteLeft.fontSize = 11
    style_texteLeft.textColor = colors.HexColor('#37456c')
    style_texteLeft.leading = 5
    style_texteLeft.alignment = 2

    """
    
    contenu.append(Paragraph(f"Nom: {nom}", style_texte))
    contenu.append(Paragraph(f"Prénom: {prenom}", style_texte))
    contenu.append(Paragraph(f"Âge: {age}", style_texte))
    """
    

    texte = f"""
    Je soussignée,  {consultante} , consultante en bilan de compétences au sein de l’organisme de formation AC CONSEILS, enregistré sous le numéro de déclaration d’activité 11755658275 auprès de la DIRECCTE (Direction régionale des entreprises, de la concurrence, de la consommation, du travail et de l’emploi) de l’Ile-de-France,
    """

    texte2 = f"""
    Certifie avoir accompagné {prenom} {nom} lors d’un bilan de compétences du {date_debut} au {date_fin}, conformément aux dispositions légales en vigueur, notamment celles prévues par le Code du travail.
    """
    
    texte3 = f"""
    À l'issue de cette démarche, le {date_fin}, une synthèse a été élaborée en collaboration. Elle reflète l'analyse des compétences, des aptitudes et des motivations de la personne concernée.
    """

    
    texte4 = f"""
    La synthèse du bilan de compétences a été présentée et transmise à {prenom} {nom} le {date_fin}.
    """

    texte5 = f"""
    Fait à Paris, le {date_fin}.
    """

    texte6 = f"""
    Mme {consultante}, 
    """
    texte61 =  f"""
    Consultante en Bilan de compétences
    """
    
    texte7 = f"""
    AC CONSEILS - 6 rue de Musset 75016 PARIS
    """

    texte71 = f"""
    N° SIRET 83131268100016 - N° Déclaration d'activité 11755658275
    """

    texte72 = f"""
    Organisme de Formation non assujetti à la TVA
    """

    
    # Ajouter le texte à la liste du contenu
    contenu.append(Paragraph(texte, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte2, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte3, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte4, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte5, style_texte))
    contenu.append(Spacer(0.5, 15))
    contenu.append(Paragraph(texte6, style_texteLeft))
    contenu.append(Paragraph(texte61, style_texteLeft))

    contenu.append(Spacer(0.5, 15))
    image = Image(signature, width=100, height=60)
    image.hAlign = 'RIGHT'
    contenu.append(image)

    contenu.append(Spacer(0.5, 15))
    contenu.append(Paragraph(texte7, style_texteCenter))
    contenu.append(Paragraph(texte71, style_texteCenter))
    contenu.append(Paragraph(texte72, style_texteCenter))



    # Générez le PDF
    doc.build(contenu)
    return fichier_pdf



def generer_ACpdfEMARGEMENT(ids , nom, prenom, consultante, date_debut, date_two, date_three, date_fin, signature , role, vocation):

    fichier_pdf = f"{nom}-{prenom}-{ids}-AACC--EMARGEMENT.pdf"
    doc = SimpleDocTemplate(fichier_pdf, pagesize=letter, 
                        rightMargin=50, leftMargin=50, 
                        topMargin=10, bottomMargin=10)


    styles = getSampleStyleSheet()

    contenu = []

    # Ajoutez une image (logo)
    
    if role == 'T1T':
        color = '37aff0'
        link = 'https://bilan.trouver-un-therapeute.fr'
        platformd = "https://i.ibb.co/5YqHDRb/therapeute.png"
    elif role == 'TS':
        # Talents-Solutions https://talents-solutions.com/
        color = '2153C1'
        link = 'https://talents.espace-competences.com/'
        platformd = "https://talents.espace-competences.com/wp-content/uploads/2023/05/Logo-talents-Solutions-1.png"
    elif role == 'TNET':
        color = '018B7F'
        link = 'https://espace-competences.com/'
        platformd = "https://i.ibb.co/3z7WJwg/image.png"
    elif role == 'ET':
        # EMPLOI TALENT https://emploi-talent.com/
        color = '094FA3'
        link = 'https://bilan.emploi-talent.com/'
        platformd = "https://i.ibb.co/cvM9g9C/image.png"
    elif role == 'FFR':
        color = '08b9e1'
        link = 'https://bilan.freelance-france.com/'
        platformd = "https://i.ibb.co/P1xScyk/image.png"
    else:
        color = '2153C1'
        link = 'https://bilan.trouver-un-candidat.com/'
        platformd = "https://i.ibb.co/YjrkZVn/image.png"



    #chemin_local = "./logo1.png"
    #urllib.request.urlretrieve(platformd, chemin_local)
    """image0 = Image(platformd, width=200, height=70)
    image0.hAlign = 'CENTER'
    contenu.append(image0)"""


    contenu.append(Spacer(0.5, 10))

    # Titre
    style_titre = styles['Title']
    style_titre.fontName = 'Helvetica'
    style_titre.fontSize = 22
    style_titre.spaceAfter = 20
    style_titre.textColor = colors.white
    titre = f""" FEUILLE D'EMARGEMENT \n Bilan de Compétences \n {date_debut} au {date_fin} """
    #titre = Paragraph(titre, style_titre)

    # Créer un tableau avec une seule cellule pour le titre
    tableau_titre = Table([[titre]], colWidths=[6 * inch], rowHeights=[1 * inch])

    style_tableau = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#' + color)),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#' + color)),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('FONTSIZE', (0, 0), (-1, -1), 22),
        ('LEADING', (0, 0), (-1, -1), 24)
    ])
    
    tableau_titre.setStyle(style_tableau)

    # Ajouter le tableau du titre au contenu
    contenu.append(tableau_titre)
    contenu.append(Spacer(1.5, 10))
    # Corps du texte
    style_texte = styles['BodyText']
    style_texte.fontName = 'Helvetica'
    style_texte.fontSize = 11
    style_texte.textColor = colors.HexColor('#37456c')
    style_texte.leading = 20
    style_texte.alignment = 4

    styles2 = getSampleStyleSheet()
    style_texteCenter = styles2['BodyText']
    style_texteCenter.fontName = 'Helvetica'
    style_texteCenter.fontSize = 10
    style_texteCenter.textColor = colors.HexColor('#37456c')
    style_texteCenter.leading = 15
    style_texteCenter.alignment = 1

    styles3 = getSampleStyleSheet()
    style_texteLeft = styles3['BodyText']
    style_texteLeft.fontName = 'Helvetica'
    style_texteLeft.fontSize = 11
    style_texteLeft.textColor = colors.HexColor('#37456c')
    style_texteLeft.leading = 5
    style_texteLeft.alignment = 2

    styles4 = getSampleStyleSheet()
    small_texteCenter = styles4['BodyText']
    small_texteCenter.fontName = 'Helvetica'
    small_texteCenter.fontSize = 7
    small_texteCenter.textColor = colors.HexColor('#37456c')
    small_texteCenter.leading = 3
    small_texteCenter.alignment = 1


        
    texte1 = f"""
    Nom et Prénom du titulaire : <b>{prenom} {nom} </b>
    """


    contenu.append(Paragraph(texte1, style_texte))
    contenu.append(Spacer(0.5, 5))

        
    texte2 = f"""
    <b>Rendez-vous avec la consultante</b>
    """
    texte3 = f"""
    <b>Signature</b>
    """
    texte4 = f"""
    {date_debut} <br /> Rdv 1 <br /><b>Mon itinéraire professionnel</b>
    """
    texte5 = f"""
    {date_two} <br /> Rdv 2 <br /><b>Mes motivations, ma personnalité</b>
    """
    texte6 = f"""
    {date_three} <br /> Rdv 3 <br /><b>Mes aspirations et mes freins</b>
    """
    texte7 = f"""
    {date_fin} <br /> Rdv 4 <br /><b>Mon projet professionnel </b>
    """



    #imaaaaaaaaaaaagegeeeeeeeeeeee
    
    if "data:image" in signature:
        signature = signature
    else:
        signature = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAABCAQAAABeK7cBAAAA9klEQVR42mJ4//8/Axjs4bJiXKAwM7OxsiHqFAiJi//8/Azn5z4/H//8/AwMDAwM7OxM7Tz/b/AzEwszMRM7hEM/z/BwAKXVH4QVHtQ//8/MRAszPxAI3Hw/f/AwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwMA5R1TcQ8YmQAAAAASUVORK5CYII="
    # Obtenez les données binaires de l'image depuis le lien de données
    image_data = signature.split(",")[1].strip()
    image_bytes = base64.b64decode(image_data)
    temp_image = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    temp_image.write(image_bytes)
    temp_image.close()
    signature = temp_image.name

    # Données pour le tableau
    
    image = Image(signature, width=60, height=25)
    nom_prenom = f"""{prenom} {nom}
    """
    image_with_text0 = [
        image,
        Paragraph(nom_prenom, small_texteCenter)
    ]

    data = [[Paragraph(texte2, style_texteCenter), Paragraph(texte3, style_texteCenter)],
            [Paragraph(texte4, style_texteCenter), image_with_text0],
            [Paragraph(texte5, style_texteCenter), image_with_text0],
            [Paragraph(texte6, style_texteCenter), image_with_text0],
            [Paragraph(texte7, style_texteCenter), image_with_text0]]

    # Créez le tableau
    table = Table(data, colWidths=[250, 250], rowHeights=65)

    # Définir le style du tableau
    style_tableau = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOX', (0, 0), (-1, -1), 1, colors.grey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('TEXTCOLOR', (0, 0), (1, 1), colors.black),  # Couleur du texte dans les deux premières cellules
        ('FONTSIZE', (0, 0), (1, 1), 12),  # Taille de la police dans les deux premières cellules
    ])

    table.setStyle(style_tableau)
    contenu.append(table)


    
    texte8 = f"""
    J’atteste m'être connecté(e) et avoir suivi les ateliers présents sur la plateforme d’e-learning {link}
    """
    contenu.append(Paragraph(texte8, style_texte))



    texte22 = f"""
    <b>Connexion à la plateforme d’e-learning</b>
    """
    texte23 = f"""
    <b>Signature</b>
    """
    texte71 = f"""
    Inter Rendez-vous <br /> Semaine du {date_debut} au {date_fin} 
    """

    image = Image(signature, width=60, height=25)
    nom_prenom = f"""{prenom} {nom}
    """
    image_with_text = [
        image,
        Paragraph("Signé(e) par "+nom_prenom, small_texteCenter)
    ]

    data2 = [[Paragraph(texte22, style_texteCenter), Paragraph(texte23, style_texteCenter)],
            [Paragraph(texte71, style_texteCenter), image_with_text]]

    # Créez le tableau50
    table2 = Table(data2, colWidths=[250, 250], rowHeights=50)
    style_tableau2 = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOX', (0, 0), (-1, -1), 1, colors.grey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('TEXTCOLOR', (0, 0), (1, 1), colors.black),  # Couleur du texte dans les deux premières cellules
        ('FONTSIZE', (0, 0), (1, 1), 12),  # Taille de la police dans les deux premières cellules
    ])

    


    table2.setStyle(style_tableau2)
    contenu.append(table2)

    texte70 = f"""
    AC CONSEILS - 6 rue de Musset 75016 PARIS
    """

    texte72 = f"""
    N° SIRET 83131268100016 - N° Déclaration d'activité 11755658275
    """

    texte73 = f"""
    Organisme de Formation non assujetti à la TVA
    """

    contenu.append(Spacer(0.5, 85))
    contenu.append(Paragraph(texte70, small_texteCenter))
    contenu.append(Paragraph(texte72, small_texteCenter))
    contenu.append(Paragraph(texte73, small_texteCenter))


    # Générez le PDF
    doc.build(contenu)
    return fichier_pdf


def generer_ACpdfFORMATION(ids , nom, prenom, consultante, date_debut, date_fin,  signatureGerant, signatureSTAGIARE , role, vocation):

    fichier_pdf = f"{nom}-{prenom}-{ids}--AACC-ATTESTATION-FIN.pdf"
    doc = SimpleDocTemplate(fichier_pdf, pagesize=letter, 
                        rightMargin=50, leftMargin=50, 
                        topMargin=10, bottomMargin=10)


    styles = getSampleStyleSheet()

    contenu = []

    # Ajoutez une image (logo)
    
    if role == 'T1T':
        color = '37aff0'
        link = 'https://bilan.trouver-un-therapeute.fr'
        platformd = "https://i.ibb.co/5YqHDRb/therapeute.png"
    elif role == 'TS':
        # Talents-Solutions https://talents-solutions.com/
        color = '2153C1'
        link = 'https://talents.espace-competences.com/'
        platformd = "https://talents.espace-competences.com/wp-content/uploads/2023/05/Logo-talents-Solutions-1.png"
    elif role == 'TNET':
        color = '018B7F'
        link = 'https://espace-competences.com/'
        platformd = "https://i.ibb.co/3z7WJwg/image.png"
    elif role == 'ET':
        # EMPLOI TALENT https://emploi-talent.com/
        color = '094FA3'
        link = 'https://bilan.emploi-talent.com/'
        platformd = "https://i.ibb.co/cvM9g9C/image.png"
    elif role == 'FFR':
        color = '08b9e1'
        link = 'https://bilan.freelance-france.com/'
        platformd = "https://i.ibb.co/P1xScyk/image.png"
    else:
        color = '2153C1'
        link = 'https://bilan.trouver-un-candidat.com/'
        platformd = "https://i.ibb.co/YjrkZVn/image.png"



    #chemin_local = "./logo1.png"
    #urllib.request.urlretrieve(platformd, chemin_local)
    """image0 = Image(platformd, width=200, height=70)
    image0.hAlign = 'CENTER'
    contenu.append(image0)"""


    contenu.append(Spacer(0.5, 40))

    # Titre
    style_titre = styles['Title']
    style_titre.fontName = 'Helvetica'
    style_titre.fontSize = 22
    style_titre.spaceAfter = 20
    style_titre.textColor = colors.white
    titre = Paragraph("ATTESTATION INDIVIDUELLE DE FIN DE FORMATION ", style_titre)

    # Créer un tableau avec une seule cellule pour le titre
    tableau_titre = Table([[titre]], colWidths=[6 * inch], rowHeights=[1 * inch])

    style_tableau = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#' + color)),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#' + color))
    ])
    
    tableau_titre.setStyle(style_tableau)

    # Ajouter le tableau du titre au contenu
    contenu.append(tableau_titre)
    contenu.append(Spacer(1.5, 55))
    # Corps du texte
    style_texte = styles['BodyText']
    style_texte.fontName = 'Helvetica'
    style_texte.fontSize = 11
    style_texte.textColor = colors.HexColor('#37456c')
    style_texte.leading = 20
    style_texte.alignment = 4

    styles2 = getSampleStyleSheet()
    style_texteCenter = styles2['BodyText']
    style_texteCenter.fontName = 'Helvetica'
    style_texteCenter.fontSize = 7
    style_texteCenter.textColor = colors.HexColor('#37456c')
    style_texteCenter.leading = 5
    style_texteCenter.alignment = 1

    styles3 = getSampleStyleSheet()
    style_texteLeft = styles3['BodyText']
    style_texteLeft.fontName = 'Helvetica'
    style_texteLeft.fontSize = 11
    style_texteLeft.textColor = colors.HexColor('#37456c')
    style_texteLeft.leading = 5
    style_texteLeft.alignment = 2

    styles4 = getSampleStyleSheet()
    style_sooulign = styles4['BodyText']
    style_sooulign.fontName = 'Helvetica'
    style_sooulign.fontSize = 11
    style_sooulign.textColor = colors.HexColor('#37456c')
    style_sooulign.leading = 20
    style_sooulign.alignment = 4
    style_sooulign.textDecoration = 'underline'


        
    texte1 = f"""
    Je soussigné(e) Madame Célia BEAUCOURT, représentant(e) légal(e) de l’organisme de formation AC CONSEILS enregistré sous le numéro de déclaration d’activité 11755658275 auprès de la DIRECCTE (Direction régionale des entreprises, de la concurrence, de la consommation, du travail et de l’emploi) de l’Ile-de-France atteste que {prenom} {nom}, {vocation} a suivi le Bilan de Compétences sur la période du {date_debut} au {date_fin}.
    """

    texte2 = f"""
    <u>Durée du Bilan de compétences : 24h00</u>
    """

    texte3 = f"""
    Intervenant(e) : Madame {consultante}
    """

    texte4 = f"""
    <u>Objectifs pédagogiques mentionnés dans le programme de formation :</u>
    """

    texte5 = f"""
    Le bilan de compétences est une réflexion professionnelle pour repérer les atouts, les axes de développement, et les traduire en objectifs de changement. Les bénéficiaires apprendront à mieux se connaître au travers de questionnaires de personnalité, à valoriser l’estime de soi et ainsi comprendre les choix, les causes de changement, les différentes expériences, les formations effectuées ou suivies qu’ils ont fait lors de leurs parcours professionnels.
    """

    texte6 = f"""
    Lors de la deuxième phase, l’exploration de l’histoire professionnelle et personnelle permettra d’identifier les compétences construites et de rédiger un portfolio de compétences.
    """

    texte61 =  f"""
    Identifier, clarifier et valider un projet de développement de compétences, ainsi que la rédaction d’un plan d’action en lien avec le développement de compétences.
    """

    texte7 = f"""
    Enfin, lors de la dernière phase du bilan de compétences, la consultante délivrera aux bénéficiaires les informations recueillies via leurs travaux effectués au préalable, analysera en synergie avec les stagiaires les compétences révélées et pour finir rédigera la synthèse du bilan de compétences.
    """

    texte71 = f"""
    AC CONSEILS - 6 rue de Musset 75016 PARIS
    """

    texte72 = f"""
    N° SIRET 83131268100016 - N° Déclaration d'activité 11755658275
    """

    texte73 = f"""
    Organisme de Formation non assujetti à la TVA
    """

    

    texte74 = f"""
    <u>Résultats de l’évaluation des acquis :</u>
    """

    texte75 = f"""
    Le participant a appris à mieux se connaître au travers des questionnaires de personnalité, à valoriser l’estime de soi et ainsi comprendre ses choix, les causes de changement, ses différentes expériences, ses formations effectuées ou suivies qu’il a fait lors de son parcours professionnel.
    """

    texte76 = f"""
    Le bilan de compétences a permis au bénéficiaire de valider son projet réaliste et réalisable et ainsi définir son plan d’actions pour la concrétisation de celui-ci.
    """

    texte77 = f"""
    Fait à Paris, le {date_fin}.
    """

    texte78 = f"""
    AC CONSEILS
    """

    texte79 = f"""
    Madame Célia BEAUCOURT
    """

    texte710 = f"""
    Gérant(e)
    """

    texte711 = f"""
    Signature
    """


    texte712 = f"""
    {prenom} {nom}
    """

    texte713 = f"""
    Signature
    """


    texte71 = f"""
    AC CONSEILS - 6 rue de Musset 75016 PARIS
    """

    texte72 = f"""
    N° SIRET 83131268100016 - N° Déclaration d'activité 11755658275
    """

    texte73 = f"""
    Organisme de Formation non assujetti à la TVA
    """

    # Ajouter le texte à la liste du contenu
    contenu.append(Paragraph(texte1, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte2, style_sooulign))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte3, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte4, style_sooulign))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte5, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte6, style_texte))
    contenu.append(Paragraph(texte61, style_texte))
    contenu.append(Spacer(0.5, 5))
    contenu.append(Paragraph(texte7, style_texte))
    contenu.append(Spacer(0.5, 45))
    contenu.append(Paragraph(texte71, style_texteCenter))
    contenu.append(Paragraph(texte72, style_texteCenter))
    contenu.append(Paragraph(texte73, style_texteCenter))
    contenu.append(Spacer(0.5, 80))
    contenu.append(Paragraph(texte74, style_sooulign))
    contenu.append(Paragraph(texte75, style_texte))
    contenu.append(Paragraph(texte76, style_texte))
    contenu.append(Spacer(0.5, 20))
    contenu.append(Paragraph(texte77, style_texte))
    contenu.append(Spacer(0.5, 30))
    contenu.append(Paragraph(texte78, style_texte))
    contenu.append(Paragraph(texte79, style_texte))
    contenu.append(Spacer(0.5, -15))
    contenu.append(Paragraph(texte710, style_texte))
    contenu.append(Spacer(0.5, -15))
    contenu.append(Paragraph(texte711, style_texte))
    

    image0 = Image('https://i.ibb.co/F6W98Rm/signature-beaucourt.png', width=120, height=70)
    image0.hAlign = 'LEFT'
    contenu.append(image0)
    image0 = Image(signatureGerant, width=120, height=80)
    image0.hAlign = 'LEFT'
    contenu.append(image0)

    


    contenu.append(Paragraph(texte712, style_texteLeft))
    contenu.append(Paragraph(texte713, style_texteLeft))
    contenu.append(Spacer(0.5, 5))

    if "data:image" in signatureSTAGIARE:
        signatureSTAGIARE = signatureSTAGIARE
    else:
        signatureSTAGIARE = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAABCAQAAABeK7cBAAAA9klEQVR42mJ4//8/Axjs4bJiXKAwM7OxsiHqFAiJi//8/Azn5z4/H//8/AwMDAwM7OxM7Tz/b/AzEwszMRM7hEM/z/BwAKXVH4QVHtQ//8/MRAszPxAI3Hw/f/AwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwMA5R1TcQ8YmQAAAAASUVORK5CYII="
    # Obtenez les données binaires de l'image depuis le lien de données
    image_data = signatureSTAGIARE.split(",")[1].strip()
    image_bytes = base64.b64decode(image_data)
    temp_image = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    temp_image.write(image_bytes)
    temp_image.close()


    image1 = Image(temp_image.name, width=150, height=70)
    image1.hAlign = 'RIGHT'
    contenu.append(image1)


    contenu.append(Spacer(0.5, 40))
    contenu.append(Paragraph(texte71, style_texteCenter))
    contenu.append(Paragraph(texte72, style_texteCenter))
    contenu.append(Paragraph(texte73, style_texteCenter))


    # Générez le PDF
    doc.build(contenu)
    return fichier_pdf











"""         --------------------------------                """
def run3():
    # Utilisation de la fonction pour générer un PDF avec une conception personnalisée
    nom = "WILLEMIN"
    prenom = "HELENE"
    consultante = "Tifenn GUINANT"
    date_debut = "20/9/2021"
    date_fin = "24/9/2021"
    role = "FFR"
    vocation = "Traducteur"
    
    date_two = "21/9/2021"
    date_three = "23/9/2021"


    signatureEP = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAABCAQAAABeK7cBAAAA9klEQVR42mJ4//8/Axjs4bJiXKAwM7OxsiHqFAiJi//8/Azn5z4/H//8/AwMDAwM7OxM7Tz/b/AzEwszMRM7hEM/z/BwAKXVH4QVHtQ//8/MRAszPxAI3Hw/f/AwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwMA5R1TcQ8YmQAAAAASUVORK5CYII="
    signatureGerant = "https://i.ibb.co/Cz89s7d/tampon-evolution.png"
    signatureSTAGIARE = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAABCAQAAABeK7cBAAAA9klEQVR42mJ4//8/Axjs4bJiXKAwM7OxsiHqFAiJi//8/Azn5z4/H//8/AwMDAwM7OxM7Tz/b/AzEwszMRM7hEM/z/BwAKXVH4QVHtQ//8/MRAszPxAI3Hw/f/AwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwM7OxsiHqFAiJiXKAwMA5R1TcQ8YmQAAAAASUVORK5CYII="
    
    #fichier_pdf = generer_pdf_PM_EMARGEMENT("0",nom, prenom, consultante, date_debut, date_two, date_three, date_fin, signatureEP ,role ,vocation )
    generer_EVpdfFORMATION(1073, nom, prenom, consultante, date_debut, date_fin, signatureGerant, signatureSTAGIARE ,role ,vocation )
    generer_EVpdfEMARGEMENT(1073, nom, prenom, consultante, date_debut, date_two, date_three, date_fin, signatureSTAGIARE ,role ,vocation )
    print(f"Fichier PDF généré : {nom}")


def get_image_url(role):
    if role == 'T1T':
        return "https://i.ibb.co/5YqHDRb/therapeute.png"
    elif role == 'et':
        return "https://i.ibb.co/D7ZvQ3p/ET.png"
    elif role == 'tnet':
        return "https://i.ibb.co/nggjcX9/therapeute-net.png"
    elif role == 'ts':
        return "https://i.ibb.co/JsNpsZP/talent-solution.png"
    else:
        return "https://i.ibb.co/vX2q2qW/logo-candidat.png"
    

def obtenir_image(prenom, line):
    if "Françoise" in prenom or "Francoise" in prenom  :
        return "https://i.ibb.co/wwK1R2Q/Fran-oise-MARGUET.png"
    elif "Martine" in prenom:
        return "https://i.ibb.co/fYsdQck/Martine-LDM.png"
    elif "Mathilde" in prenom:
        return "https://i.ibb.co/YtcCFrJ/Mathilde-GARCIA.png"
    elif "Sabine" in prenom:
        return "https://i.ibb.co/XbL0LST/Sabine-BENITHA.png"
    elif "Soumaya" in prenom:
        return "https://i.ibb.co/GkCVL8j/Soumay-TRIKI.png"
    elif "Thi-van" in prenom or "Thi-Van" in prenom  :
        return "https://i.ibb.co/sts3c5J/Thivan-MUONGHANE.png"
    elif "Tifenn" in prenom:
        return "https://i.ibb.co/kXxHkQJ/Tifenn-GUINANT.png"
    elif "Virginie" in prenom or "Virgine" in prenom or "Virignie" in prenom: 
        return "https://i.ibb.co/THdppGz/Virgnie-COURVOISIER.png"
    elif "Amélia" in prenom or "Amelia" in prenom:
        return "https://i.ibb.co/Yp7T6Bg/Am-lia-LAMRI.png"
    elif "Anne" in prenom:
        return "https://i.ibb.co/j4j1qR6/Anne-GRUAU.png"
    elif "Barbara" in prenom:
        return "https://i.ibb.co/Qf3nWhC/Barbara-LACRESSONNIERE.png"
    elif "Céline" in prenom or "Celine" in prenom:
        return "https://i.ibb.co/VpqQhPY/C-line-BONET.png"
    elif "Dovi" in prenom:
        return "https://i.ibb.co/0B4WSJC/Dovi-BURLANDY.png"
    elif "Estelle" in prenom:
        return "https://i.ibb.co/yFhD7pp/Estelle-RIVIERE.png"
    else:
        append_new_line("pdf sans signature consultante.txt", str(line)+'-' +str(prenom))
        return "https://i.ibb.co/dkQ6YVG/image.png"


def complete_csv():
    nom_fichier = 'c:/Users/fanti/Downloads/FE_EP_2023.csv' 
    donnees = lire_fichier_csv(nom_fichier)
    print('')
    for item in range(int(1), 1865):
        linkkk = linecache.getline(r"d:/Documents/Website/therapeute.net/nom-jan.txt", item)
        linkkk = linkkk.replace('\n', '')
        input(linkkk)
    for ligne in donnees:
        if len(ligne) > 0 and ligne[0] == linkkk:
            input('""555')

        


def run():
    dernier_etape_processus = "create-pdf.txt"
    try:
        with open(dernier_etape_processus, 'r') as file:
            etape_processus = str(file.read())
    except FileNotFoundError:
        etape_processus = 1

    nom_fichier = 'c:/Users/fanti/Downloads/celia-ac-ep-ev.csv'
    #for ligne in lire_fichier_csv(nom_fichier):
    donnees = lire_fichier_csv(nom_fichier)
    
    for i in range(int(etape_processus), len(donnees)+1):
        ligne = donnees[i]

        nom = str(ligne[0])
        iddd = str(ligne[1])
        prenom = str(ligne[4])
        consultante = str(ligne[9])
        date_debut = str(ligne[5])
        date_two = str(ligne[6])
        date_three = str(ligne[7])
        date_fin = str(ligne[8])
        role = str(ligne[10])
        vocation = str(ligne[11])
        email = str(ligne[12])
        AC_pc_ev = str(ligne[15])
        prenom_consultante = consultante.split()[0]
        signature = obtenir_image(prenom_consultante, i)
        signatureSTAGIARE = (str(ligne[19]))
        signatureGerant_EV = "https://i.ibb.co/Cz89s7d/tampon-evolution.png"
        signatureGerant_PM = "https://i.ibb.co/BjWhsvN/tampon-pm.png"
        signatureGerant_AC = "https://i.ibb.co/ZWSd6zB/tampon-ac.png"
        
        

        if "FOUND" in email:
            pass
        else:
            if AC_pc_ev == "AC":
                generer_AC_pdf(str(i),(nom), prenom, consultante, date_debut, date_fin, signature)
                generer_ACpdfEMARGEMENT(i , nom, prenom, consultante, date_debut, date_two, date_three, date_fin, signatureSTAGIARE , role, vocation)
                generer_ACpdfFORMATION(i, nom, prenom, consultante, date_debut, date_fin, signatureGerant_AC, signatureSTAGIARE ,role ,vocation )
            elif AC_pc_ev == "EP":
                generer_EV_pdf(str(i),(nom), prenom, consultante, date_debut, date_fin, signature)
                generer_EVpdfEMARGEMENT(i , nom, prenom, consultante, date_debut, date_two, date_three, date_fin, signatureSTAGIARE , role, vocation)
                generer_EVpdfFORMATION(i, nom, prenom, consultante, date_debut, date_fin, signatureGerant_EV, signatureSTAGIARE ,role ,vocation )
            elif AC_pc_ev == "PM":
                generer_PMpdf(str(i),(nom), prenom, consultante, date_debut, date_fin, signature)
                generer_pdf_PM_EMARGEMENT(i , nom, prenom, consultante, date_debut, date_two, date_three, date_fin, signatureSTAGIARE , role, vocation)
                generer_PMpdfFORMATION(i, nom, prenom, consultante, date_debut, date_fin, signatureGerant_PM, signatureSTAGIARE ,role ,vocation )
            else:
                append_new_line("IEERREUR-AC-PM-.txt", str(nom))





            """generer_EV_pdf(str(i),(nom), prenom, consultante, date_debut, date_fin, signature)
            #generer_PMpdf(str(i),(nom), prenom, consultante, date_debut, date_fin, signature)
            #generer_EVpdfFORMATION(i, nom, prenom, consultante, date_debut, date_fin, signatureGerant_EV, signatureSTAGIARE ,role ,vocation )
            #generer_PMpdfFORMATION(i, nom, prenom, consultante, date_debut, date_fin, signatureGerant_PM, signatureSTAGIARE ,role ,vocation )
            #fichier_pdf = generer_pdfFORMATION(i, nom, prenom, consultante, date_debut, date_fin, signatureGerant, signatureSTAGIARE ,role ,vocation )

            #generer_EVpdfEMARGEMENT(i , nom, prenom, consultante, date_debut, date_two, date_three, date_fin, signatureSTAGIARE , role, vocation)

            resultat = recherche_ligne_texte("./idddeja.txt", iddd)
            
            if resultat == 1:
                pass
            else:
                append_new_line(r'save_all_in_already_day.txt', str(iddd))
                generer_pdf_PM_EMARGEMENT(i , nom, prenom, consultante, date_debut, date_two, date_three, date_fin, signatureSTAGIARE , role, vocation)"""
            
            with open(dernier_etape_processus, 'w') as file:
                file.write(str(i))

        
        input(nom)
        nom = ligne[0]
        id = ligne[1]
        nom2 = ligne[2]
        prenom1 = ligne[3]
        prenom2 = ligne[4]
        date_debut = ligne[5]
        date_fin = ligne[6]
        autre_date = ligne[7]
        autre_date2 = ligne[8]
        nom_complet = ligne[9]
        role = ligne[10]
        vocation = ligne[11]
        email = ligne[12]
        telephone = ligne[13]
        adresse = ligne[14]
        type = ligne[15]

run()