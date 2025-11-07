import pygame
import os
from pathlib import Path

directory = Path(__file__).parent ##Chemin d'accès vers le programme

calqueOeil = pygame.image.load(f'{directory}/Ressource/Sprite/calqueOeil.png')

character = { # ["Voyante"/"Sorciere"]
    "Voyante":pygame.image.load(f'{directory}/Ressource/Sprite/Voyante.png'),
    "Sorciere":pygame.image.load(f'{directory}/Ressource/Sprite/Sorciere.png')
}

arbre = { #["Jour"/"Nuit"]
    "Jour":pygame.image.load(f'{directory}/Ressource/Sprite/arbre/Jour.png'),
    "Nuit":pygame.image.load(f'{directory}/Ressource/Sprite/arbre/Nuit.png'),
}

fondMap = { # ["Jour"/"Nuit"/"DansLaTente"]
    "Jour":pygame.image.load(f'{directory}/Ressource/Sprite/fondMap/Jour.png'),
    "Nuit":pygame.image.load(f'{directory}/Ressource/Sprite/fondMap/Nuit.png'),
    "DansLaTente":pygame.image.load(f'{directory}/Ressource/Sprite/fondMap/DansLaTente.png')
}

feu = { # ["Jour"] / ["Nuit"][n]
    "Jour":pygame.image.load(f'{directory}/Ressource/Sprite/feu/feu_jour.png'),
    "Nuit":[pygame.image.load(f'{directory}/Ressource/Sprite/feu/feu_nuit{b}.png') for b in range(1,5)]
}

elPyromaniac = {
    "Torche":pygame.image.load(f'{directory}/Ressource/Sprite/torche.png'),
    "Baril":pygame.image.load(f'{directory}/Ressource/Sprite/baril.png')
}

potion = {
    "Vie":pygame.image.load(f'{directory}/Ressource/Sprite/potionVie.png'),
    "Mort":pygame.image.load(f'{directory}/Ressource/Sprite/potionMort.png')
}

iconePerso = [ #[n]
    pygame.image.load(f'{directory}/Ressource/Sprite/icones persos/perso{a}.png') for a in range(1,7)   
]

tente = { #["Nuit"/"Jour"]["Gauche"/"Droite"/"Détruite"]
    "Nuit":{
        "Gauche":pygame.image.load(f'{directory}/Ressource/Sprite/tente/GaucheNuit.png'),
        "Droite":pygame.image.load(f'{directory}/Ressource/Sprite/tente/DroiteNuit.png'),
        "Détruite":pygame.image.load(f'{directory}/Ressource/Sprite/tente/DetruiteNuit.png'),
    },
    "Jour":{
        "Gauche":pygame.image.load(f'{directory}/Ressource/Sprite/tente/Gauche.png'),
        "Droite":pygame.image.load(f'{directory}/Ressource/Sprite/tente/Droite.png'),
        "Détruite":pygame.image.load(f'{directory}/Ressource/Sprite/tente/Detruite.png'),
    }
}

buche = { #["Nuit"/"Jour"]["Haut"/"Gauche"/"Droite"]
    "Nuit":{ 
        "Haut":pygame.image.load(f'{directory}/Ressource/Sprite/buche/haut_nuit.png'),
        "Gauche":pygame.image.load(f'{directory}/Ressource/Sprite/buche/droite_nuit.png'),
        "Droite":pygame.image.load(f'{directory}/Ressource/Sprite/buche/gauche_nuit.png')
    },
    "Jour":{
        "Haut":pygame.image.load(f'{directory}/Ressource/Sprite/buche/haut_jour.png'),
        "Gauche":pygame.image.load(f'{directory}/Ressource/Sprite/buche/gaucheETdroit.png'),
        "Droite":pygame.image.load(f'{directory}/Ressource/Sprite/buche/gaucheETdroit.png')
    },
}

