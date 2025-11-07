import pygame
import math

from Converter import Converter
from CommonFonction import hover, fade_out
from CommonVar import directory
import CommonVar
import Font
import SpriteBank

class WitchChoice:
    def __init__ (self,screen):
        self.screen = screen
        self.running = False

        self.commonVar = CommonVar.CommonVar()
        self.converter = Converter(self.screen)

        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(Font.IMfell,self.converter.conv_y(55))

        self.chosen = None

        self.witchImage = SpriteBank.character['Sorciere']
        self.witchImage = pygame.transform.scale(self.witchImage,(self.converter.conv_x(900),self.converter.conv_y(900)))
        self.witchRect = self.witchImage.get_rect(center=(self.screen.get_width()/2,self.screen.get_height()/2 + self.converter.conv_y(100)))

        self.title = self.font.render("Sorcière, Quelle potion souhaitez vous utiliser cette nuit ?",True,(255,255,255))
        self.titleRect = self.title.get_rect(center=(self.screen.get_width()/2 , self.converter.conv_y(150)))


        self.deathPotionOriginalImage = SpriteBank.potion['Mort']
        self.deathPotionImage = pygame.transform.scale(self.deathPotionOriginalImage,(self.converter.conv_x(389),self.converter.conv_y(391)))
        self.deathPotionRect = self.deathPotionImage.get_rect(center=(self.screen.get_width()/4,self.screen.get_height()/2))
        self.deathPotionRotation = 0
        self.deathPotionSelected = False

        self.deathPotionText = self.font.render("Potion de mort",True,(255,255,255))
        self.deathPotionTextRect = self.deathPotionText.get_rect(center=(self.screen.get_width()/4,self.screen.get_height()/2 + self.converter.conv_y(230)))


        self.revivePotionOriginalImage = SpriteBank.potion['Vie']
        self.revivePotionImage = pygame.transform.scale(self.revivePotionOriginalImage,(self.converter.conv_x(389),self.converter.conv_y(391)))
        self.revivePotionRect = self.revivePotionImage.get_rect(center=(3*self.screen.get_width()/4,self.screen.get_height()/2))
        self.revivePotionRotation = 1
        self.revivePotionSelected = False

        self.revivePotionText = self.font.render("Potion de vie",True,(255,255,255))
        self.revivePotionTextRect = self.revivePotionText.get_rect(center=(3*self.screen.get_width()/4,self.screen.get_height()/2 + self.converter.conv_y(230)))


        self.nothingImage = SpriteBank.logo['Aucun']
        self.nothingImage = pygame.transform.scale(self.nothingImage,(self.converter.conv_x(200),self.converter.conv_y(200)))
        self.nothingImageRect = self.nothingImage.get_rect(center=(self.screen.get_width()/2,self.screen.get_height() - self.converter.conv_y(200)))

        nothingHitboxWidth = self.converter.conv_x(200)
        nothingHitboxHeight = self.converter.conv_y(200)
        self.nothingHitbox = pygame.Rect(self.screen.get_width()/2 - nothingHitboxWidth/2 , self.screen.get_height() - self.converter.conv_y(200) - nothingHitboxHeight/2 , nothingHitboxWidth , nothingHitboxHeight)
        self.nothingSeleted = False

        self.nothingText = self.font.render("Ne rien faire",True,(255,255,255))
        self.nothingTextRect = self.nothingText.get_rect(center=(self.screen.get_width()/2,self.screen.get_height() - self.converter.conv_y(200)))

        self.fade = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        self.fadeColor = [0,0,0,255]

    def handling_event (self,event):
            if event.type == pygame.QUIT: ##Si le joueur appuie sur la croix de la fenetre
                self.commonVar.update_saving_json()
                self.commonVar.update_common_json()
                pygame.quit() ##Le jeu s'arrete


    def interraction (self,event):
            if CommonVar.savingDico['witchRemainingPotion'][0] == CommonVar.savingDico['witchRemainingPotion'][1] == False:
                self.running = False

            survol = False

            if CommonVar.savingDico['witchRemainingPotion'][0]:
                if hover(event,self.deathPotionRect)[0]:
                    self.deathPotionSelected = True
                    survol = True
                    if hover(event,self.deathPotionRect)[1]:
                        self.chosen = "death"
                        fade_out(self, 60)
                        CommonVar.savingDico['witchRemainingPotion'][0] = False
                else:
                    self.deathPotionSelected = False

            if CommonVar.savingDico['witchRemainingPotion'][1]:
                if hover(event,self.revivePotionRect)[0]:
                    self.revivePotionSelected = True
                    survol = True
                    if hover(event,self.revivePotionRect)[1]:
                        self.chosen = "revive"
                        fade_out(self, 60)
                        CommonVar.savingDico['witchRemainingPotion'][1] = False
                else:
                    self.revivePotionSelected = False


            if hover(event,self.nothingHitbox)[0]:
                self.nothingSeleted = True
                survol = True
                if hover(event,self.nothingHitbox)[1]:
                    self.chosen = None
                    fade_out(self, 60)
            else:
                self.nothingSeleted = False


            if survol:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def update (self):
        # Animation potion
        ## Potion de mort
        if not self.deathPotionSelected:
            if self.deathPotionRotation < 2:
                self.deathPotionRotation += 0.01
            else:
                self.deathPotionRotation = 0.01
            deathPotionRotation = 25 * math.sin(math.pi * self.deathPotionRotation)

            self.deathPotionImage = pygame.transform.scale(self.deathPotionOriginalImage,(self.converter.conv_x(389),self.converter.conv_y(391)))
            self.deathPotionImage = pygame.transform.rotate(self.deathPotionImage,deathPotionRotation)
        else:
            self.deathPotionImage = pygame.transform.scale(self.deathPotionOriginalImage,(self.converter.conv_x(419),self.converter.conv_y(421)))
        self.deathPotionRect = self.deathPotionImage.get_rect(center=(self.screen.get_width()/4,self.screen.get_height()/2))

        ## Potion de vie
        if not self.revivePotionSelected:
            if self.revivePotionRotation < 2:
                self.revivePotionRotation += 0.01
            else:
                self.revivePotionRotation = 0.01
            revivePotionRotation = 25 * math.sin(math.pi * self.revivePotionRotation)

            self.revivePotionImage = pygame.transform.scale(self.revivePotionOriginalImage,(self.converter.conv_x(389),self.converter.conv_y(391)))
            self.revivePotionImage = pygame.transform.rotate(self.revivePotionImage,revivePotionRotation)
        else:
            self.revivePotionImage = pygame.transform.scale(self.revivePotionOriginalImage,(self.converter.conv_x(419),self.converter.conv_y(421)))
        self.revivePotionRect = self.revivePotionImage.get_rect(center=(3* self.screen.get_width()/4,self.screen.get_height()/2))

    def display (self):
        self.screen.fill((0,0,0))

        self.screen.blit(self.witchImage,self.witchRect)

        if CommonVar.savingDico['witchRemainingPotion'][0]:
            self.screen.blit(self.deathPotionImage,self.deathPotionRect)
        if CommonVar.savingDico['witchRemainingPotion'][1]:
            self.screen.blit(self.revivePotionImage,self.revivePotionRect)

        if self.nothingSeleted:
            self.screen.blit(self.nothingImage,self.nothingImageRect)

        self.screen.blit(self.title,self.titleRect)
        self.screen.blit(self.nothingText,self.nothingTextRect)

        if self.deathPotionSelected:
            self.screen.blit(self.deathPotionText,self.deathPotionTextRect)
        if self.revivePotionSelected:
            self.screen.blit(self.revivePotionText,self.revivePotionTextRect)

        self.screen.blit(self.fade, (0,0))
        self.fade.fill(self.fadeColor)

        pygame.display.flip()

    def run (self):
        while self.running :
            for event in pygame.event.get():
                self.handling_event(event)
                self.interraction(event)
            self.update()
            self.display()
            self.clock.tick(60)