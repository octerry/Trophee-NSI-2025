import pygame

from CommonVar import directory
from Converter import Converter
from CommonFonction import hover, create_radial_vignette, fade_out
from SpriteAnimation import feu
import Font
import SpriteBank

class PyromaniacChoice:
    def __init__(self,screen):
        self.screen = screen
        self.running = False

        self.clock = pygame.time.Clock()
        self.tick = 0
        self.tickFont = pygame.font.Font(Font.inter,20)
        self.tickText = self.tickFont.render('0',True,(255,255,255))

        self.converter = Converter(self.screen)

        self.bgImage = SpriteBank.fondMap['Nuit']
        self.bgImage = pygame.transform.scale(self.bgImage, (self.converter.conv_x(1920*4),self.converter.conv_y(1080*4)))
        self.bgRect = self.bgImage.get_rect(center=(self.screen.get_width()/2,self.screen.get_height()/2))

        self.logLeftImage = SpriteBank.buche['Nuit']['Gauche']
        self.logRightImage = SpriteBank.buche['Nuit']['Droite']
        self.logUpImage = SpriteBank.buche['Nuit']['Haut']

        self.logLeftImage = pygame.transform.scale(self.logLeftImage, (self.converter.conv_x(105*4), self.converter.conv_y(220*4)))
        self.logRightImage = pygame.transform.scale(self.logRightImage, (self.converter.conv_x(105*4), self.converter.conv_y(220*4)))
        self.logUpImage = pygame.transform.scale(self.logUpImage, (self.converter.conv_x(245*4), self.converter.conv_y(95*4)))

        self.logLeftRect = self.logLeftImage.get_rect(center = (self.converter.conv_x(20), self.converter.conv_y(600)))
        self.logRightRect = self.logRightImage.get_rect(center = (self.screen.get_width() - self.converter.conv_x(20), self.converter.conv_y(600)))
        self.logUpRect = self.logUpImage.get_rect(center = (self.screen.get_width()/2, self.converter.conv_y(10)))


        self.fireCampSpriteAnimation = feu[1]
        self.fireCampSpriteAnimation = [pygame.transform.scale(self.fireCampSpriteAnimation[i],(self.converter.conv_x(590),self.converter.conv_y(830))) for i in range(4)]
        self.fireCampSpriteAnimationRect = [self.fireCampSpriteAnimation[i].get_rect(center=(self.screen.get_width()/2, self.converter.conv_y(440))) for i in range(4)]

        self.torchImage = SpriteBank.elPyromaniac['Torche']
        self.torchImage = pygame.transform.scale(self.torchImage, (self.converter.conv_x(355),self.converter.conv_y(355)))
        self.torchRect = self.torchImage.get_rect(center=(self.screen.get_width()/4, self.screen.get_height()*2/3))

        self.kegImage = SpriteBank.elPyromaniac['Baril']
        self.kegImage = pygame.transform.scale(self.kegImage, (self.converter.conv_x(594), self.converter.conv_y(588)))
        self.kegRect = self.kegImage.get_rect(center=(self.screen.get_width()*3/4, self.screen.get_height()*2/3))

        self.titleFont = pygame.font.Font(Font.IMfell, self.converter.conv_y(100))
        self.title = self.titleFont.render("Que voulez vous faire, Pyromancien ?",True,(255,255,255))
        self.titleRect = self.title.get_rect(center = ((self.screen.get_width()/2, self.converter.conv_y(60))))


        self.choiceFont = pygame.font.Font(Font.RubikVinyl, self.converter.conv_y(100))

        self.choice1 = False
        self.choice2 = False

        self.choiceText1A = self.choiceFont.render("Tout faire",True,(255,255,255))
        self.choiceText1B = self.choiceFont.render("exploser",True,(255,255,255))
        self.choiceText2A = self.choiceFont.render("Déposer un",True,(255,255,255))
        self.choiceText2B = self.choiceFont.render("autre baril",True,(255,255,255))

        self.choiceRect1A = self.choiceText1A.get_rect(center = ((self.screen.get_width()/4, self.converter.conv_y(850))))
        self.choiceRect1B = self.choiceText1B.get_rect(center = ((self.screen.get_width()/4, self.converter.conv_y(935))))
        self.choiceRect2A = self.choiceText2A.get_rect(center = ((self.screen.get_width()*3/4, self.converter.conv_y(850))))
        self.choiceRect2B = self.choiceText2B.get_rect(center = ((self.screen.get_width()*3/4, self.converter.conv_y(935))))


        self.chosen = None

        self.vignette = create_radial_vignette((self.screen.get_width(), self.screen.get_height()))

        self.fade = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        self.fadeColor = [0,0,0,255]

    def handling_event(self, event):
        if event.type == pygame.QUIT: ##Si le joueur appuie sur la croix de la fenetre
            self.running = False ##Le jeu s'arrete


    def interraction(self, event):
        survol = False

        if hover(event, self.torchRect)[0] or self.chosen == 'torch':
            survol = True
            self.choice1 = True
            if hover(event, self.torchRect)[1] and not self.chosen:
                self.chosen = "torch"
                fade_out(self, 30)
        else:
            self.choice1 = False

        if hover(event, self.kegRect)[0] or self.chosen == 'keg':
            survol = True
            self.choice2 = True
            if hover(event, self.kegRect)[1] and not self.chosen:
                self.chosen = "keg"
                fade_out(self, 30)
        else:
            self.choice2 = False

        if survol:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def update(self):
        self.tickText = self.tickFont.render(str(self.tick),True,(255,255,255))
        if self.tick == 12:
            self.tick = 0
        else:
            self.tick += 1

    def display(self):
        self.screen.fill((0,0,0))
        
        self.screen.blit(self.bgImage,self.bgRect)
        
        self.screen.blit(self.logLeftImage, self.logLeftRect)
        self.screen.blit(self.logRightImage, self.logRightRect)
        self.screen.blit(self.logUpImage, self.logUpRect)

        self.screen.blit(self.fireCampSpriteAnimation[self.tick//4], self.fireCampSpriteAnimationRect[self.tick//4])
        
        if not self.chosen == 'keg':
            self.screen.blit(self.torchImage, self.torchRect)
        if not self.chosen == 'torch':
            self.screen.blit(self.kegImage, self.kegRect)

        self.screen.blit(self.vignette, (0,0))

        self.screen.blit(self.title, self.titleRect)
        if self.choice1:
            self.screen.blit(self.choiceText1A, self.choiceRect1A)
            self.screen.blit(self.choiceText1B, self.choiceRect1B)
        if self.choice2:
            self.screen.blit(self.choiceText2A, self.choiceRect2A)
            self.screen.blit(self.choiceText2B, self.choiceRect2B)

        self.screen.blit(self.tickText, self.tickText.get_rect(topleft = (0,0)))

        self.screen.blit(self.fade, (0,0))
        self.fade.fill(self.fadeColor)

        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.handling_event(event)
                self.interraction(event)
            self.update()
            self.display()
            self.clock.tick(30)