loup = { # ["Run"/"Static"]["Arriere"/"Avant"/"Droite"/"Gauche"]
    "Run":{
        "Arriere" : [pygame.image.load(f'{directory}/Ressource/Sprite/Loup/ArriereRun{b}.png') for b in range(1,5)],
        "Avant" : [pygame.image.load(f'{directory}/Ressource/Sprite/Loup/AvantRun{b}.png') for b in range(1,5)],
        "Droite" : [pygame.image.load(f'{directory}/Ressource/Sprite/Loup/DroiteRun{b}.png') for b in range(1,5)],
        "Gauche" : [pygame.image.load(f'{directory}/Ressource/Sprite/Loup/GaucheRun{b}.png') for b in range(1,5)]
    },
    "Static":{
        "Arriere" : [pygame.image.load(f'{directory}/Ressource/Sprite/Loup/Arriere{b}.png') for b in range(1,3)],
        "Avant" : [pygame.image.load(f'{directory}/Ressource/Sprite/Loup/Avant{b}.png') for b in range(1,3)],
        "Droite" : [pygame.image.load(f'{directory}/Ressource/Sprite/Loup/Droite{b}.png') for b in range(1,3)],
        "Gauche" : [pygame.image.load(f'{directory}/Ressource/Sprite/Loup/Gauche{b}.png') for b in range(1,3)]
    }
}

logo = { # ["Prochain"/"Precedent"/"Home"/"Moins"/"Plus"/"Id"/"Exit"/"Engrenage"/"Disquette"] / ["Bouton"]["On"/"Off"]
    "Prochain" : pygame.image.load(f'{directory}/Ressource/Sprite/logoProchain.png'),
    "Precedent" : pygame.image.load(f'{directory}/Ressource/Sprite/logoPrecedent.png'),
    "Home" : pygame.image.load(f'{directory}/Ressource/Sprite/home.png'),
    "Moins" : pygame.image.load(f'{directory}/Ressource/Sprite/moins.png'), #A CHANGER
    "Plus" : pygame.image.load(f'{directory}/Ressource/Sprite/logoPrecedent.png'), #A CHANGER
    "Id" : pygame.image.load(f'{directory}/Ressource/Sprite/id.png'),
    "Exit" : pygame.image.load(f'{directory}/Ressource/Sprite/exitButton.png'),
    "Engrenage":pygame.image.load(f'{directory}/Ressource/Sprite/engrenage.png'),
    "Disquette":pygame.image.load(f'{directory}/Ressource/Sprite/disquette.png'),
    "Aucun":pygame.image.load(f'{directory}/Ressource/Sprite/SigneBarre.png'),
    "Bouton":{
        "On":pygame.image.load(f'{directory}/Ressource/Sprite/boutonOn.png'),
        "Off":pygame.image.load(f'{directory}/Ressource/Sprite/boutonOff.png'),
    },
    "Fond":pygame.image.load(f'{directory}/Ressource/Sprite/logoFondMenus.png')
}

perso = [ #[n]["Run"/"Static"]["Arriere"/"Avant"/"Droite"/"Gauche"]
    {
        "Run":{
            "Arriere" : [pygame.image.load(f'{directory}/Ressource/Sprite/perso{a}/ArriereRun{b}.png') for b in range(1,5)],
            "Avant" : [pygame.image.load(f'{directory}/Ressource/Sprite/perso{a}/AvantRun{b}.png') for b in range(1,5)],
            "Droite" : [pygame.image.load(f'{directory}/Ressource/Sprite/perso{a}/DroiteRun{b}.png') for b in range(1,5)],
            "Gauche" : [pygame.image.load(f'{directory}/Ressource/Sprite/perso{a}/GaucheRun{b}.png') for b in range(1,5)]
        },
        "Static":{
            "Arriere" : [pygame.image.load(f'{directory}/Ressource/Sprite/perso{a}/Arriere{b}.png') for b in range(1,3)],
            "Avant" : [pygame.image.load(f'{directory}/Ressource/Sprite/perso{a}/Avant{b}.png') for b in range(1,3)],
            "Droite" : [pygame.image.load(f'{directory}/Ressource/Sprite/perso{a}/Droite{b}.png') for b in range(1,3)],
            "Gauche" : [pygame.image.load(f'{directory}/Ressource/Sprite/perso{a}/Gauche{b}.png') for b in range(1,3)]
        }
    } for a in range(1,7)
]