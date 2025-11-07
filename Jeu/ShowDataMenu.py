import pygame
import math

from CommonVar import directory
from Keybinds import keybinds
from Converter import Converter
import Font
import SpriteBank

class ShowDataMenu:
    def __init__(self,screen,background):
        self.screen = screen
        self.background = background
        self.running = False
        self.generalSettings = True ## True : parametres généraux , False : configuration des touches
        self.converter = Converter(self.screen)

        self.homeIconImage = SpriteBank.logo['Home']
        self.homeIconRect = self.homeIconImage.get_rect()
        self.homeIconImage = pygame.transform.scale(self.homeIconImage, (self.converter.conv_x(100),self.converter.conv_y(100)))
        self.homeIconBgSurface = pygame.Surface((self.converter.conv_x(200),self.converter.conv_y(200)), pygame.SRCALPHA)
        self.homeIconBgAlpha = 120

        self.menuTitleFont = pygame.font.Font(Font.jaini, self.converter.conv_y(150))
        self.menuTitleText = self.menuTitleFont.render("Données de partie",True,(240,240,240))
        self.menuTitleRect = self.menuTitleText.get_rect(center=(self.screen.get_width()/2,self.converter.conv_y(150)))
        self.menuTitleBgSurface = pygame.Surface((self.screen.get_width(),self.converter.conv_y(300)), pygame.SRCALPHA)
        
    def hover_circle(self, event, circle_center, circle_radius):
        mouse_pos = pygame.mouse.get_pos()
        if math.dist(mouse_pos, circle_center) < circle_radius: # Quand la souris rentre dans le cercle
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return True,True # Touche : True , Clique : True
            return True,False # Touche : True , Clique : False
        else:
            return False,False # Touche : False

    def handling_event(self): ##Tous les évenements (joueur -> jeu) seront ici
        for event in pygame.event.get():
            if event.type == pygame.QUIT: ##Si le joueur appuie sur la croix de la fenetre
                pygame.quit() ##Le jeu s'arrete
            
            keys = pygame.key.get_pressed()
            if keys[keybinds['openMenu']]:
                self.running = False
            
            survol = False

            if self.hover_circle(event, (self.converter.conv_x(150),self.screen.get_height() - self.converter.conv_y(150)), self.converter.conv_y(70))[0]:
                self.homeIconBgAlpha = 120
                survol = True
                if self.hover_circle(event, (self.converter.conv_x(150),self.screen.get_height() - self.converter.conv_y(150)), self.converter.conv_y(70))[1]:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    self.running = False
            else:
                self.homeIconBgAlpha = 60

            if survol:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def update(self): ##Tous les trucs à actualiser (collision,interractions automatiques) seront ici
        pass

    def display(self): ##Toutes les fonctions pygame pour afficher seront ici
        self.screen.fill((0,0,0))
        self.background.display()

        ## Affichage de l'icon de menu
        self.screen.blit(self.homeIconBgSurface, (self.converter.conv_x(50),self.screen.get_height() - self.converter.conv_y(250)))
        pygame.draw.circle(self.homeIconBgSurface, (0, 0, 0, self.homeIconBgAlpha), (self.converter.conv_x(100),self.converter.conv_y(100)), self.converter.conv_y(70))
        self.screen.blit(self.homeIconImage,(self.converter.conv_x(100),self.screen.get_height() - self.converter.conv_y(200)))

        ## Affichage du titre et son fond
        pygame.draw.rect(self.menuTitleBgSurface,(0,0,0,120),(0,0,self.screen.get_width(),self.converter.conv_y(250)))
        self.screen.blit(self.menuTitleBgSurface,(0,0))
        self.screen.blit(self.menuTitleText, self.menuTitleRect)

        pygame.display.flip() ##Actualiser

    def run(self):
        while self.running:
            self.handling_event()
            self.update()
            self.display()