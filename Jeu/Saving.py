import json
import os
import threading
from pathlib import Path
 
directory = Path(__file__).parent ##Chemin d'accès vers le programme
os.system(f'cd {directory}')
jsonLock = threading.Lock()

def saveData(data1:dict,n:int):
    assert 1 <= n <= 3,"Il ne peut y avoir qu'entre 1 et 3 sauvegarde"
    path = f"{directory}/Ressource/Save/Save{n}.json" ##Chemin d'acces vers le fichier

    data = openData(n)
    if data != '':
        with jsonLock:
            with open(path, "w") as f:
                json.dump(data1, f, indent=4) ##Créé un fichier et enregistre data1 dedans
    
    ref = openData(n)
    assert data1 == ref,"c'est bien ici que tu t'es foiré"

def openData(n:int):
    assert 1 <= n <= 3,"Il ne peut y avoir qu'entre 1 et 3 sauvegarde"
    path = f"{directory}/Ressource/Save/Save{n}.json" ##Chemin d'acces vers le fichier

    try : 
        with jsonLock:
            if os.path.exists(path) and os.path.getsize(path) > 0:
                with open(path,"r") as f:
                    data = json.load(f) ##Ouvre le fichier et enregistre son dictionnaire dans data

        return data
    except FileNotFoundError : print(f'Fichier Save{n} introuvable')

def updateData(key:str,el,n:int,dominant:bool):
    assert 1 <= n <= 3,"Il ne peut y avoir qu'entre 1 et 3 sauvegarde"
    path = f"{directory}/Ressource/Save/Save{n}.json" ##Chemin d'acces vers le fichier

    save = openData(n) ##Ouvre le fichier
    if not key in save.keys() or dominant: ##Si il n'existe pas de clé key ou si on a choisit de l'écraser
        save[key] = el
        saveData(save,n) ##Enregistre le nouveau save dans le fichier Json

def delData(n:int):
    path = f"{directory}/Ressource/Save/Save3.json"
    try : ##Pour éviter d'avoir une erreur avec os.remove()
        if n == 2:
            data = openData(3)
            saveData(data,2)
        elif n == 1:
            data = openData(2)
            saveData(data,1)
            data = openData(3)
            saveData(data,2)

        os.remove(path) ##Supprimer le fichier
    except FileNotFoundError: print(f'Fichier Save{n} introuvable')

def nJson():
    for a, a, files in os.walk(f"{directory}/Ressource/Save"):
        if 'desktop.ini' in files:
            files.pop(0)
        files.pop(-1) ## On retire Settings.json
        return(len(files))