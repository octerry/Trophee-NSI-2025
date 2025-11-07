import pygame
import math

from Converter import Converter
from CommonFonction import fade_out
import CommonVar
import Font
import SpriteBank

class LittleGirlSpying:
    def __init__(self,screen):
        self.screen = screen
        self.running = True

        self.converter = Converter(self.screen)
        self.clock = pygame.time.Clock()
        self.tick = 0

        self.target = None

        self.eyeMask = pygame.transform.scale(SpriteBank.calqueOeil, (self.converter.conv_x(3708),self.converter.conv_y(2880))).convert_alpha()
        self.eyeMaskRect = self.eyeMask.get_rect(center=(self.screen.get_width()/2,self.screen.get_height()/2))

        self.bgSurface = pygame.Surface((self.screen.get_width(),self.screen.get_height()))
        self.bgPos = (0,0)
        self.frontSurface = pygame.Surface((self.screen.get_width(),self.screen.get_height()), pygame.SRCALPHA)
        self.frontPos = (0,0)

        self.nightTent = pygame.transform.scale(SpriteBank.tente['Nuit']['Droite'], (self.converter.conv_x(827),self.converter.conv_y(592)))
        self.nightTentCenterRect = self.nightTent.get_rect(center = (self.screen.get_width()*2/3,self.screen.get_height()/2))

        self.titleFont = pygame.font.Font(Font.IMfell, self.converter.conv_y(80))
        self.titleText = self.titleFont.render("Vous espionnez actuellement -nom-",True,(151,151,151))
        self.titleTextRect = self.titleText.get_rect(center = ((self.screen.get_width()/2, self.converter.conv_y(100))))

        self.subtitleFont = pygame.font.Font(Font.jaini, self.converter.conv_y(50))
        self.subtitleText = self.subtitleFont.render("C'est au tour des Loups-garous",True,(124,29,29))
        self.subtitleTextRect = self.subtitleText.get_rect(center = ((self.screen.get_width()/2, self.converter.conv_y(155))))

        self.wolfImage = SpriteBank.loup['Run']['Gauche'][0]
        self.wolfImage = pygame.transform.scale(self.wolfImage, (self.converter.conv_x(640), self.converter.conv_y(480)))
        self.wolfRect = self.wolfImage.get_rect(center = (self.screen.get_width()/2, self.screen.get_height()/2))

        self.fade = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        self.fadeColor = [0,0,0,255]

    def handling_event(self, event):
        if event.type == pygame.QUIT: ##Si le joueur appuie sur la croix de la fenetre
            self.running = False ##Le jeu s'arrete

    def timing(self):
        if self.tick >= 500:
            fade_out(self, 60)

    def update(self):
        assert not self.target, self.target

        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEALL)

        self.tick += 1

        if self.tick == 1:
            self.titleText = self.titleFont.render(f"Vous espionnez actuellement {CommonVar.savingDico['creatureId'][self.target]}",True,(151,151,151))
            self.titleTextRect = self.titleText.get_rect(center = ((self.screen.get_width()/2, self.converter.conv_y(100))))

        mouseX,mouseY = pygame.mouse.get_pos()
        posX = (mouseX + self.screen.get_width()/2) /2
        posY = (mouseY + self.screen.get_height()/2) /2
        self.eyeMaskRect = self.eyeMask.get_rect(center=(posX,posY))
        
        posX = (mouseX + self.screen.get_width()*4) /7 - self.screen.get_width()*2/3
        posY = (mouseY + self.screen.get_height()*8) /11 - self.screen.get_height()*3/4
        self.bgPos = (posX, posY)

        posX = (mouseX + self.screen.get_width()*8) /17 - self.screen.get_width()/2
        posY = (mouseY + self.screen.get_height()*16) /33 - self.screen.get_height()/2
        self.frontPos = (posX, posY)

    def display(self):

        self.screen.blit(self.bgSurface, self.bgPos)
        self.bgSurface.fill((54,50,47))
        self.bgSurface.blit(self.nightTent, self.nightTentCenterRect)
        self.bgSurface.blit(self.wolfImage, self.wolfRect)
        
        self.screen.blit(self.eyeMask, self.eyeMaskRect)

        self.screen.blit(self.frontSurface, self.frontPos)
        self.frontSurface.blit(self.titleText, self.titleTextRect)
        self.frontSurface.blit(self.subtitleText, self.subtitleTextRect)

        self.screen.blit(self.fade, (0,0))
        self.fade.fill(self.fadeColor)

        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.handling_event(event)
            self.timing()
            self.update()
            self.display()
            self.clock.tick(60)