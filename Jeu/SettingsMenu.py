import pygame
import math

from KeybindingMenu import KeybindingMenu
from GeneralSettingsMenu import GeneralSettingsMenu
from Keybinds import keybinds
from CommonVar import directory
from CommonVar import CommonVar
from Converter import Converter
from CommonFonction import hover
import Font
import SpriteBank

class SettingsMenu:
    def __init__(self,screen,background):
        self.screen = screen
        self.running = False
        self.generalSettings = True ## True : parametres généraux , False : configuration des touches
        
        self.converter = Converter(self.screen)
        self.commonVar = CommonVar()

        self.background = background
        self.clock = pygame.time.Clock()
 
        self.font = pygame.font.SysFont(None, 30) # Temporaire (FPS)

        self.keybindingMenu = KeybindingMenu(self.screen)
        self.generalSettingsMenu = GeneralSettingsMenu(self.screen)

        self.homeIconImage = SpriteBank.logo['Home']
        self.homeIconRect = self.homeIconImage.get_rect()
        self.homeIconImage = pygame.transform.scale(self.homeIconImage, (self.converter.conv_x(100),self.converter.conv_y(100)))
        self.homeIconBgSurface = pygame.Surface((self.converter.conv_x(200),self.converter.conv_y(200)), pygame.SRCALPHA)
        self.homeIconBgAlpha = 120

        self.menuTitleFont = pygame.font.Font(Font.jaini, self.converter.conv_y(150))
        self.menuTitleText = self.menuTitleFont.render("Paramètres",True,(240,240,240))
        self.menuTitleRect = self.menuTitleText.get_rect(center=(self.screen.get_width()/2,self.converter.conv_x(150)))
        self.menuTitleBgSurface = pygame.Surface((self.screen.get_width(),self.converter.conv_y(300)), pygame.SRCALPHA)

        self.generalSettingsFont = pygame.font.Font(Font.jacquard, 70)
        self.generalSettingsText = self.generalSettingsFont.render("Paramètres généraux",True,(255,255,255))
        self.generalSettingsRect = self.generalSettingsText.get_rect(center=(self.screen.get_width()*0.75,self.converter.conv_y(300)))
        self.generalSettingsBgSurface = pygame.Surface((self.screen.get_width(),self.converter.conv_y(300)), pygame.SRCALPHA)
        self.generalSettingsBgRect = pygame.Rect((self.screen.get_width()/2,self.converter.conv_y(250),self.screen.get_width()/2,self.converter.conv_y(100)))

        self.keybindingSettingsFont = pygame.font.Font(Font.jacquard, self.converter.conv_y(70))
        self.keybindingSettingsText = self.keybindingSettingsFont.render("Configuration des touches",True,(0,0,0))
        self.keybindingSettingsRect = self.keybindingSettingsText.get_rect(center=(self.screen.get_width()*0.25,self.converter.conv_y(300)))
        self.keybindingSettingsBgSurface = pygame.Surface((self.screen.get_width()/2,self.converter.conv_y(200)), pygame.SRCALPHA)
        self.keybindingSettingsBgRect = pygame.Rect((0,self.converter.conv_y(250),self.screen.get_width()/2,self.converter.conv_y(100)))
        
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
                self.commonVar.update_saving_json()   
                self.commonVar.update_common_json()
                pygame.quit() ##Le jeu s'arrete
            
            keys = pygame.key.get_pressed()
            if keys[keybinds['openMenu']]:
                self.commonVar.update_saving_json()
                self.running = False
                self.background.alpha = 255
            
            survol = False

            if self.hover_circle(event, (self.converter.conv_x(150),self.screen.get_height() - self.converter.conv_y(150)), self.converter.conv_y(70))[0]:
                self.homeIconBgAlpha = 120
                survol = True
                if self.hover_circle(event, (self.converter.conv_x(150),self.screen.get_height() - self.converter.conv_y(150)), self.converter.conv_y(70))[1]:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    self.commonVar.update_saving_json()
                    self.running = False
                    self.background.alpha = 255
            else:
                self.homeIconBgAlpha = 60

            if self.generalSettings :
                self.generalSettingsText = self.generalSettingsFont.render("Paramètres généraux",True,(255,255,255))
                if hover(event,self.keybindingSettingsBgRect)[0]:
                    self.keybindingSettingsText = self.keybindingSettingsFont.render("Configuration des touches",True,(100,100,255))
                    survol = True

                    if hover(event,self.keybindingSettingsBgRect)[1]:
                        self.generalSettings = False

                else:
                    self.keybindingSettingsText = self.keybindingSettingsFont.render("Configuration des touches",True,(100,100,100))

            else:
                self.keybindingSettingsText = self.keybindingSettingsFont.render("Configuration des touches",True,(255,255,255))
                if hover(event, self.generalSettingsBgRect)[0]:
                    self.generalSettingsText = self.generalSettingsFont.render("Paramètres généraux",True,(100,100,255))
                    survol = True

                    if hover(event,self.generalSettingsBgRect)[1]:
                        self.generalSettings = True

                else:
                    self.generalSettingsText = self.generalSettingsFont.render("Paramètres généraux",True,(100,100,100))

            if self.generalSettings :
                survol = self.generalSettingsMenu.handling_event(survol,event)
            else:
                survol = self.keybindingMenu.handling_event(survol,event,self)

            if survol:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def update(self): ##Tous les trucs à actualiser (collision,interractions automatiques) seront ici
        pass

    def display(self): ##Toutes les fonctions pygame pour afficher seront ici
        self.screen.fill((0,0,0))
        self.background.display()

        if self.generalSettings:
            self.generalSettingsMenu.display()
        else:
            self.keybindingMenu.display()

        ## Affichage de l'icon de menu
        self.screen.blit(self.homeIconBgSurface, (self.converter.conv_x(50),self.screen.get_height() - self.converter.conv_y(250)))
        pygame.draw.circle(self.homeIconBgSurface, (0, 0, 0, self.homeIconBgAlpha), (self.converter.conv_x(100),self.converter.conv_y(100)), self.converter.conv_y(70))
        self.screen.blit(self.homeIconImage,(self.converter.conv_x(100),self.screen.get_height() - self.converter.conv_y(200)))

        ## Affichage des titres secondaires
        if self.generalSettings:
            ### "Parametres généraux"
            pygame.draw.rect(self.generalSettingsBgSurface,(0,0,0,120),(0,0,self.screen.get_width()/2,self.converter.conv_y(100)),border_bottom_left_radius=self.converter.conv_y(40))
            self.screen.blit(self.generalSettingsBgSurface,(self.screen.get_width()/2,self.converter.conv_y(250)))
            self.screen.blit(self.generalSettingsText, self.generalSettingsRect)

            self.screen.blit(self.keybindingSettingsText, self.keybindingSettingsRect)
        else:
            ### "Configuration des touches"
            pygame.draw.rect(self.keybindingSettingsBgSurface,(0,0,0,120),(0,0,self.screen.get_width()/2,self.converter.conv_y(100)),border_bottom_right_radius=self.converter.conv_y(40))
            self.screen.blit(self.keybindingSettingsBgSurface,(0,self.converter.conv_y(250)))
            self.screen.blit(self.keybindingSettingsText, self.keybindingSettingsRect)

            self.screen.blit(self.generalSettingsText, self.generalSettingsRect)

        ## Affichage du titre et son fond
        pygame.draw.rect(self.menuTitleBgSurface,(0,0,0,120),(0,0,self.screen.get_width(),self.converter.conv_y(250)))
        self.screen.blit(self.menuTitleBgSurface,(0,0))
        self.screen.blit(self.menuTitleText, self.menuTitleRect)

        fps_text = self.font.render(f"FPS: {int(self.clock.get_fps())}", True, (255, 255, 255))
        self.screen.blit(fps_text, (10, 10))

        pygame.display.flip() ##Actualiser

    def run(self):
        while self.running:
            if self.generalSettings:
                self.generalSettingsMenu.update()
            else:
                self.keybindingMenu.update()
            self.handling_event()
            self.update()
            self.display()