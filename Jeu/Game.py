import pygame 
import random
import math

import CommonVar
import Font
import SpriteBank
from CommonVar import directory
from CommonFonction import fade_out, fade_in
from Keybinds import keybinds
from Converter import Converter
from FloatingMenu import FloatingMenu
from InTent import InTent
from Vote import Vote

class Game:
    def __init__(self,screen):
        self.screen = screen
        self.running = False
        self.commonVar = CommonVar.CommonVar()
        self.converter = Converter(self.screen)
        self.floatingMenu = FloatingMenu(self.screen)
        self.inTent = InTent(self.screen)
        self.vote = Vote(self.screen)

        self.font = pygame.font.SysFont(None, 30) # Temporaire

        self.frame = 1

        self.zoomUp = False
        self.worldPos = [0,0]
        
        self.transitionBgSurface = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.fadeColor = [0,0,0,255]

        self.ordreAffichage = []
        self.percepective(CommonVar.savingDico['creaturePositions'],[i for i in range(len(CommonVar.savingDico['creaturePositions']))])

        self.clock = pygame.time.Clock()
        self.time = True
        self.startingTime = 0
        self.timer = pygame.USEREVENT +1
        pygame.time.set_timer(self.timer,1000,100)
        self.timeShow = int(CommonVar.savingDico['timeRemaining']) - self.startingTime
        self.timeShowConvert = str(self.timeShow//60).zfill(2) + ':' + str(self.timeShow%60).zfill(2)

        self.timeFont = pygame.font.Font(Font.jaini,100)
        self.timeText = self.timeFont.render(str(self.timeShowConvert),True,(255,255,255))
        self.timeSurface = pygame.Surface((190,110),pygame.SRCALPHA)
        self.timeRect = pygame.Rect(10,10,190,110)

        self.bgSurface = pygame.Surface(self.screen.get_size(),pygame.SRCALPHA)
        self.jour = True
        self.bgImage = SpriteBank.fondMap['Jour']
        self.bgImage = pygame.transform.scale(self.bgImage,self.screen.get_size())
        self.bgNuitImage = SpriteBank.fondMap['Nuit']
        self.bgNuitImage = pygame.transform.scale(self.bgNuitImage,self.screen.get_size())
        self.bgRect = self.screen.get_rect()

        self.bgCampfireImage = SpriteBank.feu['Jour']
        self.bgCampfireImage = pygame.transform.scale(self.bgCampfireImage,(self.converter.conv_x(160*0.75),self.converter.conv_y(225*0.75)))
        self.bgCampfireRect = self.bgCampfireImage.get_rect(center=(self.screen.get_width()/2,self.screen.get_height()/2-self.converter.conv_y(50)))

        self.bgLogHorizontalImage = SpriteBank.buche['Jour']['Haut']
        self.bgLogVerticalImage = SpriteBank.buche['Jour']['Gauche']
        self.bgLogHorizontalImage = pygame.transform.scale(self.bgLogHorizontalImage,(self.converter.conv_x(245*0.75),self.converter.conv_y(95*0.75)))
        self.bgLogVerticalImage = pygame.transform.scale(self.bgLogVerticalImage,(self.converter.conv_x(105*0.75),self.converter.conv_y(220*0.75)))
        self.bgLogUpRect = self.bgLogHorizontalImage.get_rect(center=(self.screen.get_width()/2,self.converter.conv_y(400)))
        self.bgLogDownRect = self.bgLogHorizontalImage.get_rect(center=(self.screen.get_width()/2,self.converter.conv_y(650)))
        self.bgLogLeftRect = self.bgLogVerticalImage.get_rect(center=(self.converter.conv_y(750),self.screen.get_height()/2-self.converter.conv_y(20)))
        self.bgLogRightRect = self.bgLogVerticalImage.get_rect(center=(self.converter.conv_y(1200),self.screen.get_height()/2-self.converter.conv_y(20)))
        
        nameFont = pygame.font.Font(Font.inter,30)
        for i in range(len(CommonVar.savingDico['creaturePositions'])):
            if CommonVar.savingDico['creatureSprites']:
                spriteStep1 = CommonVar.savingDico['creatureSprites'][i]-1 # Personnage
            else:
                spriteStep1 = 1
            spriteStep2 = "Static" # Action
            spriteStep3 = "Avant" # Direction
            spriteStep4 = 1 # Frame

            pnjImage = CommonVar.perso [spriteStep1] [spriteStep2] [spriteStep3] [spriteStep4]

            setattr(self,f'pnj{i}ImageRef',pygame.transform.scale(pnjImage,(self.converter.conv_x(164),self.converter.conv_y(165))))
            setattr(self,f'pnj{i}Image',getattr(self,f'pnj{i}ImageRef'))
            setattr(self,f'pnj{i}Rect',getattr(self,f'pnj{i}Image').get_rect(topleft=CommonVar.savingDico['creaturePositions'][i]))
            setattr(self,f'pnj{i}Name',nameFont.render(CommonVar.savingDico['creatureId'][i],True,(255,255,255)))
            setattr(self,f'pnj{i}NameRect',getattr(self,f'pnj{i}Name').get_rect(center=(CommonVar.savingDico['creaturePositions'][i][0] + self.converter.conv_x(32),CommonVar.savingDico['creaturePositions'][i][1] - self.converter.conv_y(30))))
            setattr(self,f'pnj{i}Direction','Avant')
            setattr(self,f'pnj{i}Running',False)
            setattr(self,f'pnj{i}Mod',0)
            setattr(self,f'pnj{i}Frame',1)

        self.repertDestinationSurface = pygame.Surface((self.converter.conv_x(64),self.converter.conv_y(64)),pygame.SRCALPHA)
        self.repertDestinationPos = (self.screen.get_width(),self.screen.get_height())

        self.tentPositions = [(self.converter.conv_x(200*u) + self.converter.conv_x(50),self.converter.conv_y(100*i)) for i in range(1,10) for u in range(0,2)] + [(self.screen.get_width() - (self.converter.conv_x(200)*u + self.converter.conv_x(178)),self.converter.conv_y(100)*i) for i in range(1,10) for u in range(0,2)]
        self.tentImage = SpriteBank.tente['Jour']['Droite']
        self.tentReverseImage = SpriteBank.tente['Jour']['Gauche']
        self.destroyedTentImage = SpriteBank.tente['Jour']['Détruite']
        self.tentImage = pygame.transform.scale(self.tentImage,(self.converter.conv_x(363*.5),self.converter.conv_y(260*.5)))
        self.destroyedTentImage = pygame.transform.scale(self.destroyedTentImage,(self.converter.conv_x(200*0.75),self.converter.conv_y(95*0.75)))
        self.tentReverseImage = pygame.transform.scale(self.tentImage,(self.converter.conv_x(363*.5),self.converter.conv_y(260*.5)))

    def handling_event(self,window):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: ##Si le joueur appuie sur la croix de la fenetre
                self.commonVar.update_saving_json()
                self.commonVar.update_common_json()
                pygame.quit() ##Le jeu s'arrete
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                self.floatingMenu.opening()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.jour:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                destination = pygame.mouse.get_pos()
                destination = [destination[0]-32,destination[1]-32]
                currentPos = CommonVar.savingDico['creaturePositions'][0]
                CommonVar.savingDico['creatureDestinations'][0] = destination
                distance = math.sqrt((destination[0]-currentPos[0])**2 + (destination[1]-currentPos[1])**2)
                sensX = 5*(destination[0]-currentPos[0])/distance
                sensY = 5*(destination[1]-currentPos[1])/distance
                sens = [sensX,sensY]
                CommonVar.savingDico['creatureSens'][0] = sens
                self.repertDestinationPos = (destination[0],destination[1])
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            if event.type == self.timer and self.jour:
                CommonVar.savingDico['timeRemaining'] += 1

            keys = pygame.key.get_pressed()
            if keys[keybinds['openMenu']] and self.jour:
                fade_out(self, 30)
                fade_in(window.menu, 30)

            if event.type == pygame.KEYDOWN and keys[keybinds['skipJourney']]:
                CommonVar.savingDico['timeRemaining'] += 1

            if event.type == pygame.KEYDOWN and keys[keybinds['centerCamera']]:
                self.zoomUp = not self.zoomUp

    def update(self):
        if self.bgImage.get_alpha():
            if self.jour and self.bgImage.get_alpha() < 230:
                self.bgImage.set_alpha(self.bgImage.get_alpha() + 25)
            elif not self.jour and self.bgImage.get_alpha() > 25:
                self.bgImage.set_alpha(self.bgImage.get_alpha() - 25)
        if self.jour:
            self.timeShow = CommonVar.commonDico['journeyLongivity'] - CommonVar.savingDico['timeRemaining']
            self.timeShowConvert = self.timeShowConvert = str(self.timeShow//60).zfill(2) + ':' + str(self.timeShow%60).zfill(2)
            self.timeText = self.timeFont.render(str(self.timeShowConvert),True,(255,255,255))
        if CommonVar.commonDico['journeyLongivity'] <= CommonVar.savingDico['timeRemaining']:
            self.jour = False
            CommonVar.savingDico['timeRemaining'] = 0
            self.timeShow = CommonVar.commonDico['journeyLongivity'] - CommonVar.savingDico['timeRemaining']
            self.timeShowConvert = self.timeShowConvert = str(self.timeShow//60).zfill(2) + ':' + str(self.timeShow%60).zfill(2)
            for i in range(CommonVar.savingDico['creatureNumber']):
                CommonVar.savingDico['creatureDestinations'][i] = [0,0]
                CommonVar.savingDico['creatureDestinations'][i][0] = self.tentPositions[CommonVar.savingDico['creatureTent'][i]][0] + self.converter.conv_x(32)
                CommonVar.savingDico['creatureDestinations'][i][1] = self.tentPositions[CommonVar.savingDico['creatureTent'][i]][1] + self.converter.conv_x(32)

                currentX = CommonVar.savingDico['creaturePositions'][i][0]
                currentY = CommonVar.savingDico['creaturePositions'][i][1]
                distance = math.sqrt((CommonVar.savingDico['creatureDestinations'][i][0]-currentX)**2 + (CommonVar.savingDico['creatureDestinations'][i][1]-currentY)**2)

                sensX = 10*(CommonVar.savingDico['creatureDestinations'][i][0]-currentX)/distance
                sensY = 10*(CommonVar.savingDico['creatureDestinations'][i][1]-currentY)/distance
                sens = [sensX,sensY]
                CommonVar.savingDico['creatureSens'][i] = sens

        if CommonVar.savingDico['creatureDestinations'][0] == None and not self.jour:
            fade_out(self, 30)
            fade_in(self.inTent, 30)
            self.jour = True
            self.startingTime = 0

        CommonVar.savingDico['creatureNumber'] = len(CommonVar.savingDico['creaturePositions'])
        for i in range(len(CommonVar.savingDico['creaturePositions'])):
            sprite = CommonVar.savingDico['creatureSprites'][i]
            if i == 0 and not CommonVar.savingDico['creatureDestinations'][0]:
                setattr(self,f'pnj{i}Running',False)
            elif CommonVar.savingDico['creatureDestinations'][i]:
                setattr(self,f'pnj{i}Running',True)
                if CommonVar.savingDico['creatureSens'][i] and CommonVar.savingDico['creatureTentState'][i]:
                    if CommonVar.savingDico['creatureSens'][i][0] > 0:
                        if CommonVar.savingDico['creatureSens'][i][1] > 0:
                            if CommonVar.savingDico['creatureSens'][i][0] > CommonVar.savingDico['creatureSens'][i][1]:
                                setattr(self,f'pnj{i}Direction','Droite')
                            else:
                                setattr(self,f'pnj{i}Direction','Arriere')
                        else:
                            if CommonVar.savingDico['creatureSens'][i][0] > -CommonVar.savingDico['creatureSens'][i][1]:
                                setattr(self,f'pnj{i}Direction','Droite')
                            else:
                                setattr(self,f'pnj{i}Direction','Avant')
                    else:
                        if CommonVar.savingDico['creatureSens'][i][1] > 0:
                            if -CommonVar.savingDico['creatureSens'][i][0] > CommonVar.savingDico['creatureSens'][i][1]:
                                setattr(self,f'pnj{i}Direction','Gauche')
                            else:
                                setattr(self,f'pnj{i}Direction','Arriere')
                        else:
                            if -CommonVar.savingDico['creatureSens'][i][0] > -CommonVar.savingDico['creatureSens'][i][1]:
                                setattr(self,f'pnj{i}Direction','Gauche')
                            else:
                                setattr(self,f'pnj{i}Direction','Avant')
            
            if (pygame.time.get_ticks()+getattr(self,f'pnj{i}Mod'))%100 <= 20:
                        if getattr(self,f'pnj{i}Frame') < 4:
                            setattr(self,f'pnj{i}Frame',getattr(self,f'pnj{i}Frame')+1)
                        else:
                            setattr(self,f'pnj{i}Frame',1)
            
            if CommonVar.savingDico['creatureSprites']:
                spriteStep1 = CommonVar.savingDico['creatureSprites'][i]-1 # Personnage
            else:
                spriteStep1 = 1
            spriteStep3 = getattr(self,f'pnj{i}Direction') # Direction

            if getattr(self,f'pnj{i}Running'):
                spriteStep2 = "Run" # Run 
                spriteStep4 = getattr(self,f'pnj{i}Frame')-1 # Frame
            else:
                spriteStep2 = "Static" # Action
                spriteStep4 = getattr(self,f'pnj{i}Frame')%2 # Frame

            pnjImage = SpriteBank.perso [spriteStep1] [spriteStep2] [spriteStep3] [spriteStep4]
            setattr(self,f'pnj{i}Image',pygame.transform.scale(pnjImage,(self.converter.conv_x(64*1.25),self.converter.conv_y(64*1.25))))
            setattr(self,f'pnj{i}Rect',getattr(self,f'pnj{i}Image').get_rect(topleft=CommonVar.savingDico['creaturePositions'][i]))

            nameFont = pygame.font.Font(Font.inter,30)
            setattr(self,f'pnj{i}Name',nameFont.render(CommonVar.savingDico['creatureId'][i],True,(255,255,255)))
            setattr(self,f'pnj{i}NameRect',getattr(self,f'pnj{i}Name').get_rect(center=(CommonVar.savingDico['creaturePositions'][i][0] + self.converter.conv_x(32),CommonVar.savingDico['creaturePositions'][i][1] - self.converter.conv_y(30))))


            if CommonVar.savingDico['creatureDestinations'][i] == None and i != 0 and self.jour and random.randint(0,100) == 0:
                setattr(self,f'pnj{i}Mod',pygame.time.get_ticks()%23)
                x = 1920 - 100
                y = 1080 - 100
                destinationX = self.converter.conv_x(random.randint(100,x))
                destinationY = self.converter.conv_y(random.randint(100,y))
                CommonVar.savingDico['creatureDestinations'][i] = [destinationX,destinationY]
                currentX = CommonVar.savingDico['creaturePositions'][i][0]
                currentY = CommonVar.savingDico['creaturePositions'][i][1]

                ## DAMN ON A UTILISE LE THEOREME DE PYTHAGORE EN PYTHON
                distance = math.sqrt((destinationX-currentX)**2 + (destinationY-currentY)**2)

                sensX = 3*(destinationX-currentX)/distance
                sensY = 3*(destinationY-currentY)/distance
                sens = [sensX,sensY]
                CommonVar.savingDico['creatureSens'][i] = sens
            elif CommonVar.savingDico['creatureDestinations'][i] == None:
                setattr(self,f'pnj{i}Running',False)
            else:
                position = CommonVar.savingDico['creaturePositions'][i]
                destination = CommonVar.savingDico['creatureDestinations'][i]
                sens = CommonVar.savingDico['creatureSens'][i]
                if CommonVar.savingDico['creatureDestinations'][i] != None:
                    if (destination[0] > position[0] and sens[0] < 0) or (destination[0] < position[0] and sens[0] > 0) or (destination[1] > position[1] and sens[1] < 0) or (destination[1] < position[1] and sens[1] > 0):
                        CommonVar.savingDico['creatureDestinations'][i] = None
                    else:
                        currentX = position[0]+sens[0]
                        currentY = position[1]+sens[1]
                        position = [currentX,currentY]
                        CommonVar.savingDico['creaturePositions'][i] = position

        positions = CommonVar.savingDico['creaturePositions']
        ordre = [i for i in range(len(positions))]
        self.ordreAffichage = self.percepective(positions,ordre)

    def display(self):
        self.bgSurface.blit(self.bgNuitImage,self.bgRect)
        self.bgSurface.blit(self.bgImage,self.bgRect)
        if self.zoomUp:
            self.screen.blit(self.bgSurface,(0-self.worldPos[0],0-self.worldPos[1]))
        else:
            self.screen.blit(self.bgSurface,(0,0))

        self.screen.blit(self.bgCampfireImage,self.bgCampfireRect) #Feu de camp

        self.screen.blit(self.bgLogHorizontalImage,self.bgLogUpRect) #Log haute
        self.screen.blit(self.bgLogHorizontalImage,self.bgLogDownRect) #Log basse
        self.screen.blit(self.bgLogVerticalImage,self.bgLogLeftRect) #Log droite
        self.screen.blit(self.bgLogVerticalImage,self.bgLogRightRect) #Log gauche

        if CommonVar.savingDico['creatureDestinations'][0]:
            self.screen.blit(self.repertDestinationSurface,self.repertDestinationPos)
        self.repertDestinationSurface.fill((200,200,255,50))
        
        for i in self.ordreAffichage:
            if CommonVar.savingDico['creatureTentState'][i]:
                self.screen.blit(getattr(self,f'pnj{i}Image'),getattr(self,f'pnj{i}Rect'))
                self.screen.blit(getattr(self,f'pnj{i}Name'),getattr(self,f'pnj{i}NameRect'))

        for i in range(len(CommonVar.savingDico['creatureTent'])):
            if CommonVar.savingDico['creatureTentState'][i]:
                if self.tentPositions[CommonVar.savingDico['creatureTent'][i]][0] > self.screen.get_width()/2:
                    self.screen.blit(self.tentImage,(self.tentPositions[CommonVar.savingDico['creatureTent'][i]][0],self.tentPositions[CommonVar.savingDico['creatureTent'][i]][1],128,128))
                else:
                    self.screen.blit(self.tentReverseImage,(self.tentPositions[CommonVar.savingDico['creatureTent'][i]][0],self.tentPositions[CommonVar.savingDico['creatureTent'][i]][1],128,128))
            else:
                self.screen.blit(self.destroyedTentImage,(self.tentPositions[CommonVar.savingDico['creatureTent'][i]][0],self.tentPositions[CommonVar.savingDico['creatureTent'][i]][1],128,128))

        fps_text = self.font.render(f"FPS: {int(self.clock.get_fps())}", True, (255, 255, 255))
        self.screen.blit(fps_text, (10, 10))
        
        self.screen.blit(self.timeSurface,self.timeRect)
        self.screen.blit(self.timeText,self.timeText.get_rect(topleft=(0,0)))

        ## Affichage du fondu enchainé (calque noir)
        self.screen.blit(self.transitionBgSurface,(0,0))
        self.transitionBgSurface.fill(self.fadeColor)

                
        if not self.floatingMenu.running:
            pygame.display.flip()

    def run(self,window):
        if self.running:
            self.inTent.run(window)
            self.vote.run(window)
            self.handling_event(window)
            self.update()
            self.display()
            self.floatingMenu.run(self)

    def sortab(self,tab):
        return sorted(tab, key=lambda x: x[1], reverse=True)

    def percepective(self,ref,tab):
        temp = self.sortab(ref)
        final = []

        for i in range(len(temp)):
            final.append(tab[ref.index(temp[-i])])

        return final

    def add_time(self):
        self.startingTime += 1