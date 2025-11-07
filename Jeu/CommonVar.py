import json
import threading
import os
import random
from pathlib import Path

import RoleDefinition
from NameGenerator import generate_random_name
from SpriteBank import *

directory = Path(__file__).parent ##Chemin d'accès vers le programme

class CommonVar:
    def __init__(self):
        self.jsonLock = threading.Lock()

        self.commonVariable = [
            'journeyLongivity',
            'showClock',
            'maximumEntity',
            'saveChosen',
        ]
        
        self.savingVariable = [
            'creatureStartingNumber',
            'creatureNumber',
            'creaturePositions',
            'creatureId',
            'creatureDestinations',
            'creatureSens',
            'creatureSprites',
            'creatureRoles',
            'creatureMates',
            'creatureEvilness',
            'creatureTent',
            'creatureTentState',
            'creatureTrust',
            'straightReproduction',
            'villainPart',
            'villainPartPercentage',
            'cycle',
            'timeRemaining',
            'playType',
            'mayor',
            'witchRemainingPotion',
            'witchUseHeal',
            'protected',
            'foxPower',
            'lovers',
            'pyromaniacTarget'
        ]

        global commonDico
        commonDico = dict()

        global savingDico
        savingDico = dict()

        for var in self.commonVariable:
            setattr(self,var,None)
            commonDico[var] = None

        for var in self.savingVariable:
            setattr(self,var,None)
            savingDico[var] = None

        self.update_common_var()
        self.update_saving_var()

    def add_common_var(self,data):
        for var in self.commonVariable:
            setattr(self,var,data[var])
            commonDico[var] = data[var]
    
    def add_saving_var(self,data):
        for var in self.savingVariable:
            setattr(self,var,data[var])
            savingDico[var] = data[var]

    def update_common_var(self):
        commonPath = f"{directory}/Ressource/Save/Settings.json" ##Chemin d'acces vers le fichier Settings
        try : 
            with self.jsonLock:
                with open(commonPath,"r") as f:
                    data = json.load(f) ##Ouvre le fichier et enregistre son dictionnaire dans data
                    self.add_common_var(data)

        except FileNotFoundError: print('Fichier Settings.json introuvable dans le dossier Save')

    def update_saving_var(self):
        savingPath = f"{directory}/Ressource/Save/Save{commonDico['saveChosen']}.json" ##Chemin d'acces vers le ficher de sauvegarde
        try:
            with self.jsonLock:
                if os.path.exists(savingPath) and os.path.getsize(savingPath) > 0:
                    with open(savingPath, "r") as f:
                        try:
                            data = json.load(f)  # Charge le JSON
                            self.add_saving_var(data)
                        except json.JSONDecodeError:
                            data = savingDico
                else:
                    data = savingDico
        except FileNotFoundError: print('fichier introuvable')

    def update_common_json(self):
        commonPath = f"{directory}/Ressource/Save/Settings.json" ##Chemin d'acces vers le fichier

        with self.jsonLock:
            with open(commonPath, "w") as f:
                json.dump(commonDico, f, indent=4) ##Créé un fichier et enregistre data1 dedans

    def update_saving_json(self):
        if commonDico['saveChosen']:
            savingPath = f"{directory}/Ressource/Save/Save{commonDico['saveChosen']}.json" ##Chemin d'acces vers le fichier

            with self.jsonLock:
                with open(savingPath, "w") as f:
                    if savingDico:
                        json.dump(savingDico, f, indent=4) ##Créé un fichier et enregistre data1 dedans
                        f.flush()
                        os.fsync(f.fileno())
                    
    def nJson(self):
        for a, a, files in os.walk(f"{directory}/Ressource/Save"):
            if 'desktop.ini' in files:
                files.pop(0)
            files.pop(-1) ## On retire Settings.json
            if 'SaveNone.json' in files:
                self.del_save(None)
                files.pop(-1)
            return(len(files))
        
    def create_new_save(self):
        if self.nJson() < 3:
            commonDico['saveChosen'] = self.nJson() + 1
            self.new_save()
            self.update_saving_json()

    def new_save(self):
        savingDico['creatureStartingNumber'] = 6
        savingDico['creatureNumber'] = 6
        savingDico['creaturePositions'] = [[500,500] for _ in range(6)]
        savingDico['creatureId'] = [generate_random_name() for _ in range(6)]
        savingDico['creatureDestinations'] = [None for _ in range(6)]
        savingDico['creatureSens'] = [None for _ in range(6)]
        savingDico['creatureSprites'] = [random.randint(1,6) for _ in range(6)]
        savingDico['creatureRoles'] = [None for _ in range(6)]
        savingDico['creatureMates'] = [[] for _ in range(6)]
        savingDico['creatureEvilness'] = [100] + [random.randint(0,200) for _ in range(6)]
        savingDico['creatureTent'] = []
        for i in range(6):
            tentPos = random.randint(0,34)
            while tentPos in savingDico['creatureTent']:
                tentPos = random.randint(0,34)
            savingDico['creatureTent'].append(tentPos)
        savingDico['creatureTentState'] = [True for _ in range(6)]
        savingDico['creatureTrust'] = [[100 for _ in range(6)] for _ in range(6)]
        savingDico['cycle'] = 1
        savingDico['witchRemainingPotion'] = [True,True]
        savingDico['witchUseHeal'] = False
        savingDico['protected'] = None
        savingDico['foxPower'] = True
        savingDico['lovers'] = None
        savingDico['pyromaniacTarget'] = []
        RoleDefinition.definition()

    def del_save(self,n):
        if self.nJson() != 1:
            finalDel = 3
            if n != 3:
                if n == 1:
                    if self.nJson() > 1:
                        data = self.openSave(2)
                        savingPath = f"{directory}/Ressource/Save/Save1.json" ##Chemin d'acces vers le fichier
                        with self.jsonLock:
                            with open(savingPath, "w") as f:
                                json.dump(data, f, indent=4) ##Créé un fichier et enregistre data1 dedans
                                f.flush()
                                os.fsync(f.fileno())

                if self.nJson() > 2:
                    data = self.openSave(3)
                    savingPath = f"{directory}/Ressource/Save/Save2.json" ##Chemin d'acces vers le fichier
                    with self.jsonLock:
                        with open(savingPath, "w") as f:
                            json.dump(data, f, indent=4) ##Créé un fichier et enregistre data1 dedans
                            f.flush()
                            os.fsync(f.fileno())
                else:
                    finalDel -= 1
                

            savingPath = f"{directory}/Ressource/Save/Save{finalDel}.json" ##Chemin d'acces vers le fichier
            try:   
                os.remove(savingPath)
            except FileNotFoundError: print('fichier introuvable')

            commonDico['saveChosen'] = finalDel-1
        else:
            self.new_save()
            self.update_saving_json()

    def openSave(self,n):
        savingPath = f"{directory}/Ressource/Save/Save{n}.json" ##Chemin d'acces vers le fichier
        try:
            with self.jsonLock:
                if os.path.exists(savingPath) and os.path.getsize(savingPath) > 0:
                    with open(savingPath, "r") as f:
                        try:
                            data = json.load(f)  # Charge le JSON
                            return data
                        except json.JSONDecodeError: 
                            print('probleme dans votre fichier json')
                            return savingDico
                else: 
                    print('votre fichier json est vide ou introuvable')
                    return savingDico
        except FileNotFoundError: 
            print('fichier introuvable')
            return savingDico
