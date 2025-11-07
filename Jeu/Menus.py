import pygame
import math
import threading
import time

from SaveMenu import SaveMenu
from SettingsMenu import SettingsMenu
from ShowDataMenu import ShowDataMenu
from BackgroundRandomSimulation import BackgroundRandomSimulation
from Converter import Converter
from CommonFonction import hover, fade_in, fade_out
from CommonVar import directory
import CommonVar
import Font
import SpriteBank

class Menus:
    def __init__(self,screen,window):
        self.screen = screen
        self.window = window
        self.running = True
 
        self.font = pygame.font.SysFont(None, 30) # Temporaire (FPS)

        self.commonVar = CommonVar.CommonVar()
        self.converter = Converter(self.screen)
        if self.commonVar.nJson() != 0:
            self.ingame = True
        else:
            self.ingame = False

        self.font = pygame.font.SysFont(None, 30) # Temporaire

        self.clock = pygame.time.Clock()

        self.backgroundRandomSimulation = BackgroundRandomSimulation(self.screen)
        self.saveMenu = SaveMenu(self.screen, self.backgroundRandomSimulation)
        self.settingsMenu = SettingsMenu(self.screen, self.backgroundRandomSimulation)
        self.showDataMenu = ShowDataMenu(self.screen, self.backgroundRandomSimulation)

        self.transitionBgSurface = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.fadeColor = [0,0,0,0]

        self.gameTitleFont = pygame.font.Font(Font.islandMomentFont, self.converter.conv_y(250))
        self.gameTitleText = self.gameTitleFont.render("Nox Villae",True,(255,255,255))
        self.gameTitleRect = self.gameTitleText.get_rect(center=(self.screen.get_width()/2,self.screen.get_height()/2 - self.converter.conv_y(190)))
        self.gameTitleBgSurface = pygame.Surface((self.converter.conv_x(1000),self.converter.conv_y(300)), pygame.SRCALPHA)

        self.buttonStartFont = pygame.font.Font(Font.jaini, self.converter.conv_y(100))
        self.buttonStartText = self.buttonStartFont.render("Démarrer",True,(188,209,191))
        self.buttonStartRect = self.buttonStartText.get_rect(center=(self.screen.get_width()/2,self.screen.get_height()/2 + self.converter.conv_y(95)))
        self.buttonStartBgSurface = pygame.Surface((self.converter.conv_x(500),self.converter.conv_y(200)), pygame.SRCALPHA)
        self.buttonStartBgRect = pygame.Rect(self.screen.get_width()/2 - self.converter.conv_x(200),self.screen.get_width()/2 - self.converter.conv_y(410),self.converter.conv_x(400),self.converter.conv_y(200))
        self.buttonStartBgColor = (68,84,70)

        self.buttonContinueFont = pygame.font.Font(Font.jaini, self.converter.conv_y(90))
        self.buttonContinueText = self.buttonContinueFont.render("Continuer",True,(188,209,191))
        self.buttonContinueRect = self.buttonContinueText.get_rect(center=(self.screen.get_width()/2,self.screen.get_height()/2 + self.converter.conv_y(30)))
        self.buttonContinueBgSurface = pygame.Surface((self.converter.conv_x(500),self.converter.conv_y(200)), pygame.SRCALPHA)
        self.buttonContinueBgRect = pygame.Rect(self.screen.get_width()/2 - self.converter.conv_x(200),self.screen.get_width()/2 - self.converter.conv_y(410),self.converter.conv_x(400),self.converter.conv_y(100))
        self.buttonContinueBgColor = (68,84,70)

        self.buttonSaveFont = pygame.font.Font(Font.jaini, self.converter.conv_y(90))
        self.buttonSaveText = self.buttonSaveFont.render("Parties",True,(206,194,194))
        self.buttonSaveRect = self.buttonSaveText.get_rect(center=(self.screen.get_width()/2 - self.converter.conv_x(50),self.screen.get_height()/2 + self.converter.conv_y(140)))
        self.buttonSaveBgSurface = pygame.Surface((500,200), pygame.SRCALPHA)
        self.buttonSaveBgRect = pygame.Rect(self.screen.get_width()/2 - self.converter.conv_x(200),self.screen.get_width()/2 - self.converter.conv_y(300),self.converter.conv_x(400),self.converter.conv_y(100))
        self.buttonSaveBgColor = (91,50,51)

        self.floppyDiscImage = SpriteBank.logo['Disquette']
        self.floppyDiscImage = pygame.transform.scale(self.floppyDiscImage, (self.converter.conv_x(70),self.converter.conv_y(70)))

        self.populationFont = pygame.font.Font(Font.inter, self.converter.conv_y(35))
        self.populationText = self.populationFont.render("Population de départ : __",True,(255,255,255))
        self.populationRect = self.populationText.get_rect(center=(self.screen.get_width()/2,self.screen.get_height()/2 + self.converter.conv_y(250)))
        self.populationBgSurface = pygame.Surface((self.converter.conv_x(500),self.converter.conv_y(50)), pygame.SRCALPHA)

        self.settingsIconImage = SpriteBank.logo['Engrenage']
        self.settingsIconImage = pygame.transform.scale(self.settingsIconImage, (self.converter.conv_x(100),self.converter.conv_y(100)))
        self.settingsIconRect = self.settingsIconImage.get_rect()
        self.settingsIconBgSurface = pygame.Surface((self.converter.conv_x(200),self.converter.conv_y(200)), pygame.SRCALPHA)
        self.settingsIconBgAlpha = 120

        self.idIconImage = SpriteBank.logo['Id']
        self.idIconImage = pygame.transform.scale(self.idIconImage, (self.converter.conv_x(188),self.converter.conv_y(128)))
        self.idIconRect = pygame.Rect((self.screen.get_width() - self.converter.conv_x(325),self.converter.conv_y(300),self.converter.conv_x(188),self.converter.conv_y(128)))
        self.idIconAlpha = 200

        self.exitIconImage = SpriteBank.logo['Exit']
        self.exitIconImage = pygame.transform.scale(self.exitIconImage, (self.converter.conv_x(117),self.converter.conv_y(122)))
        self.exitIconRect = pygame.Rect((self.screen.get_width() - self.converter.conv_x(210),self.screen.get_height() - self.converter.conv_y(210),self.converter.conv_x(117),self.converter.conv_y(122)))
        self.exitIconAlpha = 200
        
        self.start_threading()
        
    def hover_circle(self, event, circle_center, circle_radius):
        mouse_pos = pygame.mouse.get_pos()
        if math.dist(mouse_pos, circle_center) < circle_radius: # Quand la souris rentre dans le cercle
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return True,True # Touche : True , Clique : True
            return True,False # Touche : True , Clique : False
        else:
            return False,False # Touche : False

    def handling_event(self, event): ##Tous les évenements (joueur -> jeu) seront ici
        if event.type == pygame.QUIT: ##Si le joueur appuie sur la croix de la fenetre
            self.commonVar.update_saving_json()   
            self.commonVar.update_common_json()
            pygame.quit() ##Le jeu s'arrete

    def interraction(self, event):
        # Couleur des boutons au survol
        survol = False
        if self.ingame:
            if hover(event,self.buttonContinueBgRect)[0]:
                self.buttonContinueBgColor = (108,124,110)
                self.buttonContinueText = self.buttonContinueFont.render("Continuer",True,(228,249,231))
                survol = True
                
                if hover(event,self.buttonContinueBgRect)[1]:
                    self.bootGame()
            else:
                self.buttonContinueBgColor = (68,84,70)
                self.buttonContinueText = self.buttonContinueFont.render("Continuer",True,(188,209,191))

            if hover(event,self.buttonSaveBgRect)[0]:
                self.buttonSaveBgColor = (131,90,91)
                self.buttonSaveText = self.buttonSaveFont.render("Parties",True,(246,234,234))
                survol = True
                
                if hover(event,self.buttonSaveBgRect)[1]:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    self.backgroundRandomSimulation.alpha = 70
                    self.openSaveMenu()
            else:
                self.buttonSaveBgColor = (91,50,51)
                self.buttonSaveText = self.buttonSaveFont.render("Parties",True,(206,194,194))
        else:
            if hover(event,self.buttonStartBgRect)[0]:
                self.buttonStartBgColor = (108,124,110)
                self.buttonStartText = self.buttonStartFont.render("Démarrer",True,(228,249,231))
                survol = True
                if hover(event,self.buttonStartBgRect)[1]:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    self.backgroundRandomSimulation.alpha = 70
                    self.openSaveMenu()
            else:
                self.buttonStartBgColor = (68,84,70)
                self.buttonStartText = self.buttonStartFont.render("Démarrer",True,(188,209,191))
        
        # Augmenter l'alpha du fond de l'engrenage quand on le survol
        if self.hover_circle(event, (self.converter.conv_x(150),self.screen.get_height() - self.converter.conv_y(150)), 70)[0]:
            self.settingsIconBgAlpha = 120
            survol = True
            if self.hover_circle(event, (self.converter.conv_x(150),self.screen.get_height() - self.converter.conv_y(150)), 70)[1]:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                self.backgroundRandomSimulation.alpha = 70
                self.openSettingsMenu()
        else:
            self.settingsIconBgAlpha = 60

        # Augmenter l'alpha de l'id quand on le survol
        if hover(event, self.idIconRect)[0]:
            self.idIconAlpha = 255
            survol = True
            
            if hover(event, self.idIconRect)[1]:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                self.backgroundRandomSimulation.alpha = 70
                self.openShowDataMenu()
        else:
            self.idIconAlpha = 200
        self.idIconImage.set_alpha(self.idIconAlpha)

        # Augmenter l'alpha du bouton exit quand on le survol
        if hover(event, self.exitIconRect)[0]:
            self.exitIconAlpha = 255

            if hover(event, self.exitIconRect)[1]:
                self.commonVar.update_saving_json()   
                self.commonVar.update_common_json()
                pygame.quit()
        
        else:
            self.exitIconAlpha = 200
        self.exitIconImage.set_alpha(self.exitIconAlpha)

        if survol :
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            

    def update(self): ##Tous les trucs à actualiser (colition,interractions automatiques) seront ici

        self.backgroundRandomSimulation.alpha = 255

        if self.ingame :
            self.populationText = self.populationFont.render(f"Population actuelle : {CommonVar.savingDico['creatureNumber']}",True,(255,255,255))
        else:
            self.populationText = self.populationFont.render(f"Population de départ : {CommonVar.savingDico['creatureStartingNumber']}",True,(255,255,255))

    def display(self): ##Toutes les fonctions pygame pour afficher seront ici
        self.backgroundRandomSimulation.display()

        if self.ingame: ## Boutons qui change si on est en partie ou pas
            self.screen.blit(self.buttonContinueBgSurface,(self.screen.get_width()/2 - self.converter.conv_x(200),self.screen.get_width()/2 - self.converter.conv_y(435)))
            pygame.draw.rect(self.buttonContinueBgSurface, self.buttonContinueBgColor,(0,0,self.converter.conv_x(400),self.converter.conv_y(100)),border_radius=self.converter.conv_y(20))
            self.screen.blit(self.buttonContinueText, self.buttonContinueRect)

            self.screen.blit(self.buttonSaveBgSurface,(self.screen.get_width()/2 - self.converter.conv_x(200),self.screen.get_width()/2 - self.converter.conv_y(325)))
            pygame.draw.rect(self.buttonSaveBgSurface, self.buttonSaveBgColor,(0,0,self.converter.conv_x(400),self.converter.conv_y(100)),border_radius=self.converter.conv_y(20))
            self.screen.blit(self.buttonSaveText, self.buttonSaveRect)

            self.screen.blit(self.floppyDiscImage,(self.screen.get_width()/2 + self.converter.conv_x(90),self.screen.get_width()/2 - self.converter.conv_y(310)))
        else:
            self.screen.blit(self.buttonStartBgSurface,(self.screen.get_width()/2 - self.converter.conv_x(200),self.screen.get_width()/2 - self.converter.conv_y(425)))
            pygame.draw.rect(self.buttonStartBgSurface, self.buttonStartBgColor,(0,0,self.converter.conv_x(400),self.converter.conv_y(200)),border_radius=self.converter.conv_y(30))
            self.screen.blit(self.buttonStartText, self.buttonStartRect)
            
        ## Affichage de "Population de départ : __" ouf "Population actuelle : __"
        self.screen.blit(self.populationBgSurface,(self.screen.get_width()/2 - self.converter.conv_x(200),self.screen.get_width()/2 - self.converter.conv_y(195)))
        pygame.draw.rect(self.populationBgSurface, (0,0,0,120),(0,0,self.converter.conv_x(400),self.converter.conv_y(50)),border_radius=self.converter.conv_y(20))
        self.screen.blit(self.populationText, self.populationRect)

        ## Affichage de l'engrenage et son fonds
        self.screen.blit(self.settingsIconBgSurface, (self.converter.conv_x(50),self.screen.get_height() - self.converter.conv_y(250)))
        pygame.draw.circle(self.settingsIconBgSurface, (0, 0, 0, self.settingsIconBgAlpha), (self.converter.conv_y(100),self.converter.conv_x(100)), self.converter.conv_y(70))
        self.screen.blit(self.settingsIconImage,(self.converter.conv_x(100),self.screen.get_height() - self.converter.conv_y(200)))

        ##Affichage de la carte d'identité
        self.screen.blit(self.idIconImage,self.idIconRect)

        ##Affichage du bouton exit
        self.screen.blit(self.exitIconImage,self.exitIconRect)

        ## Affichage du titre et son fond
        self.screen.blit(self.gameTitleBgSurface,(self.screen.get_width()/2 - self.converter.conv_x(500),self.screen.get_height()/2 - self.converter.conv_y(330)))
        pygame.draw.rect(self.gameTitleBgSurface,(0,0,0,120),(0,0,self.converter.conv_x(1000),self.converter.conv_y(300)),border_radius=30)
        self.screen.blit(self.gameTitleText, self.gameTitleRect)

        ## Affichage du fondu enchainé (calque noir)
        self.screen.blit(self.transitionBgSurface,(0,0))
        self.transitionBgSurface.fill(self.fadeColor)

        fps_text = self.font.render(f"FPS: {int(self.clock.get_fps())}", True, (255, 255, 255))
        self.screen.blit(fps_text, (10, 10))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.settingsMenu.run()
            self.saveMenu.run()
            self.showDataMenu.run()
            self.update()
            for event in pygame.event.get():
                self.handling_event(event)
                self.interraction(event)
            self.display()

    def randomSimulationUpdate(self):
        while self.running:
            self.backgroundRandomSimulation.handling_event()
            self.backgroundRandomSimulation.update()
            self.clock.tick(30)

    def start_threading(self):
        threading.Thread(target=self.randomSimulationUpdate, daemon=True).start()

    def bootGame(self):
        print('ouais')
        fade_out(self, 30)
        fade_in(self.window.game, 30)
        self.window.game.run(self.window)

    def openSettingsMenu(self):
        self.settingsMenu.running = True

    def openSaveMenu(self): # A CHANGER ABSOLUMENT QUAND ON AURA FINI
        self.saveMenu.running = True
        self.saveMenu.update()

    def openShowDataMenu(self):
        self.showDataMenu.running = True