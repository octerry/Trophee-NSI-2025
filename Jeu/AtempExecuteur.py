import pygame
from pathlib import Path

#from PyromaniacChoice import PyromaniacChoice
#from LittleGirlSpying import LittleGirlSpying
#from WitchChoice import WitchChoice
from ClairvoyantReveal import ClairvoyantReveal

import CommonVar
commonVar = CommonVar.CommonVar()
import CommonFonction
import Font

class Window:
    def __init__(self,screen):
        self.screen = screen ##Avoir les informations sur l'écran (taille)
        self.running = True ##Pour le couper quand on veut

        self.clock = pygame.time.Clock()
        self.clock.tick(30)

        #self.menus = Menus(self.screen,self)
        #self.game = Game(self.screen)
        
        #self.pyromaniacChoice = PyromaniacChoice(screen)
        
        #self.littleGirlSpying = LittleGirlSpying(screen)
        #self.littleGirlSpying.target = 0

        #self.witchChoice = WitchChoice(screen)

        self.clairvoyantReveal = ClairvoyantReveal(screen)

        pygame.display.set_caption("Nox Villae (Mode Développeur)")

    def handling_event(self): ##Tous les évenements (joueur -> jeu) seront ici
        for event in pygame.event.get():
            if event.type == pygame.QUIT: ##Si le joueur appuie sur la croix de la fenetre
                self.running = False ##Le jeu s'arrete

    def update(self): ##Tous les trucs à actualiser (colition,interractions automatiques) seront ici'
        pass

    def display(self): ##Toutes les fonctions pygame pour afficher seront ici
        pygame.display.flip() ##Actualiser

    def run(self):
        '''while self.running:
            self.handling_event()
            #self.menus.run()
            #self.game.run(self)
            self.PyromaniacChoice.run()
            self.display()'''
        #testing_one = self.pyromaniacChoice
        #testing_one = self.littleGirlSpying
        #testing_one = self.witchChoice
        testing_one = self.clairvoyantReveal

        CommonFonction.fade_in(testing_one, 60)

pygame.init()
# AJOUTER pygame.FULLSCREEN QUAND ON AURA FINI DE CODER
screen = pygame.display.set_mode((0,0)) ##Définir un écran ((0,0) c'est pour dire plein écran et pygame.FULLSCREEN pour être considéré comme plein écran par Windows)
game = Window(screen) ##Appeller la classe
game.run() ##Lancer le jeu

commonVar.update_saving_json()
pygame.quit()