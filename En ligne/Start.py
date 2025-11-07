# Programme de démarrage du menu de Nox Villae

import pygame # Librairie pour créer notre jeu

class Window:
    def __init__ (self,screen):
        self.screen = screen # Avoir les infos sur l'écran
        self.running = True # Pour couper au moment voulu

        # Titre de la fenêtre
        pygame.display.set_caption("Nox Villae")


    def run(self):
        # Lancer le jeu
        self.loading()

    def loading(self):
        from Menus import Menus

        menus = Menus(self.screen) ## Initialiser Menu
        menus.run() ## Lancer Menu

pygame.init() # Initialisation du module Pygame

screen = pygame.display.set_mode((0,0)) # Définir un écran ( (0,0) -> prends toute la taille de l'écran)
game = Window(screen) # Appeller la classe
game.run() # Lancer le jeu

pygame.quit() # Couper tous les programmes pygame en cours 