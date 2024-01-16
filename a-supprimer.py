
import linecache
import random

# pour colorer les prints
import colorama
import os
import os.path
import re
import time
import json
import pymongo
import json


# Lecture des fichiers 1 et 2
with open('fichier1.txt', 'r') as file1, open('fichier2.txt', 'r') as file2:
    lines1 = file1.readlines()
    lines2 = file2.readlines()

# Suppression des caractères de saut de ligne
lines1 = [line.strip() for line in lines1]
lines2 = [line.strip() for line in lines2]

# Création d'un ensemble pour stocker les lignes uniques
unique_lines = set()

# Ajout des lignes du fichier 1 dans l'ensemble
for line in lines1:
    if line not in lines2:
        unique_lines.add(line)

# Ajout des lignes du fichier 2 dans l'ensemble
for line in lines2:
    if line not in lines1:
        unique_lines.add(line)

# Écriture des lignes uniques dans le fichier 3
with open('fichier3.txt', 'w') as file3:
    file3.write('\n'.join(unique_lines))

print('Fichier 3 créé avec succès !')
