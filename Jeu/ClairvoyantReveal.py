import pygame

from Converter import Converter
from CommonFonction import fade_out
import CommonVar
import Font
import SpriteBank

class ClairvoyantReveal:
    def __init__ (self,screen):
        self.screen = screen
        self.running = True

        self.converter = Converter(screen)
        self.commonVar = CommonVar.CommonVar()

        self.clock = pygame.time.Clock()

        self.targetId = 1

        self.clairvoyantImage = SpriteBank.character['Voyante']
        self.clairvoyantImage = pygame.transform.scale(self.clairvoyantImage,(self.converter.conv_x(1282),self.converter.conv_y(1282)))
        self.clairvoyantRect = self.clairvoyantImage.get_rect(center=(self.screen.get_width()/2,self.screen.get_height()/3))

        self.titleFont = pygame.font.Font(Font.IMfell,self.converter.conv_y(80))
        self.titleText = self.titleFont.render("Vous lisez dans la boule de crystal que...",True,(255,255,255))
        self.titleRect = self.titleText.get_rect(center=(self.screen.get_width()/2,self.converter.conv_y(100)))

        self.infoFont = pygame.font.Font(Font.RubikVinyl,self.converter.conv_y(90))
        self.infoText = self.infoFont.render(f"{CommonVar.savingDico['creatureId'][self.targetId]} est {CommonVar.savingDico['creatureRoles'][self.targetId]}",True,(255,255,255))
        self.infoRect = self.infoText.get_rect(center=(self.screen.get_width()/2,self.screen.get_height() - self.converter.conv_y(150)))

        self.fade = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        self.fadeColor = [0,0,0,255]

    def handling_event (self,event):
        if event.type == pygame.QUIT: ##Si le joueur appuie sur la croix de la fenetre
            self.commonVar.update_saving_json()
            self.commonVar.update_common_json()
            pygame.quit() ##Le jeu s'arrete

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            fade_out(self, 60)

    def update(self):
        pass

    def update_text(self):
        self.infoFont = pygame.font.Font(Font.RubikVinyl,self.converter.conv_y(90))
        self.infoText = self.infoFont.render(f"{CommonVar.savingDico['creatureId'][self.targetId]} est {CommonVar.savingDico['creatureRoles'][self.targetId]}",True,(255,255,255))
        self.infoRect = self.infoText.get_rect(center=(self.screen.get_width()/2,self.screen.get_height() - self.converter.conv_y(150)))

    def display(self):
        self.screen.fill((0,0,0))

        self.screen.blit(self.clairvoyantImage,self.clairvoyantRect)
        self.screen.blit(self.titleText,self.titleRect)
        self.screen.blit(self.infoText,self.infoRect)

        self.screen.blit(self.fade, (0,0))
        self.fade.fill(self.fadeColor)

        pygame.display.flip()
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.handling_event(event)
            self.update()
            self.display()
            self.clock.tick(60)