import pygame
import random
import math
import copy

import SpriteBank
import CommonVar
from CommonVar import directory
from Converter import Converter

class BackgroundRandomSimulation :
    def __init__(self,screen):
        self.screen = screen
        self.alpha = 255

        self.commonVar = CommonVar.CommonVar()
        self.converter = Converter(self.screen)

        self.ordreAffichage = self.percepective(CommonVar.savingDico['creaturePositions'],[i for i in range(CommonVar.savingDico['creatureNumber'])])

        self.darknessBgSurface = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.darknessAlpha = 0

        self.bgImage = SpriteBank.fondMap['Jour']
        self.bgImage = pygame.transform.scale(self.bgImage,self.screen.get_size())
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

        for i in range(len(CommonVar.savingDico['creaturePositions'])):
            if CommonVar.savingDico['creatureSprites']:
                spriteStep1 = CommonVar.savingDico['creatureSprites'][i]-1 # Personnage
            else:
                spriteStep1 = 1
            spriteStep2 = "Static" # Action
            spriteStep3 = "Avant" # Direction
            spriteStep4 = 1 # Frame

            pnjImage = CommonVar.perso [spriteStep1] [spriteStep2] [spriteStep3] [spriteStep4]

            setattr(self,f'pnj{i}Image',pygame.transform.scale(pnjImage,(self.converter.conv_x(164),self.converter.conv_y(165))))
            setattr(self,f'pnj{i}Rect',getattr(self,f'pnj{i}Image').get_rect(topleft=(CommonVar.savingDico['creaturePositions'][i])))
            setattr(self,f'pnj{i}PreSens',[])
            setattr(self,f'pnj{i}Direction','Avant')
            setattr(self,f'pnj{i}Run','')
            setattr(self,f'pnj{i}Mod',0)
            setattr(self,f'pnj{i}Frame',1)

        self.tentPositions = [(self.converter.conv_x(200*u) + self.converter.conv_x(50),self.converter.conv_y(100*i)) for i in range(1,10) for u in range(0,2)] + [(self.screen.get_width() - (self.converter.conv_x(200)*u + self.converter.conv_x(178)),self.converter.conv_y(100)*i) for i in range(1,10) for u in range(0,2)]
        self.tentImage = SpriteBank.tente['Jour']['Droite']
        self.tentReverseImage = SpriteBank.tente['Jour']['Gauche']
        self.destroyedTentImage = SpriteBank.tente['Jour']['Détruite']
        self.tentImage = pygame.transform.scale(self.tentImage,(self.converter.conv_x(363*0.75),self.converter.conv_y(260*0.75)))
        self.destroyedTentImage = pygame.transform.scale(self.destroyedTentImage,(self.converter.conv_x(200*0.75),self.converter.conv_y(90*0.75)))
        self.tentReverseImage = pygame.transform.scale(self.tentReverseImage,(self.converter.conv_x(363*0.75),self.converter.conv_y(260*0.75)))

        tentRef = [self.tentPositions[i] for i in CommonVar.savingDico['creatureTent']]
        self.tentOrdreAffichage = []
        self.tentOrdreAffichage = self.percepective(tentRef,[i for i in range(len(CommonVar.savingDico['creatureTent']))])

    def handling_event(self):
        for event in pygame.event.get():
            pass
        
    def display(self):
        self.screen.blit(self.bgImage,self.bgRect) #Image de fond

        self.screen.blit(self.bgCampfireImage,self.bgCampfireRect) #Feu de camp

        self.screen.blit(self.bgLogHorizontalImage,self.bgLogUpRect) #Log haute
        self.screen.blit(self.bgLogHorizontalImage,self.bgLogDownRect) #Log basse
        self.screen.blit(self.bgLogVerticalImage,self.bgLogLeftRect) #Log droite
        self.screen.blit(self.bgLogVerticalImage,self.bgLogRightRect) #Log gauche

        # Affichage des creatures
        try:
            for i in self.ordreAffichage:
                try:
                    if CommonVar.savingDico['creatureTentState'][i]:
                        self.screen.blit(getattr(self,f'pnj{i}Image'),getattr(self,f'pnj{i}Rect'))
                except IndexError: pass
        except AttributeError: pass   
        
        for i in self.tentOrdreAffichage:
            if CommonVar.savingDico['creatureTentState'] and len(CommonVar.savingDico['creatureTentState']) == len(self.tentOrdreAffichage):
                if CommonVar.savingDico['creatureTentState'][i]:
                    if self.tentPositions[CommonVar.savingDico['creatureTent'][i]][0] > self.screen.get_width()/2:
                        self.screen.blit(self.tentImage,(self.tentPositions[CommonVar.savingDico['creatureTent'][i]][0],self.tentPositions[CommonVar.savingDico['creatureTent'][i]][1],128,128))
                    else:
                        self.screen.blit(self.tentReverseImage,(self.tentPositions[CommonVar.savingDico['creatureTent'][i]][0],self.tentPositions[CommonVar.savingDico['creatureTent'][i]][1],128,128))
                else:
                    self.screen.blit(self.destroyedTentImage,(self.tentPositions[CommonVar.savingDico['creatureTent'][i]][0],self.tentPositions[CommonVar.savingDico['creatureTent'][i]][1],128,128))

        ## Affichage du fondu enchainé (calque noir)
        self.screen.blit(self.darknessBgSurface,(0,0))
        self.darknessBgSurface.fill((0,0,0,self.darknessAlpha))

    def update(self):
        self.darknessAlpha = 255 - self.alpha

        if CommonVar.savingDico['creatureNumber'] and CommonVar.savingDico['creaturePositions']:
            CommonVar.savingDico['creatureNumber'] = len(CommonVar.savingDico['creaturePositions'])
            for i in range(CommonVar.savingDico['creatureNumber']):

                self.update_animation(i)
                
                try:
                    if CommonVar.savingDico['creaturePositions']:
                        setattr(self,f'pnj{i}Rect',getattr(self,f'pnj{i}Image').get_rect(topleft=CommonVar.savingDico['creaturePositions'][i]))
                        setattr(self,f'pnj{i}PreSens',CommonVar.savingDico['creatureSens'][i])
                except AttributeError: pass

                if CommonVar.savingDico['creatureDestinations']:
                    if CommonVar.savingDico['creatureDestinations'][i] == None and random.randint(0,100) == 0:
                        setattr(self,f'pnj{i}Mod',0)
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
                        if (destination[0] > position[0] and sens[0] < 0) or (destination[0] < position[0] and sens[0] > 0) or (destination[1] > position[1] and sens[1] < 0) or (destination[1] < position[1] and sens[1] > 0):
                            CommonVar.savingDico['creatureDestinations'][i] = None
                        else:
                            currentX = position[0]+sens[0]
                            currentY = position[1]+sens[1]
                            position = [currentX,currentY]
                            CommonVar.savingDico['creaturePositions'][i] = position
        
        if CommonVar.savingDico['creatureTent']:
            tentRef = [self.tentPositions[i] for i in CommonVar.savingDico['creatureTent']]
            self.tentOrdreAffichage = self.percepective(tentRef,[i for i in range(len(CommonVar.savingDico['creatureTent']))])

        positions = CommonVar.savingDico['creaturePositions']
        if positions:
            ordre = [i for i in range(len(positions))]
            self.ordreAffichage = self.percepective(positions,ordre)

    def update_animation(self,i):
                try:
                    if CommonVar.savingDico['creatureSens']:
                        if getattr(self,f'pnj{i}PreSens') != CommonVar.savingDico['creatureSens'][i]:
                            self.sprite = CommonVar.savingDico['creatureSprites'][i]
                            self.direction = "Avant"
                            if CommonVar.savingDico['creatureSens'][i]:
                                setattr(self,f'pnj{i}Running',True)
                                if CommonVar.savingDico['creatureSens'][i][0] > 0:
                                    if CommonVar.savingDico['creatureSens'][i][1] > 0:
                                        if CommonVar.savingDico['creatureSens'][i][0] > CommonVar.savingDico['creatureSens'][i][1]:
                                            setattr(self,f'pnj{i}Direction',"Droite")
                                        else:
                                            setattr(self,f'pnj{i}Direction',"Arriere")
                                    else:
                                        if CommonVar.savingDico['creatureSens'][i][0] > -CommonVar.savingDico['creatureSens'][i][1]:
                                            setattr(self,f'pnj{i}Direction',"Droite")
                                        else:
                                            setattr(self,f'pnj{i}Direction',"Avant")
                                else:
                                    if CommonVar.savingDico['creatureSens'][i][1] > 0:
                                        if -CommonVar.savingDico['creatureSens'][i][0] > CommonVar.savingDico['creatureSens'][i][1]:
                                            setattr(self,f'pnj{i}Direction',"Gauche")
                                        else:
                                            setattr(self,f'pnj{i}Direction',"Arriere")
                                    else:
                                        if -CommonVar.savingDico['creatureSens'][i][0] > -CommonVar.savingDico['creatureSens'][i][1]:
                                            setattr(self,f'pnj{i}Direction',"Gauche")
                                        else:
                                            setattr(self,f'pnj{i}Direction',"Avant")
                    
                    if getattr(self,f'pnj{i}Mod')%100 <= 20:
                        if getattr(self,f'pnj{i}Frame') < 16:
                            setattr(self,f'pnj{i}Frame',getattr(self,f'pnj{i}Frame')+1)
                        else:
                            setattr(self,f'pnj{i}Frame',1)

                    if CommonVar.savingDico['creatureSprites']:
                        spriteStep1 = CommonVar.savingDico['creatureSprites'][i]-1 # Personnage
                    else:
                        spriteStep1 = 1
                    spriteStep3 = getattr(self,f'pnj{i}Direction') # Direction

                    if getattr(self,f'pnj{i}Running'):
                        spriteStep2 = "Run" # Action
                        spriteStep4 = (getattr(self,f'pnj{i}Frame')//4)-1 # Frame
                    else:
                        spriteStep2 = "Static" # Action
                        spriteStep4 = (getattr(self,f'pnj{i}Frame')//8)-1 # Frame

                    pnjImage = CommonVar.perso [spriteStep1] [spriteStep2] [spriteStep3] [spriteStep4]
                    setattr(self,f'pnj{i}Image',pygame.transform.scale(pnjImage,(self.converter.conv_x(64*1.75),self.converter.conv_y(64*1.75))))

                except AttributeError :
                    setattr(self,f'pnj{i}PreSens',None)


    def sortab(self, tab):
        return sorted(tab, key=lambda x: x[1], reverse=True)

    def percepective(self,ref,tab):
        temp = self.sortab(ref)
        final = []

        for i in range(len(temp)):
            final.append(tab[ref.index(temp[-i])])

        return final