import pygame
import math

import Font
import SpriteBank
import Choose
import CommonVar
from CommonVar import directory
from Converter import Converter
from Keybinds import keybinds
from CommonFonction import hover

class NightAction :
    def __init__(self,screen):
        self.screen = screen
        self.running = False
        self.werewolfRunning = False
        self.clock = pygame.time.Clock()

        self.confirmed = pygame.USEREVENT + 3

        self.autoChoosing = True

        self.role = CommonVar.savingDico['creatureRoles'][0]

        self.commonVar = CommonVar.CommonVar()
        self.converter = Converter(self.screen)

        self.transitionAlpha = 255
        self.transitionBgSurface = pygame.Surface(self.screen.get_size(),pygame.SRCALPHA)

        self.bgNuitImage = SpriteBank.fondMap['Nuit']
        self.bgNuitImage = pygame.transform.scale(self.bgNuitImage,(self.screen.get_width(),self.screen.get_height()))
        self.bgRect = self.screen.get_rect()

        self.tentPositions = [(self.converter.conv_x(200*u) + self.converter.conv_x(50),self.converter.conv_y(100*i)) for i in range(1,10) for u in range(0,2)] + [(self.screen.get_width() - (self.converter.conv_x(200)*u + self.converter.conv_x(178)),self.converter.conv_y(100)*i) for i in range(1,10) for u in range(0,2)]
        self.tentImage = SpriteBank.tente['Jour']['Droite']
        self.tentReverseImage = SpriteBank.tente['Jour']['Gauche']
        self.destroyedTentImage = SpriteBank.tente['Jour']['Détruite']
        self.tentImage = pygame.transform.scale(self.tentImage,(self.converter.conv_x(362*0.5),self.converter.conv_y(260*0.5)))
        self.destroyedTentImage = pygame.transform.scale(self.destroyedTentImage,(self.converter.conv_x(200*0.75),self.converter.conv_y(95*0.75)))
        self.tentReverseImage = pygame.transform.scale(self.tentImage,(self.converter.conv_x(362*0.5),self.converter.conv_y(260*0.5)))
        self.tentNameFont = pygame.font.Font(Font.jaini,self.converter.conv_y(30))
        self.tentNameText = self.tentNameFont.render('nom',True,(255,255,255))
        self.tentNameRect = self.tentNameText.get_rect()

        self.tentWerewolfVoteNumber = 0
        self.tentWerewolfVoteNumberFont = pygame.font.Font(Font.jaini,self.converter.conv_y(100))
        self.tentWerewolfVoteNumberText = self.tentWerewolfVoteNumberFont.render("0",True,(255,255,255))
        self.tentWerewolfVoteNumberTextRect = self.tentWerewolfVoteNumberText.get_rect(center=(0,0))


        self.title = 'Votez pour la personne à dévorer'
        self.titleFont = pygame.font.Font(Font.IMfell,self.converter.conv_y(60))
        self.titleText = self.titleFont.render(self.title,True,(255,255,255))
        self.titleTextRect = self.titleText.get_rect(center=(self.screen.get_width()/2,self.converter.conv_y(100)))
        self.titleRect = pygame.Rect(self.screen.get_width()/2 - len(self.title)*self.converter.conv_x(30)/2,self.converter.conv_y(60),len(self.title)*self.converter.conv_x(30),self.converter.conv_y(80))

        self.maxSelection = 2
        self.selectedHover = False
        self.selectedHoverSurface = pygame.Surface((self.converter.conv_x(362*0.5),self.converter.conv_y(300*0.5)),pygame.SRCALPHA)
        self.selectedHoverPosition = (0,0)
        self.selectedConfirmSurface = pygame.Surface((self.converter.conv_x(362*0.5),self.converter.conv_y(300*0.5)),pygame.SRCALPHA)
        self.selectedConfirm = [False for _ in range(self.maxSelection)]
        self.selectedConfirmPosition = [(0,0) for _ in range(self.maxSelection)]

        self.confirmButtonFont = pygame.font.Font(Font.jaini,self.converter.conv_y(60))
        self.confirmButtonText = self.confirmButtonFont.render("Confirmer",True,(255,255,255))
        self.confirmButtonTextRect = self.confirmButtonText.get_rect(center=(self.screen.get_width()/2,self.screen.get_height()/2))
        self.confirmButtonRect = pygame.Rect(self.screen.get_width()/2 - self.converter.conv_x(110),self.screen.get_height()/2 - self.converter.conv_y(30),self.converter.conv_x(220),self.converter.conv_y(60))
        self.confirmButtonRectColor = (0,170,0)

    def handling_event(self,window):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: ##Si le joueur appuie sur la croix de la fenetre
                self.commonVar.update_saving_json()
                self.commonVar.update_common_json()
                pygame.quit() ##Le jeu s'arrete
            
            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN and keys[keybinds['openMenu']]:
                self.fade_to_menus(window)

            survol = False

            # Cases (tentes)
            self.selectedHover = False
            for i in range(len(CommonVar.savingDico['creatureTent'])):
                if CommonVar.savingDico['creatureTentState'][i]:
                    temp = pygame.Rect(self.tentPositions[CommonVar.savingDico['creatureTent'][i]][0],self.tentPositions[CommonVar.savingDico['creatureTent'][i]][1],self.converter.conv_x(373*0.5),self.converter.conv_y(270*0.5))
                    if hover(event,temp)[0]:
                        if i!=0 or self.autoChoosing:
                            survol = True
                            self.selectedHover = True
                            self.selectedHoverPosition = self.tentPositions[CommonVar.savingDico['creatureTent'][i]]
                            
                            if CommonVar.savingDico['creatureRoles'][0] == "Loup-garou":
                                self.tentWerewolfVoteNumber = self.werewolfChoose[i]
                                if i == 0:
                                    self.tentNameText = self.tentNameFont.render("VOUS",True,(255,100,100))
                                elif CommonVar.savingDico['creatureRoles'][i] == "Loup-garou" and self.werewolfRunning:
                                    self.tentNameText = self.tentNameFont.render(CommonVar.savingDico['creatureId'][i] + " (Loup)",True,(255,100,100))
                                else:
                                    self.tentNameText = self.tentNameFont.render(CommonVar.savingDico['creatureId'][i],True,(255,255,255))
                            else:
                                if i == 0:
                                    self.tentNameText = self.tentNameFont.render("VOUS",True,(255,255,255))
                                else:
                                    self.tentNameText = self.tentNameFont.render(CommonVar.savingDico['creatureId'][i],True,(255,255,255))
                            self.tentNameRect = self.tentNameText.get_rect(center = (temp[0] + self.converter.conv_x(362*0.4/2),temp[1] - self.converter.conv_y(40)))
                            self.tentWerewolfVoteNumberText = self.tentWerewolfVoteNumberFont.render(str(self.tentWerewolfVoteNumber),True,(255,255,255))
                            self.tentWerewolfVoteNumberTextRect = self.tentWerewolfVoteNumberText.get_rect(center=(temp[0] + self.converter.conv_x(373*0.25),temp[1] + self.converter.conv_y(270*0.25)))
                            if hover(event,temp)[1]:
                                if self.selectedHoverPosition in self.selectedConfirmPosition:
                                    index = self.selectedConfirmPosition.index(self.selectedHoverPosition)
                                    self.selectedConfirm[index] = not self.selectedConfirm[index]
                                else:
                                    index = 0
                                    while self.selectedConfirm[index] == True:
                                        if len(self.selectedConfirm) == index+1:
                                            index = 0
                                            break
                                        index += 1
                                            
                                    self.selectedConfirmPosition[index] = self.selectedHoverPosition
                                    self.selectedConfirm[index] = True

            # Bouton confirmer
            if hover(event,self.confirmButtonRect)[0] and all(self.selectedConfirm):
                self.confirmButtonRectColor = (0,170,0)
                survol = True
                if hover(event,self.confirmButtonRect)[1]:
                    if self.werewolfRunning :
                        self.werewolfRunning = False
                        pygame.time.set_timer(self.confirmed,2000)
                    else:
                        self.running = False
            else:
                self.confirmButtonRectColor = (0,91,0)

            if event.type == self.confirmed:
                self.running = False

            if survol :
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def update(self):
        self.transitionAlpha = 0

        if len(self.selectedConfirm) != self.maxSelection:
            self.selectedConfirm = [False for _ in range(self.maxSelection)]
            self.selectedConfirmPosition = [(0,0) for _ in range(self.maxSelection)]

    def display(self):
        self.screen.blit(self.bgNuitImage,self.bgRect)

        for i in range(len(CommonVar.savingDico['creatureTent'])):
            if CommonVar.savingDico['creatureTentState'][i]:
                if self.tentPositions[CommonVar.savingDico['creatureTent'][i]][0] > self.screen.get_width()/2:
                    self.screen.blit(self.tentImage,(self.tentPositions[CommonVar.savingDico['creatureTent'][i]][0],self.tentPositions[CommonVar.savingDico['creatureTent'][i]][1],self.converter.conv_x(362*0.5),self.converter.conv_y(260*0.5)))
                else:
                    self.screen.blit(self.tentReverseImage,(self.tentPositions[CommonVar.savingDico['creatureTent'][i]][0],self.tentPositions[CommonVar.savingDico['creatureTent'][i]][1],self.converter.conv_x(362*0.5),self.converter.conv_y(260*0.5)))
            else:
                self.screen.blit(self.destroyedTentImage,(self.tentPositions[CommonVar.savingDico['creatureTent'][i]][0],self.tentPositions[CommonVar.savingDico['creatureTent'][i]][1],self.converter.conv_x(362*0.5),self.converter.conv_y(260*0.5)))

        if self.selectedHover:
            tempHover = (self.selectedHoverPosition[0] - 10,self.selectedHoverPosition[1] - 10)
            self.screen.blit(self.selectedHoverSurface,tempHover)
            pygame.draw.rect(self.selectedHoverSurface,(48,175,255),(0,0,self.converter.conv_x(362*0.5),self.converter.conv_y(300*0.5)),width=10)
            self.screen.blit(self.tentNameText,self.tentNameRect)
            self.screen.blit(self.tentWerewolfVoteNumberText,self.tentWerewolfVoteNumberTextRect)

        for i in range(len(self.selectedConfirm)):
            if self.selectedConfirm[i]:
                tempConfirm = (self.selectedConfirmPosition[i][0] - 10,self.selectedConfirmPosition[i][1] - 10)
                self.screen.blit(self.selectedConfirmSurface,tempConfirm)
                pygame.draw.rect(self.selectedConfirmSurface,(48,198,48),(0,0,self.converter.conv_x(362*0.5),self.converter.conv_y(300*0.5)),width=10)

        pygame.draw.rect(self.screen,(37,48,45),self.titleRect,border_radius=20)
        self.screen.blit(self.titleText,self.titleTextRect)

        if all(self.selectedConfirm): ## Vérifie toutes les conditions dans la liste (and)
            pygame.draw.rect(self.screen,self.confirmButtonRectColor,self.confirmButtonRect,border_radius=15)
            self.screen.blit(self.confirmButtonText,self.confirmButtonTextRect)

        ## Affichage du fondu enchainé (calque noir)
        self.screen.blit(self.transitionBgSurface,(0,0))
        self.transitionBgSurface.fill((0,0,0,self.transitionAlpha))

    def run(self,window):
        if self.running:
            self.handling_event(window)
            self.update()
            self.display()

    def werewolf_init(self):
        self.werewolfRunning = True

        self.werewolfChoose = [0 for i in range(CommonVar.savingDico['creatureNumber'])]
        for i in range(CommonVar.savingDico['creatureNumber']):
            if CommonVar.savingDico['creatureTentState'][i] and i != 0 and CommonVar.savingDico['creatureRoles'][i] == "Loup-garou":
                botChoose = Choose.bad('Loup',i)
                try:
                    while not CommonVar.savingDico['creatureTentState'][botChoose]:
                        botChoose = Choose.bad('Loup',i)
                except IndexError:
                    botChoose = Choose.bad('Loup',i)
                self.werewolfChoose[botChoose] += 1

        self.werewolfDict = dict() # dict[idCreature] = idLoup

        self.werewolfPositions = []
        self.werewolfSens = []
        self.werewolfDestination = []
        self.werewolfImage = []

        try:
            whiteWolfAlive = 1 if CommonVar.savingDico['creatureTentState'] [CommonVar.savingDico['creatureRoles'].index("Loup Blanc")] else 0
        except ValueError:
            whiteWolfAlive = 0

        wereWolfAlive = 0
        for i in range(CommonVar.savingDico['creatureNumber']):
            if CommonVar.savingDico['creatureRoles'][i] == "Loup-garou" and CommonVar.savingDico['creatureTentState'][i]:
                wereWolfAlive += 1

        self.werewolfNumber = wereWolfAlive + whiteWolfAlive
        
        self.frame = 1

        for i in range(CommonVar.savingDico['creatureNumber']):
            if CommonVar.savingDico['creatureRoles'][i]:
                if CommonVar.savingDico['creatureRoles'][i][:4] == "Loup" and CommonVar.savingDico['creatureTentState'][i]:
                    self.werewolfDict[i] = len(self.werewolfPositions)
                    image = SpriteBank.loup ["Static"] ["Arriere"] [0]  # Un loup static qui regarde vers l'arriere à la frame 1
                    self.werewolfImage.append(pygame.transform.scale(image,(self.converter.conv_x(640*0.35),self.converter.conv_y(480*0.35))))

                    h = 150
                    l = 200
                    destinationX = self.screen.get_width()/2 + math.sin((len(self.werewolfPositions)*2*math.pi)/self.werewolfNumber) * l - self.converter.conv_x(100)
                    destinationY = self.screen.get_height()/2 + math.cos((len(self.werewolfPositions)*2*math.pi)/self.werewolfNumber) * h - self.converter.conv_y(60)
                    self.werewolfDestination.append([destinationX,destinationY])

                    currentX = self.tentPositions[CommonVar.savingDico['creatureTent'][i]][0] - self.converter.conv_x(60)
                    currentY = self.tentPositions[CommonVar.savingDico['creatureTent'][i]][1] - self.converter.conv_y(20)
                    self.werewolfPositions.append([currentX,currentY])

                    ## DAMN ON A UTILISE LE THEOREME DE PYTHAGORE EN PYTHON
                    distance = math.sqrt((destinationX-currentX)**2 + (destinationY-currentY)**2)

                    sensX = 16*(destinationX-currentX)/distance
                    sensY = 16*(destinationY-currentY)/distance
                    sens = [sensX,sensY]
                    self.werewolfSens.append(sens)

    def werewolf_update(self):
                if (pygame.time.get_ticks())%100 <= 20:
                    if self.frame < 4:
                        self.frame += 1
                    else:
                        self.frame = 1

                for i in range(self.werewolfNumber):
                    if self.werewolfDestination[i] != None:
                        if not self.werewolfDestination[i]:
                            running = False
                        else:
                            running = True
                            position = self.werewolfPositions[i]
                            destination = self.werewolfDestination[i]
                            sens = self.werewolfSens[i]
                            if (destination[0] > position[0] and sens[0] < 0) or (destination[0] < position[0] and sens[0] > 0) or (destination[1] > position[1] and sens[1] < 0) or (destination[1] < position[1] and sens[1] > 0):
                                self.werewolfDestination[i] = None
                            else:
                                currentX = position[0]+sens[0]
                                currentY = position[1]+sens[1]
                                position = [currentX,currentY]
                                self.werewolfPositions[i] = position

                        direction = "Avant"

                        if self.werewolfSens[i][0] > 0:
                            if self.werewolfSens[i][1] > 0:
                                if self.werewolfSens[i][0] > self.werewolfSens[i][1]:
                                    direction = "Droite"
                                else:
                                    direction = "Arriere"
                            else:
                                if self.werewolfSens[i][0] > -self.werewolfSens[i][1]:
                                    direction = "Droite"
                                else:
                                    direction = "Avant"
                        else:
                            if self.werewolfSens[i][1] > 0:
                                if -self.werewolfSens[i][0] > self.werewolfSens[i][1]:
                                    direction = "Gauche"
                                else:
                                    direction = "Arriere"
                            else:
                                if -self.werewolfSens[i][0] > -self.werewolfSens[i][1]:
                                    direction = "Gauche"
                                else:
                                    direction = "Avant"

                        if running:
                            spriteStep2 = "Run" # Mouvement
                            spriteStep4 = self.frame-1 # Frame
                        else:
                            spriteStep2 = "Static" # Mouvement
                            spriteStep4 = self.frame%2 # Frame

                        image = SpriteBank.loup [spriteStep2] [direction] [spriteStep4]
                        self.werewolfImage[i] = pygame.transform.scale(image,(self.converter.conv_x(640*0.35),self.converter.conv_y(480*0.35)))

                    else:
                        x = math.sin((i*2*math.pi)/self.werewolfNumber)
                        y = math.cos((i*2*math.pi)/self.werewolfNumber)
                        if x >= 0:
                            if y >= 0:
                                if x > y:
                                    direction = "Gauche"
                                else:
                                    direction = "Avant"
                            else:
                                if x > -y:
                                    direction = "Gauche"
                                else:
                                    direction = "Arriere"
                        else:
                            if y >= 0:
                                if -x > y:
                                    direction = "Droite"
                                else:
                                    direction = "Avant"
                            else:
                                if -x > -y:
                                    direction = "Droite"
                                else:
                                    direction = "Arriere"
                                    
                        image = SpriteBank.loup ["Static"] [direction] [self.frame%2]
                        self.werewolfImage[i] = pygame.transform.scale(image,(self.converter.conv_x(640*0.35),self.converter.conv_y(480*0.35)))

    def werewolf_goto(self,destination):
        destination = [self.tentPositions[destination][0] + self.converter.conv_x(362*0.5),self.tentPositions[destination][1] + self.converter.conv_x(362*0.5)]
        self.selectedConfirmPosition[0] = [destination[0] + self.converter.conv_x(69),destination[1] + self.converter.conv_y(69)]

        for i in range(CommonVar.savingDico['creatureNumber']):
            if CommonVar.savingDico['creatureRoles'][i]:
                if CommonVar.savingDico['creatureRoles'][i][:3] == "Loup" and CommonVar.savingDico['creatureTentState'][i]:
                    destinationX = destination[0]
                    destinationY = destination[1]
                    self.werewolfDestination[self.werewolfDict[i]] = [destinationX,destinationY]

                    currentX = self.werewolfPositions[i][0]
                    currentY = self.werewolfPositions[i][1]

                    ## DAMN ON A UTILISE LE THEOREME DE PYTHAGORE EN PYTHON
                    distance = math.sqrt((destinationX-currentX)**2 + (destinationY-currentY)**2)

                    sensX = 16*(destinationX-currentX)/distance
                    sensY = 16*(destinationY-currentY)/distance
                    sens = [sensX,sensY]
                    self.werewolfSens[i] = sens

    def werewolf_display(self):
        for i in range(self.werewolfNumber):
            self.screen.blit(self.werewolfImage[i],self.werewolfPositions[i])
        pygame.display.flip()

    def werewolf_run(self):
        if self.running:
            self.werewolf_update()
            self.werewolf_display()

    def fade_out(self):
        self.running = True
        self.transitionAlpha = 255
        while self.transitionAlpha > 1  :
            self.display()
            self.transitionAlpha -= 25.5
        self.transitionAlpha = 0
        self.display()

    def fade_to_menus(self,window):
        while self.transitionAlpha < 255:
            self.display()
            self.transitionAlpha += 25.5
        window.game.running = False
        window.menus.fade_out()
        window.menus.start_threading()