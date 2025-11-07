import pygame

from CommonVar import directory
import SpriteBank

perso = [
    [
        {
            "Arriere" : [SpriteBank.perso[a]['Run']['Arriere'][b] for b in range(4)],
            "Avant" : [SpriteBank.perso[a]['Run']['Avant'][b] for b in range(4)],
            "Droite" : [SpriteBank.perso[a]['Run']['Droite'][b] for b in range(4)],
            "Gauche" : [SpriteBank.perso[a]['Run']['Gauche'][b] for b in range(4)]
        },
        {
            "Arriere" : [SpriteBank.perso[a]['Static']['Arriere'][b] for b in range(2)],
            "Avant" : [SpriteBank.perso[a]['Static']['Avant'][b] for b in range(2)],
            "Droite" : [SpriteBank.perso[a]['Static']['Droite'][b] for b in range(2)],
            "Gauche" : [SpriteBank.perso[a]['Static']['Gauche'][b] for b in range(2)]
        }
     ] for a in range(6)
]

feu = [
    pygame.image.load(f'{directory}/Ressource/Sprite/feu/feu_jour.png'),
    [pygame.image.load(f'{directory}/Ressource/Sprite/feu/feu_nuit{b}.png') for b in range(1,5)]
]


loup = [
    {
        "Arriere" : [pygame.image.load(f'{directory}/Ressource/Sprite/Loup/ArriereRun{b}.png') for b in range(1,5)],
        "Avant" : [pygame.image.load(f'{directory}/Ressource/Sprite/Loup/AvantRun{b}.png') for b in range(1,5)],
        "Droite" : [pygame.image.load(f'{directory}/Ressource/Sprite/Loup/DroiteRun{b}.png') for b in range(1,5)],
        "Gauche" : [pygame.image.load(f'{directory}/Ressource/Sprite/Loup/GaucheRun{b}.png') for b in range(1,5)]
    },
    {
        "Arriere" : [pygame.image.load(f'{directory}/Ressource/Sprite/Loup/Arriere{b}.png') for b in range(1,3)],
        "Avant" : [pygame.image.load(f'{directory}/Ressource/Sprite/Loup/Avant{b}.png') for b in range(1,3)],
        "Droite" : [pygame.image.load(f'{directory}/Ressource/Sprite/Loup/Droite{b}.png') for b in range(1,3)],
        "Gauche" : [pygame.image.load(f'{directory}/Ressource/Sprite/Loup/Gauche{b}.png') for b in range(1,3)]
    }
]


tente = [
    [
        pygame.image.load(f'{directory}/Ressource/Sprite/tente/GaucheNuit.png'),
        pygame.image.load(f'{directory}/Ressource/Sprite/tente/DroiteNuit.png'),
        pygame.image.load(f'{directory}/Ressource/Sprite/tente/DetruiteNuit.png'),
    ],
    [
        pygame.image.load(f'{directory}/Ressource/Sprite/tente/Gauche.png'),
        pygame.image.load(f'{directory}/Ressource/Sprite/tente/Droite.png'),
        pygame.image.load(f'{directory}/Ressource/Sprite/tente/Detruite.png'),
    ]
]

