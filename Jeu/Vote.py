import pygame
import math

from Keybinds import keybinds
from Converter import Converter
from CommonFonction import hover
from CommonVar import directory
import CommonVar
import Font
import Choose
import SpriteBank

class Vote:
    def __init__(self,screen):
        self.screen = screen
        self.running = False

        self.transitionBgSurface = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.fadeColor = [0,0,0,0]
        
        self.zoom = 1

        self.frame = 1

        self.commonVar = CommonVar.CommonVar()
        self.converter = Converter(self.screen)

        self.ordreAffichage = []
        self.percepective(CommonVar.savingDico['creaturePositions'],[i for i in range(len(CommonVar.savingDico['creaturePositions']))])

        self.bgSurface = pygame.Surface(self.screen.get_size(),pygame.SRCALPHA)
        self.bgImage = SpriteBank.fondMap['Jour']
        self.bgImage = pygame.transform.scale(self.bgImage,(self.screen.get_width()*self.zoom,self.screen.get_height()*self.zoom))
        self.bgNuitImage = SpriteBank.fondMap['Nuit']
        self.bgNuitImage = pygame.transform.scale(self.bgNuitImage,(self.screen.get_width()*self.zoom,self.screen.get_height()*self.zoom))
        self.bgRect = self.screen.get_size()

        nameFont = pygame.font.Font(Font.inter,30)
        for i in range(len(CommonVar.savingDico['creaturePositions'])):
            sprite = CommonVar.savingDico['creatureSprites'][i]-1
            pnjImage = SpriteBank.perso[sprite]['Static']['Avant'][0]
            setattr(self,f'pnj{i}ImageRef',pygame.transform.scale(pnjImage,(self.converter.conv_x(64),self.converter.conv_y(64))))
            setattr(self,f'pnj{i}Image',getattr(self,f'pnj{i}ImageRef'))
            setattr(self,f'pnj{i}Rect',getattr(self,f'pnj{i}Image').get_rect(topleft=CommonVar.savingDico['creaturePositions'][i]))
            if i == 0:
                setattr(self,f'pnj{i}Name',nameFont.render("VOUS",True,(255,255,255)))
            else:
                setattr(self,f'pnj{i}Name',nameFont.render(CommonVar.savingDico['creatureId'][i],True,(255,255,255)))
            setattr(self,f'pnj{i}NameRect',getattr(self,f'pnj{i}Name').get_rect(center=(CommonVar.savingDico['creaturePositions'][i][0],CommonVar.savingDico['creaturePositions'][i][1] - self.converter.conv_y(30))))

        self.selectedId = None
        self.selectionRect = pygame.Rect(0,0,self.converter.conv_x(128*self.zoom),self.converter.conv_y(128*self.zoom))
        self.selectionRectColor = [0,103,199]
        self.selectionRectShow = False
        self.selectionSelectedRect = self.selectionRect
        self.selectionSelectedRectShow = False
        self.selectionSelectedRectColor = [48,198,48]
        self.selectionConfirmationButtonFont = pygame.font.Font(Font.jaini,self.converter.conv_y(80))
        self.selectionConfirmationButtonText = self.selectionConfirmationButtonFont.render('Confirmer',True,(255,255,255))
        self.selectionConfirmationButtonTextRect = self.selectionConfirmationButtonText.get_rect(center=(self.screen.get_width()/2,self.screen.get_height()/2))
        self.selectionConfirmationButtonRect = pygame.Rect(self.screen.get_width()/2-self.converter.conv_x(9*16),self.screen.get_height()/2-self.converter.conv_y(40),self.converter.conv_x(9*32),self.converter.conv_y(80))
        self.selectionConfirmationButtonColor = [48,198,48]

        self.tentPositions = [(self.converter.conv_x(200*u) + self.converter.conv_x(50),self.converter.conv_y(100*i)) for i in range(1,10) for u in range(0,2)] + [(self.screen.get_width() - (self.converter.conv_x(200)*u + self.converter.conv_x(178)),self.converter.conv_y(100)*i) for i in range(1,10) for u in range(0,2)]
       
        self.toKill = None
        self.killEvent = pygame.USEREVENT + 1

        self.voteText = 'votez pour la personne à éliminer'
        self.voteRect = pygame.Rect(0,0,len(self.voteText)*self.converter.conv_x(29),self.converter.conv_y(80))
        self.voteSurface = pygame.Surface((len(self.voteText)*self.converter.conv_x(29),self.converter.conv_y(80)),pygame.SRCALPHA)
        self.voteAlpha = 0
        self.voteTextFont = pygame.font.Font(Font.IMfell,self.converter.conv_x(60))
        self.voteTextText = self.voteTextFont.render(self.voteText,True,(255,255,255))
        self.voteTextRect = self.voteTextText.get_rect(topleft=(self.converter.conv_x(10),0))

        self.votePossibility = True

    def handling_event(self,window):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: ##Si le joueur appuie sur la croix de la fenetre
                self.commonVar.update_saving_json()
                self.commonVar.update_common_json()
                pygame.quit() ##Le jeu s'arrete

            if event.type == self.killEvent:
                if self.toKill:
                    self.kill(self.toKill)
                    self.fade_to_game(window)

            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN and keys[keybinds['openMenu']]:
                self.fade_to_menus(window)

            survol = False
            self.selectionRectShow = False
            if CommonVar.savingDico['creatureDestinations'] == [None for _ in range(CommonVar.savingDico['creatureNumber'])] and self.votePossibility:
                for i in range(CommonVar.savingDico['creatureNumber']):
                    if CommonVar.savingDico['creatureTentState'][i]:
                        tempPnjRect = pygame.Rect(getattr(self,f'pnj{i}Rect')[0]*self.zoom+self.bgRect[0],getattr(self,f'pnj{i}Rect')[1]*self.zoom+self.bgRect[1],getattr(self,f'pnj{i}Rect')[2],getattr(self,f'pnj{i}Rect')[3])
                        if hover(event,tempPnjRect)[0]:
                            self.selectionRect = pygame.Rect(tempPnjRect[0]-self.converter.conv_x(10),tempPnjRect[1]-self.converter.conv_y(10),self.converter.conv_x(74*self.zoom),self.converter.conv_y(74*self.zoom))
                            survol = True
                            self.selectionRectShow = True
                            if hover(event,tempPnjRect)[1]:
                                self.selectionSelectedRect = self.selectionRect
                                self.selectionSelectedRectShow = True
                                self.selectedId = i
            if self.selectionSelectedRectShow and self.votePossibility:
                if hover(event,self.selectionConfirmationButtonRect)[0]:
                    survol = True
                    self.selectionConfirmationButtonColor = [48,198,48]
                    if hover(event,self.selectionConfirmationButtonRect)[1]:
                        choose = [0 for i in range(CommonVar.savingDico['creatureNumber'])]
                        for i in range(CommonVar.savingDico['creatureNumber']):
                            if CommonVar.savingDico['creatureTentState'][i] and i != 0:
                                botChoose = Choose.bad('id',i)
                                while not CommonVar.savingDico['creatureTentState'][botChoose]:
                                    botChoose = Choose.bad('id',i)
                                choose[Choose.bad('id',i)] += 1
                        choose[self.selectedId] += 1

                        print(choose)

                        self.toKill = Choose.max_tab_i(choose)
                        if self.toKill:
                            self.kill(self.toKill)
                            self.voteText = f"le village a décidé d'éliminer {CommonVar.savingDico['creatureId'][self.toKill]} ({max(choose)} voix)"
                            self.voteRect = pygame.Rect(0,0,len(self.voteText)*self.converter.conv_x(29),self.converter.conv_y(80))
                            self.voteSurface = pygame.Surface((len(self.voteText)*self.converter.conv_x(29),self.converter.conv_y(80)),pygame.SRCALPHA)
                            self.voteTextText = self.voteTextFont.render(self.voteText,True,(255,255,255))
                            self.voteTextRect = self.voteTextText.get_rect(topleft=(self.converter.conv_x(10),0))
                        else:
                            self.voteText = "le village n'a pas réussi à se décider : personne n'est mort"
                            self.voteRect = pygame.Rect(0,0,len(self.voteText)*self.converter.conv_x(29),self.converter.conv_y(80))
                            self.voteSurface = pygame.Surface((len(self.voteText)*self.converter.conv_x(29),self.converter.conv_y(80)),pygame.SRCALPHA)
                            self.voteTextText = self.voteTextFont.render(self.voteText,True,(255,255,255))
                            self.voteTextRect = self.voteTextText.get_rect(topleft=(self.converter.conv_x(10),0))
                        self.votePossibility = False
                        pygame.time.set_timer(self.killEvent,5000)
                        self.selectionSelectedRectShow = False

            else:
                self.selectionConfirmationButtonColor = [0,89,19]

            if survol :
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def update(self):
        if self.fadeColor[3] > 10:
            self.bgImage.set_alpha(self.bgImage.get_alpha() + 10)
            self.zoom *= 1.02
        else:
            if self.voteAlpha < 255:
                self.voteAlpha += 25.5
        
        self.bgRect = pygame.Rect(-self.screen.get_width()*(self.zoom-1)/2-self.converter.conv_x(10),-self.screen.get_height()*(self.zoom-1)/2,self.screen.get_width(),self.screen.get_height())
        self.bgImage = pygame.transform.scale(self.bgImage,(self.screen.get_width()*self.zoom,self.screen.get_height()*self.zoom))
        self.bgNuitImage = pygame.transform.scale(self.bgNuitImage,(self.screen.get_width()*self.zoom,self.screen.get_height()*self.zoom))
            
        if CommonVar.savingDico['creatureDestinations'] == [None for _ in range(CommonVar.savingDico['creatureNumber'])]:
            for i in range(CommonVar.savingDico['creatureNumber']):
                x = math.sin((i*2*math.pi)/CommonVar.savingDico['creatureNumber'])
                y = math.cos((i*2*math.pi)/CommonVar.savingDico['creatureNumber'])
                sprite = CommonVar.savingDico['creatureSprites'][i]-1
                if x >= 0:
                    if y >= 0:
                        if x > y:
                            pnjImage = SpriteBank.perso[sprite]['Static']['Gauche'][0]
                        else:
                            pnjImage = SpriteBank.perso[sprite]['Static']['Avant'][0]
                    else:
                        if x > -y:
                            pnjImage = SpriteBank.perso[sprite]['Static']['Gauche'][0]
                        else:
                            pnjImage = SpriteBank.perso[sprite]['Static']['Arriere'][0]
                else:
                    if y >= 0:
                        if -x > y:
                            pnjImage = SpriteBank.perso[sprite]['Static']['Droite'][0]
                        else:
                            pnjImage = SpriteBank.perso[sprite]['Static']['Avant'][0]
                    else:
                        if -x > -y:
                            pnjImage = SpriteBank.perso[sprite]['Static']['Droite'][0]
                        else:
                            pnjImage = SpriteBank.perso[sprite]['Static']['Arriere'][0]
                            
                nameFont = pygame.font.Font(Font.inter,30)
                setattr(self,f'pnj{i}Image',pygame.transform.scale(pnjImage,(self.converter.conv_x(64*self.zoom),self.converter.conv_y(64*self.zoom))))
                setattr(self,f'pnj{i}Rect',getattr(self,f'pnj{i}Image').get_rect(topleft=CommonVar.savingDico['creaturePositions'][i]))
                if i == 0:
                    setattr(self,f'pnj{i}Name',nameFont.render("VOUS",True,(255,255,255)))
                else:
                    setattr(self,f'pnj{i}Name',nameFont.render(CommonVar.savingDico['creatureId'][i],True,(255,255,255)))
                setattr(self,f'pnj{i}NameRect',getattr(self,f'pnj{i}Name').get_rect(center=(CommonVar.savingDico['creaturePositions'][i][0],CommonVar.savingDico['creaturePositions'][i][1] - self.converter.conv_y(30))))

        else:
            for i in range(CommonVar.savingDico['creatureNumber']):
                destination = CommonVar.savingDico['creatureDestinations'][i]
                sens = CommonVar.savingDico['creatureSens'][i]
                position = CommonVar.savingDico['creaturePositions'][i]
                if CommonVar.savingDico['creatureDestinations'][i] != None:
                    if (destination[0] > position[0] and sens[0] < 0) or (destination[0] < position[0] and sens[0] > 0) or (destination[1] > position[1] and sens[1] < 0) or (destination[1] < position[1] and sens[1] > 0):
                        CommonVar.savingDico['creatureDestinations'][i] = None
                    else:
                        currentX = position[0]+sens[0]
                        currentY = position[1]+sens[1]
                        position = [currentX,currentY]
                        CommonVar.savingDico['creaturePositions'][i] = position

                sprite = CommonVar.savingDico['creatureSprites'][i]-1
                if i == 0 and not CommonVar.savingDico['creatureDestinations'][0]:
                            pnjImage = SpriteBank.perso[sprite]['Run']['Arriere'][0]
                else:
                    if CommonVar.savingDico['creatureSens'][i]:
                        if CommonVar.savingDico['creatureSens'][i][0] > 0:
                            if CommonVar.savingDico['creatureSens'][i][1] > 0:
                                if CommonVar.savingDico['creatureSens'][i][0] > CommonVar.savingDico['creatureSens'][i][1]:
                                    pnjImage = SpriteBank.perso[sprite]['Run']['Droite'][0]
                                else:
                                    pnjImage = SpriteBank.perso[sprite]['Run']['Arriere'][0]
                            else:
                                if CommonVar.savingDico['creatureSens'][i][0] > -CommonVar.savingDico['creatureSens'][i][1]:
                                    pnjImage = SpriteBank.perso[sprite]['Run']['Droite'][0]
                                else:
                                    pnjImage = SpriteBank.perso[sprite]['Run']['Arriere'][0]
                        else:
                            if CommonVar.savingDico['creatureSens'][i][1] > 0:
                                if -CommonVar.savingDico['creatureSens'][i][0] > CommonVar.savingDico['creatureSens'][i][1]:
                                    pnjImage = SpriteBank.perso[sprite]['Run']['Gauche'][0]
                                else:
                                    pnjImage = SpriteBank.perso[sprite]['Run']['Arriere'][0]
                            else:
                                if -CommonVar.savingDico['creatureSens'][i][0] > -CommonVar.savingDico['creatureSens'][i][1]:
                                    pnjImage = SpriteBank.perso[sprite]['Run']['Gauche'][0]
                                else:
                                    pnjImage = SpriteBank.perso[sprite]['Run']['Avant'][0]
                                
                nameFont = pygame.font.Font(Font.inter,30)
                setattr(self,f'pnj{i}Image',pygame.transform.scale(pnjImage,(self.converter.conv_x(64*self.zoom),self.converter.conv_y(64*self.zoom))))
                setattr(self,f'pnj{i}Rect',getattr(self,f'pnj{i}Image').get_rect(topleft=CommonVar.savingDico['creaturePositions'][i]))
                if i == 0:
                    setattr(self,f'pnj{i}Name',nameFont.render("VOUS",True,(255,255,255)))
                else:
                    setattr(self,f'pnj{i}Name',nameFont.render(CommonVar.savingDico['creatureId'][i],True,(255,255,255)))
                setattr(self,f'pnj{i}NameRect',getattr(self,f'pnj{i}Name').get_rect(center=(CommonVar.savingDico['creaturePositions'][i][0],CommonVar.savingDico['creaturePositions'][i][1] - self.converter.conv_y(30))))

        positions = CommonVar.savingDico['creaturePositions']
        ordre = [i for i in range(len(positions))]
        self.ordreAffichage = self.percepective(positions,ordre)
        
    def display(self):
        self.screen.blit(self.bgSurface,(0,0))
        tempBgRect = (self.bgRect[0],self.bgRect[1])
        self.bgSurface.blit(self.bgNuitImage,tempBgRect)
        self.bgSurface.blit(self.bgImage,tempBgRect)

        if self.selectionRectShow:
            pygame.draw.rect(self.screen,self.selectionRectColor,self.selectionRect)

        if self.selectionSelectedRectShow:
            pygame.draw.rect(self.screen,self.selectionSelectedRectColor,self.selectionSelectedRect)
            pygame.draw.rect(self.screen,self.selectionConfirmationButtonColor,self.selectionConfirmationButtonRect,border_radius=20)
            self.screen.blit(self.selectionConfirmationButtonText,self.selectionConfirmationButtonTextRect)

        for i in self.ordreAffichage:
            if CommonVar.savingDico['creatureTentState'][i]:
                pnjRect = getattr(self,f'pnj{i}Rect')
                nameRect = getattr(self,f'pnj{i}NameRect')
                self.screen.blit(getattr(self,f'pnj{i}Image'),(pnjRect[0]*self.zoom+self.bgRect[0],pnjRect[1]*self.zoom+self.bgRect[1],pnjRect[2],pnjRect[3]))
                self.screen.blit(getattr(self,f'pnj{i}Name'),(nameRect[0]*self.zoom+self.bgRect[0]+self.converter.conv_x(50)*self.zoom,nameRect[1]*self.zoom+self.bgRect[1]+self.converter.conv_y(20)*self.zoom,nameRect[2],nameRect[3]))

        self.screen.blit(self.voteSurface,(self.screen.get_width()/2 - self.voteSurface.get_width()/2,self.converter.conv_x(50)))
        self.voteTextText.set_alpha(self.voteAlpha)
        pygame.draw.rect(self.voteSurface,(37,48,45,self.voteAlpha),self.voteRect,border_radius=38)
        self.voteSurface.blit(self.voteTextText,self.voteTextRect)

        ## Affichage du fondu enchainé (calque noir)
        self.screen.blit(self.transitionBgSurface,(0,0))
        self.transitionBgSurface.fill(self.fadeColor)

        pygame.display.flip()

    def run(self,window):

        print((self.running,window.game.running))

        while self.running and window.game.running:
            self.handling_event(window)
            self.update()
            self.display()

        print('on est bien ici')

        self.zoom = 1
        self.selectionRectShow = False
        self.selectionSelectedRectShow = False
        self.selectedId = None
        self.toKill = None
        self.votePossibility = True
        self.bgImage.set_alpha(self.bgImage.get_alpha() + 10)

        self.voteText = 'votez pour la personne à éliminer'
        self.voteRect = pygame.Rect(0,0,len(self.voteText)*self.converter.conv_x(29),self.converter.conv_y(80))
        self.voteSurface = pygame.Surface((len(self.voteText)*self.converter.conv_x(29),self.converter.conv_y(80)),pygame.SRCALPHA)
        self.voteAlpha = 0
        self.voteTextText = self.voteTextFont.render(self.voteText,True,(255,255,255))
        self.voteTextRect = self.voteTextText.get_rect(topleft=(self.converter.conv_x(10),0))
        self.display()
        self.bgImage.set_alpha(0)
        CommonVar.savingDico['creaturePositions'] = [self.tentPositions[CommonVar.savingDico['creatureTent'][u]] for u in range(CommonVar.savingDico['creatureNumber'])]
        for i in range(CommonVar.savingDico['creatureNumber']):
            h = 150
            l = 200
            destinationX = self.screen.get_width()/2 + math.sin((i*2*math.pi)/CommonVar.savingDico['creatureNumber']) * l - self.converter.conv_x(16)
            destinationY = self.screen.get_height()/2 + math.cos((i*2*math.pi)/CommonVar.savingDico['creatureNumber']) * h - self.converter.conv_y(16)
            CommonVar.savingDico['creatureDestinations'][i] = [destinationX,destinationY]
            currentX = CommonVar.savingDico['creaturePositions'][i][0]
            currentY = CommonVar.savingDico['creaturePositions'][i][1]

            ## DAMN ON A UTILISE LE THEOREME DE PYTHAGORE EN PYTHON
            distance = math.sqrt((destinationX-currentX)**2 + (destinationY-currentY)**2)

            sensX = 16*(destinationX-currentX)/distance
            sensY = 16*(destinationY-currentY)/distance
            sens = [sensX,sensY]
            CommonVar.savingDico['creatureSens'][i] = sens
        pygame.display.set_caption("Nox Villae [En jeu]")

    def sortab(self,tab):
        return sorted(tab, key=lambda x: x[1], reverse=True)

    def percepective(self,ref,tab):
        temp = self.sortab(ref)
        final = []

        for i in range(len(temp)):
            final.append(tab[ref.index(temp[-i])])

        return final
    
    def kill(self,selectedId):
        CommonVar.savingDico['creatureTentState'][selectedId] = False