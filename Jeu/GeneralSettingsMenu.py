import pygame
import random

from Converter import Converter
from NameGenerator import generate_random_name
from CommonFonction import hover
from CommonVar import directory
import CommonVar
import Font
import RoleDefinition
import SpriteBank

class GeneralSettingsMenu:
    def __init__(self,screen):
        self.screen = screen

        self.converter = Converter(self.screen)

        self.settingsFont = pygame.font.Font(Font.jaini, self.converter.conv_y(40))

        self.rep = [["Durée d'une journée :",'journeyLongivity',0],
                    ["Nombre de créatures de départ :","creatureStartingNumber",2],
                    ["Maximum d'entités :","maximumEntity",3],
                    ["Reproduction hétéronormée :","straightReproduction",4],
                    ["Part définie de méchants :","villainPart",6],
                    ["Affichage du temps écoulé :","showClock",8]]
        
        for el in self.rep:
            setattr(self,f"{el[1]}Text",self.settingsFont.render(el[0],True,(255,255,255)))
            setattr(self,f"{el[1]}Rect",getattr(self,f"{el[1]}Text").get_rect(topleft=(self.converter.conv_x(100),self.converter.conv_y(380 + 40*el[2]))))

        ##+ et - pour les nombres
        self.plusIconImage = SpriteBank.logo['Plus']
        self.plusIconImage = pygame.transform.scale(self.plusIconImage,(self.converter.conv_x(20),self.converter.conv_y(20)))
        
        self.minusIconImage = SpriteBank.logo['Moins']
        self.minusIconImage = pygame.transform.scale(self.minusIconImage,(self.converter.conv_x(20),self.converter.conv_y(20)))

        ##Durée d'une journée
        self.settingJourneyLongivityText = self.settingsFont.render(str(CommonVar.commonDico['journeyLongivity']),True,(200,200,200))
        self.settingJourneyLongivityRect = self.settingJourneyLongivityText.get_rect(topleft=(self.converter.conv_x(130) + self.journeyLongivityRect.width,self.converter.conv_y(380)))
        self.journeyLongivityPlusRect = pygame.Rect(self.converter.conv_x(105) + self.journeyLongivityRect.width,self.converter.conv_y(410),self.converter.conv_x(20),self.converter.conv_y(20))
        self.journeyLongivityMinusRect = pygame.Rect(self.converter.conv_x(5) + self.settingJourneyLongivityRect.x + self.settingJourneyLongivityRect.width,410,20,20)

        self.journeyLongivityText2 = self.settingsFont.render("secondes (",True,(255,255,255))
        self.journeyLongivityRect2 = self.journeyLongivityText2.get_rect(topleft=(self.converter.conv_x(160) + self.journeyLongivityRect.width + self.settingJourneyLongivityRect.width,self.converter.conv_y(380)))

        minutesJourneyLongivity = CommonVar.commonDico['journeyLongivity']/60
        minutesJourneyLongivity = str(format(minutesJourneyLongivity,'.2f'))
        self.settingJourneyLongivityText2 = self.settingsFont.render(minutesJourneyLongivity,True,(255,255,255))
        self.settingJourneyLongivityRect2 = self.settingJourneyLongivityText2.get_rect(topleft=(self.converter.conv_x(5) + self.journeyLongivityRect2.x + self.journeyLongivityRect2.width,self.converter.conv_y(380)))

        self.journeyLongivityText3 = self.settingsFont.render("minutes )",True,(255,255,255))
        self.journeyLongivityRect3 = self.journeyLongivityText3.get_rect(topleft=(self.converter.conv_x(10) + self.settingJourneyLongivityRect2.x + self.settingJourneyLongivityRect2.width,self.converter.conv_y(380)))

        ##Nombre de créatures de départ
        self.settingCreatureStartingNumberText = self.settingsFont.render(str(CommonVar.savingDico['creatureStartingNumber']),True,(200,200,200))
        self.settingCreatureStartingNumberRect = self.settingCreatureStartingNumberText.get_rect(topleft=(self.converter.conv_x(130) + self.creatureStartingNumberRect.width,self.converter.conv_y(460)))
        self.creatureStartingNumberPlusRect = pygame.Rect(self.converter.conv_x(5) + self.settingCreatureStartingNumberRect.x + self.settingCreatureStartingNumberRect.width,self.converter.conv_y(480),self.converter.conv_x(20),self.converter.conv_y(20))
        self.creatureStartingNumberMinusRect = pygame.Rect(self.converter.conv_x(110) + self.creatureStartingNumberRect.width,self.converter.conv_y(480),self.converter.conv_x(20),self.converter.conv_y(20))

        ##Maximum d'entités
        self.settingMaximumEntityText = self.settingsFont.render(str(CommonVar.commonDico['maximumEntity']),True,(200,200,200))
        self.settingMaximumEntityRect = self.settingMaximumEntityText.get_rect(topleft=(self.converter.conv_x(130) + self.maximumEntityRect.width,self.converter.conv_y(500)))
        self.maximumEntityPlusRect = pygame.Rect(self.converter.conv_x(5) + self.settingMaximumEntityRect.x + self.settingMaximumEntityRect.width,self.converter.conv_y(520),self.converter.conv_x(20),self.converter.conv_y(20))
        self.maximumEntityMinusRect = pygame.Rect(self.converter.conv_x(105) + self.maximumEntityRect.width,self.converter.conv_y(520),self.converter.conv_x(20),self.converter.conv_y(20))

        ##Reproduction hétéronormée
        if CommonVar.savingDico['straightReproduction']:
            self.settingStraightReproductionIconImage = SpriteBank.logo['Bouton']['On']
        else:
            self.settingStraightReproductionIconImage = SpriteBank.logo['Bouton']['Off']
        self.settingStraightReproductionIconImage = pygame.transform.scale(self.settingStraightReproductionIconImage,(self.converter.conv_x(127*0.75),self.converter.conv_y(61*0.75)))
        self.settingStraightReproductionIconRect = pygame.Rect(self.converter.conv_x(110) + self.straightReproductionRect.width,self.converter.conv_y(547),self.converter.conv_x(127*0.75),self.converter.conv_y(61*0.75))

        ##Part définie de méchants
        if CommonVar.savingDico['villainPart']:
            self.settingVillainPartIconImage = SpriteBank.logo['Bouton']['On']
        else:
            self.settingVillainPartIconImage = SpriteBank.logo['Bouton']['Off']
        self.settingVillainPartIconImage = pygame.transform.scale(self.settingVillainPartIconImage,(self.converter.conv_x(127*0.75),self.converter.conv_y(61*0.75)))
        self.settingVillainPartIconRect = pygame.Rect(self.converter.conv_x(110) + self.villainPartRect.width,self.converter.conv_y(627),self.converter.conv_x(127*0.75),self.converter.conv_y(61*0.75))

        ##Affichage du temps écoulé
        if CommonVar.commonDico['showClock']:
            self.settingShowClockIconImage = SpriteBank.logo['Bouton']['On']
        else:
            self.settingShowClockIconImage = SpriteBank.logo['Bouton']['Off']
        self.settingShowClockIconImage = pygame.transform.scale(self.settingShowClockIconImage,(self.converter.conv_x(127*0.75),self.converter.conv_y(61*0.75)))
        self.settingShowClockIconRect = pygame.Rect(self.converter.conv_x(110) + self.showClockRect.width,self.converter.conv_y(707),self.converter.conv_x(127*0.75),self.converter.conv_y(61*0.75)) 

    def handling_event(self,survol,event):
        if hover(event,self.settingStraightReproductionIconRect)[0]:
            survol = True

            if hover(event,self.settingStraightReproductionIconRect)[1]:
                CommonVar.savingDico['straightReproduction'] = not CommonVar.savingDico['straightReproduction']

        if hover(event,self.settingVillainPartIconRect)[0]:
            survol = True

            if hover(event,self.settingVillainPartIconRect)[1]:
                CommonVar.savingDico['villainPart'] = not CommonVar.savingDico['villainPart']
                
        if hover(event,self.settingShowClockIconRect)[0]:
            survol = True

            if hover(event,self.settingShowClockIconRect)[1]:
                CommonVar.commonDico['showClock'] = not CommonVar.commonDico['showClock']

        if hover(event,self.journeyLongivityPlusRect)[0]:
            survol = True
            if hover(event,self.journeyLongivityPlusRect)[1]:
                if CommonVar.commonDico['journeyLongivity'] < 1000:
                    CommonVar.commonDico['journeyLongivity'] += 10

        if hover(event,self.journeyLongivityMinusRect)[0]:
            survol = True
            if hover(event,self.journeyLongivityMinusRect)[1]:
                if CommonVar.commonDico['journeyLongivity'] > 30:
                    CommonVar.commonDico['journeyLongivity'] -= 10
                    
        if hover(event,self.creatureStartingNumberPlusRect)[0]:
            survol = True
            if hover(event,self.creatureStartingNumberPlusRect)[1]:
                if CommonVar.savingDico['creatureStartingNumber'] < 20:
                    CommonVar.savingDico['creatureStartingNumber'] += 1
                    CommonVar.savingDico['creatureNumber'] = CommonVar.savingDico['creatureStartingNumber']
                    CommonVar.savingDico['creaturePositions'].append([self.converter.conv_x(928),self.converter.conv_y(508)])
                    CommonVar.savingDico['creatureId'].append(generate_random_name())
                    CommonVar.savingDico['creatureDestinations'].append(None)
                    CommonVar.savingDico['creatureSens'].append(None)
                    CommonVar.savingDico['creatureSprites'].append(random.randint(1,6))
                    CommonVar.savingDico['creatureTent'].append(random.randint(0,34))
                    CommonVar.savingDico['creatureTentState'].append(True)
                    CommonVar.savingDico['creatureTrust'].append([100 for i in range(CommonVar.savingDico['creatureNumber'])])
                    for i in range(CommonVar.savingDico['creatureNumber']-1):
                        CommonVar.savingDico['creatureTrust'][i].append(100)
                    RoleDefinition.definition()

        if hover(event,self.creatureStartingNumberMinusRect)[0]:
            survol = True
            if hover(event,self.creatureStartingNumberMinusRect)[1]:
                if CommonVar.savingDico['creatureStartingNumber'] > 2:
                    CommonVar.savingDico['creatureStartingNumber'] -= 1
                    CommonVar.savingDico['creatureNumber'] = CommonVar.savingDico['creatureStartingNumber']
                    CommonVar.savingDico['creaturePositions'].pop()
                    CommonVar.savingDico['creatureId'].pop()
                    CommonVar.savingDico['creatureDestinations'].pop()
                    CommonVar.savingDico['creatureSens'].pop()
                    CommonVar.savingDico['creatureSprites'].pop()
                    CommonVar.savingDico['creatureTent'].pop()
                    CommonVar.savingDico['creatureTentState'].pop()
                    CommonVar.savingDico['creatureTrust'].pop()
                    for i in range(CommonVar.savingDico['creatureNumber']-1):
                        CommonVar.savingDico['creatureTrust'][i].pop()
                    RoleDefinition.definition()
                    
        if hover(event,self.maximumEntityPlusRect)[0]:
            survol = True
            if hover(event,self.maximumEntityPlusRect)[1]:
                if CommonVar.commonDico['maximumEntity'] < 320:
                    CommonVar.commonDico['maximumEntity'] += 10

        if hover(event,self.maximumEntityMinusRect)[0]:
            survol = True
            if hover(event,self.maximumEntityMinusRect)[1]:
                if CommonVar.commonDico['maximumEntity'] >  CommonVar.savingDico['creatureStartingNumber'] + 10:
                    CommonVar.commonDico['maximumEntity']-= 10

        return survol

    def update(self):

        ##Durée d'une journée
        self.settingJourneyLongivityText = self.settingsFont.render(str(CommonVar.commonDico['journeyLongivity']),True,(200,200,200))
        self.settingJourneyLongivityRect = self.settingJourneyLongivityText.get_rect(topleft=(self.converter.conv_x(130) + self.journeyLongivityRect.width,self.converter.conv_y(380)))
        self.journeyLongivityPlusRect = pygame.Rect(self.converter.conv_x(5) + self.settingJourneyLongivityRect.x + self.settingJourneyLongivityRect.width,self.converter.conv_y(400),self.converter.conv_x(20),self.converter.conv_y(20))
        self.journeyLongivityMinusRect = pygame.Rect(self.converter.conv_x(105) + self.journeyLongivityRect.width,self.converter.conv_y(400),self.converter.conv_x(20),self.converter.conv_y(20))

        self.journeyLongivityText2 = self.settingsFont.render("secondes (",True,(255,255,255))
        self.journeyLongivityRect2 = self.journeyLongivityText2.get_rect(topleft=(self.converter.conv_x(160) + self.journeyLongivityRect.width + self.settingJourneyLongivityRect.width,self.converter.conv_y(380)))

        minutesJourneyLongivity = CommonVar.commonDico['journeyLongivity']/60
        minutesJourneyLongivity = str(format(minutesJourneyLongivity,'.2f'))
        self.settingJourneyLongivityText2 = self.settingsFont.render(minutesJourneyLongivity,True,(255,255,255))
        self.settingJourneyLongivityRect2 = self.settingJourneyLongivityText2.get_rect(topleft=(self.converter.conv_x(5) + self.journeyLongivityRect2.x + self.journeyLongivityRect2.width,self.converter.conv_y(380)))

        self.journeyLongivityText3 = self.settingsFont.render("minutes )",True,(255,255,255))
        self.journeyLongivityRect3 = self.journeyLongivityText3.get_rect(topleft=(self.converter.conv_x(10) + self.settingJourneyLongivityRect2.x + self.settingJourneyLongivityRect2.width,self.converter.conv_y(380)))

        ##Nombre de créatures de départ
        self.settingCreatureStartingNumberText = self.settingsFont.render(str(CommonVar.savingDico['creatureStartingNumber']),True,(200,200,200))
        self.settingCreatureStartingNumberRect = self.settingCreatureStartingNumberText.get_rect(topleft=(self.converter.conv_x(130) + self.creatureStartingNumberRect.width,self.converter.conv_y(460)))
        self.creatureStartingNumberPlusRect = pygame.Rect(self.converter.conv_x(5) + self.settingCreatureStartingNumberRect.x + self.settingCreatureStartingNumberRect.width,self.converter.conv_y(480),self.converter.conv_x(20),self.converter.conv_y(20))
        self.creatureStartingNumberMinusRect = pygame.Rect(self.converter.conv_x(105) + self.creatureStartingNumberRect.width,self.converter.conv_x(480),self.converter.conv_x(20),self.converter.conv_y(20))

        ##Maximum d'entités
        self.settingMaximumEntityText = self.settingsFont.render(str(CommonVar.commonDico['maximumEntity']),True,(200,200,200))
        self.settingMaximumEntityRect = self.settingMaximumEntityText.get_rect(topleft=(self.converter.conv_x(130) + self.maximumEntityRect.width,self.converter.conv_y(500)))
        self.maximumEntityPlusRect = pygame.Rect(self.converter.conv_x(5) + self.settingMaximumEntityRect.x + self.settingMaximumEntityRect.width,self.converter.conv_y(520),self.converter.conv_x(20),self.converter.conv_y(20))
        self.maximumEntityMinusRect = pygame.Rect(self.converter.conv_x(105) + self.maximumEntityRect.width,self.converter.conv_y(520),self.converter.conv_x(20),self.converter.conv_y(20))
        
        if CommonVar.savingDico['straightReproduction']:
            self.settingStraightReproductionIconImage = SpriteBank.logo['Bouton']['On']
        else:
            self.settingStraightReproductionIconImage = SpriteBank.logo['Bouton']['Off']
        self.settingStraightReproductionIconImage = pygame.transform.scale(self.settingStraightReproductionIconImage,(self.converter.conv_x(127*0.75),self.converter.conv_y(61*0.75)))

        if CommonVar.savingDico['villainPart']:
            self.settingVillainPartIconImage = SpriteBank.logo['Bouton']['On']
        else:
            self.settingVillainPartIconImage = SpriteBank.logo['Bouton']['Off']
        self.settingVillainPartIconImage = pygame.transform.scale(self.settingVillainPartIconImage,(self.converter.conv_x(127*0.75),self.converter.conv_y(61*0.75)))

        if CommonVar.commonDico['showClock']:
            self.settingShowClockIconImage = SpriteBank.logo['Bouton']['On']
        else:
            self.settingShowClockIconImage = SpriteBank.logo['Bouton']['Off']
        self.settingShowClockIconImage = pygame.transform.scale(self.settingShowClockIconImage,(self.converter.conv_x(127*0.75),self.converter.conv_y(61*0.75)))

    def display(self):
        for el in self.rep:
            text = getattr(self,f'{el[1]}Text')
            rect = getattr(self,f'{el[1]}Rect')
            self.screen.blit(text,rect)
        
        self.screen.blit(self.settingJourneyLongivityText,self.settingJourneyLongivityRect)
        self.screen.blit(self.plusIconImage,self.journeyLongivityPlusRect)
        self.screen.blit(self.minusIconImage,self.journeyLongivityMinusRect)
        self.screen.blit(self.journeyLongivityText2,self.journeyLongivityRect2)
        self.screen.blit(self.settingJourneyLongivityText2,self.settingJourneyLongivityRect2)
        self.screen.blit(self.journeyLongivityText3,self.journeyLongivityRect3)

        self.screen.blit(self.settingCreatureStartingNumberText,self.settingCreatureStartingNumberRect)
        self.screen.blit(self.plusIconImage,self.creatureStartingNumberPlusRect)
        self.screen.blit(self.minusIconImage,self.creatureStartingNumberMinusRect)

        self.screen.blit(self.settingMaximumEntityText,self.settingMaximumEntityRect)
        self.screen.blit(self.plusIconImage,self.maximumEntityPlusRect)
        self.screen.blit(self.minusIconImage,self.maximumEntityMinusRect)

        self.screen.blit(self.settingStraightReproductionIconImage,self.settingStraightReproductionIconRect)
        
        self.screen.blit(self.settingVillainPartIconImage,self.settingVillainPartIconRect)
        
        self.screen.blit(self.settingShowClockIconImage,self.settingShowClockIconRect)