import pygame

from Converter import Converter
from Keybinds import keybinds
from CommonVar import directory
from CommonVar import CommonVar
from CommonFonction import hover
import Font
import SpriteBank

class FloatingMenu:
    def __init__ (self,screen):
        self.screen = screen
        self.running = False
        self.clock = pygame.time.Clock()

        self.converter = Converter(self.screen)
        self.commonVar = CommonVar()

        self.pos = ()

        width = self.converter.conv_x(205)
        height = self.converter.conv_y(32)
        menusFont = pygame.font.Font(Font.jaini,self.converter.conv_y(25))
        nameFont = pygame.font.Font(Font.inter,self.converter.conv_y(20))
        buttonFont = pygame.font.Font(Font.jaini,self.converter.conv_y(18))
        
        self.NextButtonImage = SpriteBank.logo['Prochain']
        self.PrecButtonImage = SpriteBank.logo['Precedent']

        # Menu de demandes d'aide
        self.helpWantedOpened = False
        self.helpWantedRect = pygame.Rect(0,0,width,height)
        self.helpWantedRectColor = (72,72,72)
        self.helpWantedRectSPace = 0
        self.helpWantedText = menusFont.render("Demandes d'aide (3)",True,(255,255,255))
        self.helpWantedTextRect = self.helpWantedText.get_rect(center=(width/2-10,height/2))

        self.helpWantedEl1PdpImage = SpriteBank.iconePerso[0]
        pygame.transform.scale(self.helpWantedEl1PdpImage,(32,32))
        self.helpWantedEl1PdpRect = pygame.Rect(self.converter.conv_x(5),height + self.converter.conv_y(16),32,32)

        self.helpWantedEl1Name = nameFont.render("Charles Lecl...",True,(255,255,255))
        self.helpWantedEl1NameRect = self.helpWantedEl1Name.get_rect(topleft=(self.converter.conv_x(42),height + self.converter.conv_y(16)))

        self.helpWantedEl1TreeNumber = nameFont.render("4",True,(255,255,255))
        self.helpWantedEl1TreeNumberRect = self.helpWantedEl1TreeNumber.get_rect(topright=(width - self.converter.conv_x(10),height + self.converter.conv_y(16)))

        self.helpWantedEl1Trust = 150
        self.helpWantedEl1TrustBgRect = pygame.Rect(self.converter.conv_x(42),height + self.converter.conv_y(40),self.converter.conv_x(153),self.converter.conv_y(8))
        self.helpWantedEl1TrustRect = pygame.Rect(self.converter.conv_x(42),height + self.converter.conv_y(40),self.converter.conv_x((self.helpWantedEl1Trust/200)*153),self.converter.conv_y(8))
        self.helpWantedEl1TrustColor = (0,182,33)
        
        self.helpWantedEl1AcceptButtonBgRect = pygame.Rect(self.converter.conv_x(5),height + self.converter.conv_y(52),self.converter.conv_x(58),self.converter.conv_y(21))
        self.helpWantedEl1AcceptButtonBgColor = (0,89,19)
        self.helpWantedEl1AcceptButtonText = buttonFont.render('Accepter',True,(255,255,255))
        self.helpWantedEl1AcceptButtonTextRect = self.helpWantedEl1AcceptButtonText.get_rect(topleft=(self.converter.conv_x(5),height + self.converter.conv_y(50)))

        self.helpWantedEl1BetrayButtonBgRect = pygame.Rect(width/2 - self.converter.conv_x(33),height + self.converter.conv_y(52),self.converter.conv_x(66),self.converter.conv_y(21))
        self.helpWantedEl1BetrayButtonBgColor = (0,77,105)
        self.helpWantedEl1BetrayButtonText = buttonFont.render('Trahir (+3)',True,(255,255,255))
        self.helpWantedEl1BetrayButtonTextRect = self.helpWantedEl1BetrayButtonText.get_rect(topleft=(width/2 - self.converter.conv_x(33),height + self.converter.conv_y(50)))

        self.helpWantedEl1RefuseButtonBgRect = pygame.Rect(width - self.converter.conv_x(56),height + self.converter.conv_y(52),self.converter.conv_x(51),self.converter.conv_y(21))
        self.helpWantedEl1RefuseButtonBgColor = (120,11,11)
        self.helpWantedEl1RefuseButtonText = buttonFont.render('Refuser',True,(255,255,255))
        self.helpWantedEl1RefuseButtonTextRect = self.helpWantedEl1BetrayButtonText.get_rect(topleft=(width - self.converter.conv_x(56),height + self.converter.conv_y(50)))

        self.helpWantedEl1PageNumberText = buttonFont.render('2/3',True,(255,255,255))
        self.helpWantedEl1PageNumberTextRect = self.helpWantedEl1PageNumberText.get_rect(center=(width/2,height + self.converter.conv_y(88)))

        self.helpWantedEl1PageNextButtonRect = self.NextButtonImage.get_rect(topright=(width - self.converter.conv_x(5),height + self.converter.conv_y(80)))
        self.helpWantedEl1PagePrecButtonRect = self.PrecButtonImage.get_rect(topleft=(self.converter.conv_x(5),height + self.converter.conv_y(80)))
        
        
        # Menu de partage 
        long = self.helpWantedRectSPace
        self.shareTrustOpened = False
        self.shareTrustRect = pygame.Rect(0,height + long + 3,width,height)
        self.shareTrustRectColor = (72,72,72)
        self.shareTrustRectSpace = 0
        self.shareTrustText = menusFont.render("Partager sa confiance",True,(255,255,255))
        self.shareTrustTextRect = self.helpWantedText.get_rect(center=(width/2-10,3 + long + height + height/2))
        
        trustX = 0
        trustY1 = height*2 + self.converter.conv_x(5)
        self.shareTrustEl1TrustText = nameFont.render('Confiance de:',True,(255,255,255))
        self.shareTrustEl1TrustTextRect = self.shareTrustEl1TrustText.get_rect(topleft=(trustX + self.converter.conv_x(5),trustY1))

        self.shareTrustEl1NextButtonRect = self.NextButtonImage.get_rect(topright=(width - self.converter.conv_x(5),trustY1))
        self.shareTrustEl1PrecButtonRect = self.PrecButtonImage.get_rect(topright=(width - self.converter.conv_x(37),trustY1))

        self.shareTrustEl1PdpImage = SpriteBank.iconePerso[0]
        pygame.transform.scale(self.shareTrustEl1PdpImage,(32,32))
        self.shareTrustEl1PdpRect = pygame.Rect(self.converter.conv_x(5),trustY1 + self.converter.conv_y(25),32,32)

        self.shareTrustEl1NameText = nameFont.render('Charles Leclerc',True,(255,255,255))
        self.shareTrustEl1NameRect = self.shareTrustEl1NameText.get_rect(topleft=(self.converter.conv_x(42),trustY1 + self.converter.conv_y(25)))

        self.shareTrustEl1Trust = 150
        self.shareTrustEl1TrustBgRect = pygame.Rect(self.converter.conv_x(42),trustY1 + self.converter.conv_y(49),self.converter.conv_x(153),self.converter.conv_y(8))
        self.shareTrustEl1TrustRect = pygame.Rect(self.converter.conv_x(42),trustY1 + self.converter.conv_y(49),self.converter.conv_x((self.shareTrustEl1Trust/200)*153),self.converter.conv_y(8))
        self.shareTrustEl1TrustColor = (0,182,33)

        trustY2 = height*2 + self.converter.conv_x(75)
        self.shareTrustEl2ShareText = nameFont.render('Partagée à:',True,(255,255,255))
        self.shareTrustEl2ShareTextRect = self.shareTrustEl2ShareText.get_rect(topleft=(trustX + self.converter.conv_x(5),trustY2))

        self.shareTrustEl2NextButtonRect = self.NextButtonImage.get_rect(topright=(width - self.converter.conv_x(5),trustY2))
        self.shareTrustEl2PrecButtonRect = self.PrecButtonImage.get_rect(topright=(width - self.converter.conv_x(37),trustY2))

        self.shareTrustEl2PdpImage = SpriteBank.iconePerso[0]
        pygame.transform.scale(self.shareTrustEl2PdpImage,(32,32))
        self.shareTrustEl2PdpRect = pygame.Rect(self.converter.conv_x(5),trustY2 + self.converter.conv_y(25),32,32)

        self.shareTrustEl2NameText = nameFont.render('Charles Leclerc',True,(255,255,255))
        self.shareTrustEl2NameRect = self.shareTrustEl2NameText.get_rect(topleft=(self.converter.conv_x(42),trustY2 + self.converter.conv_y(25)))

        self.shareTrustEl2Trust = 150
        self.shareTrustEl2TrustBgRect = pygame.Rect(self.converter.conv_x(42),trustY2 + self.converter.conv_y(49),self.converter.conv_x(153),self.converter.conv_y(8))
        self.shareTrustEl2TrustRect = pygame.Rect(self.converter.conv_x(42),trustY2 + self.converter.conv_y(49),self.converter.conv_x((self.shareTrustEl2Trust/200)*153),self.converter.conv_y(8))
        self.shareTrustEl2TrustColor = (0,182,33)

        self.shareTrustEl3ConfirmButtonText = buttonFont.render('Confirmer',True,(255,255,255))
        self.shareTrustEl3ConfirmButtonTextRect = self.shareTrustEl3ConfirmButtonText.get_rect(center=(width/2,trustY1 + self.converter.conv_y(145)))
        self.shareTrustEl3ConfirmButtonColor = (0,89,19)
        self.shareTrustEl3ConfirmButtonRect = pygame.Rect(self.converter.conv_x(5),trustY1 + self.converter.conv_y(134),width - self.converter.conv_x(10),self.converter.conv_y(22))


        # Menu d'attaque
        long += self.shareTrustRectSpace
        self.attackOpened = False
        self.attackRect = pygame.Rect(0,height*2 + long + 6,width,height)
        self.attackRectColor = (72,72,72)
        self.attackRectSpace = 0
        self.attackText = menusFont.render("Attaquer",True,(255,255,255))
        self.attackTextRect = self.helpWantedText.get_rect(center=(width/2-10,6 + long + height*2 + height/2))
        
        attackY = height*3 + self.converter.conv_x(10)
        self.attackEl1PageText = buttonFont.render('2/3',True,(255,255,255))
        self.attackEl1PageTextRect = self.attackEl1PageText.get_rect(center=(width/2,attackY+10))

        self.attackEl1NextButtonRect = self.NextButtonImage.get_rect(topright=(width - self.converter.conv_x(5),attackY))
        self.attackEl1PrecButtonRect = self.PrecButtonImage.get_rect(topleft=(self.converter.conv_x(5),attackY))

        self.attackEl1PdpImage = SpriteBank.iconePerso[0]
        pygame.transform.scale(self.attackEl1PdpImage,(32,32))
        self.attackEl1PdpRect = pygame.Rect(self.converter.conv_x(5),attackY + self.converter.conv_y(30),32,32)

        self.attackEl1NameText = nameFont.render('Charles Leclerc',True,(255,255,255))
        self.attackEl1NameRect = self.attackEl1NameText.get_rect(topleft=(self.converter.conv_x(42),attackY + self.converter.conv_y(25)))

        self.attackEl1Trust = 150
        self.attackEl1TrustBgRect = pygame.Rect(self.converter.conv_x(42),attackY + self.converter.conv_y(54),self.converter.conv_x(153),self.converter.conv_y(8))
        self.attackEl1TrustRect = pygame.Rect(self.converter.conv_x(42),attackY + self.converter.conv_y(54),self.converter.conv_x((self.attackEl1Trust/200)*153),self.converter.conv_y(8))
        self.attackEl1TrustColor = (0,182,33)

        self.attackEl2ConfirmButtonText = buttonFont.render('Confirmer',True,(255,255,255))
        self.attackEl2ConfirmButtonTextRect = self.shareTrustEl3ConfirmButtonText.get_rect(center=(width/2,attackY + self.converter.conv_y(75)))
        self.attackEl2ConfirmButtonColor = (0,89,19)
        self.attackEl2ConfirmButtonRect = pygame.Rect(self.converter.conv_x(5),attackY + self.converter.conv_y(66),width - self.converter.conv_x(10),self.converter.conv_y(22))


        #Menu d'accusation
        long += self.attackRectSpace
        self.accuseOpened = False
        self.accuseRect = pygame.Rect(0,height*3 + long + 9,width,height)
        self.accuseRectColor = (72,72,72)
        self.accuseRectSpace = 0
        self.accuseText = menusFont.render("Accuser",True,(255,255,255))
        self.accuseTextRect = self.helpWantedText.get_rect(center=(width/2-10,9 + long + height*3 + height/2))

        accuseY = height*4 + self.converter.conv_x(15)
        self.accuseEl1PageText = buttonFont.render('2/3',True,(255,255,255))
        self.accuseEl1PageTextRect = self.accuseEl1PageText.get_rect(center=(width/2,accuseY+10))

        self.accuseEl1NextButtonRect = self.NextButtonImage.get_rect(topright=(width - self.converter.conv_x(5),accuseY))
        self.accuseEl1PrecButtonRect = self.PrecButtonImage.get_rect(topleft=(self.converter.conv_x(5),accuseY))

        self.accuseEl1PdpImage = SpriteBank.iconePerso[0]
        pygame.transform.scale(self.accuseEl1PdpImage,(32,32))
        self.accuseEl1PdpRect = pygame.Rect(self.converter.conv_x(5),accuseY + self.converter.conv_y(30),32,32)

        self.accuseEl1NameText = nameFont.render('Charles Leclerc',True,(255,255,255))
        self.accuseEl1NameRect = self.accuseEl1NameText.get_rect(topleft=(self.converter.conv_x(42),accuseY + self.converter.conv_y(25)))

        self.accuseEl1Trust = 150
        self.accuseEl1TrustBgRect = pygame.Rect(self.converter.conv_x(42),accuseY + self.converter.conv_y(54),self.converter.conv_x(153),self.converter.conv_y(8))
        self.accuseEl1TrustRect = pygame.Rect(self.converter.conv_x(42),accuseY + self.converter.conv_y(54),self.converter.conv_x((self.accuseEl1Trust/200)*153),self.converter.conv_y(8))
        self.accuseEl1TrustColor = (0,182,33)

        self.accuseEl2ConfirmButtonText = buttonFont.render('Confirmer',True,(255,255,255))
        self.accuseEl2ConfirmButtonTextRect = self.shareTrustEl3ConfirmButtonText.get_rect(center=(width/2,accuseY + self.converter.conv_y(75)))
        self.accuseEl2ConfirmButtonColor = (0,89,19)
        self.accuseEl2ConfirmButtonRect = pygame.Rect(self.converter.conv_x(5),accuseY + self.converter.conv_y(66),width - self.converter.conv_x(10),self.converter.conv_y(22))

        # Menus de de Sniffing Special Renard 
        long += self.attackRectSpace
        self.SniffingOpened = False
        self.SniffingRect = pygame.Rect(0,height*4 + long + 12,width,height)
        self.SniffingRectColor = (72,72,72)
        self.SniffingRectSpace = 0
        self.SniffingText = menusFont.render("Sniffing",True,(255,255,255))
        self.SniffingTextRect = self.helpWantedText.get_rect(center=(width/2-10,12 + long + height*4 + height/2))

        SniffingY = height*5 + self.converter.conv_x(20)
        self.SniffingEl1PageText = buttonFont.render('2/3',True,(255,255,255))
        self.SniffingEl1PageTextRect = self.SniffingEl1PageText.get_rect(center=(width/2,accuseY+10))

        self.SniffingEl1NextButtonRect = self.NextButtonImage.get_rect(topright=(width - self.converter.conv_x(5),SniffingY))
        self.SniffingEl1PrecButtonRect = self.PrecButtonImage.get_rect(topleft=(self.converter.conv_x(5),SniffingY))

        self.SniffingEl1PdpImage = SpriteBank.iconePerso[0]
        pygame.transform.scale(self.SniffingEl1PdpImage,(32,32))
        self.SniffingEl1PdpRect = pygame.Rect(self.converter.conv_x(5),SniffingY + self.converter.conv_y(30),32,32)

        self.SniffingEl1NameText = nameFont.render('Charles Leclerc',True,(255,255,255))
        self.SniffingEl1NameRect = self.SniffingEl1NameText.get_rect(topleft=(self.converter.conv_x(42),SniffingY + self.converter.conv_y(25)))

        self.SniffingEl1Trust = 150
        self.SniffingEl1TrustBgRect = pygame.Rect(self.converter.conv_x(42),SniffingY + self.converter.conv_y(54),self.converter.conv_x(153),self.converter.conv_y(8))
        self.SniffingEl1TrustRect = pygame.Rect(self.converter.conv_x(42),SniffingY + self.converter.conv_y(54),self.converter.conv_x((self.SniffingEl1Trust/200)*153),self.converter.conv_y(8))
        self.SniffingEl1TrustColor = (0,182,33)

        self.SniffingEl2ConfirmButtonText = buttonFont.render('Confirmer',True,(255,255,255))
        self.SniffingEl2ConfirmButtonTextRect = self.shareTrustEl3ConfirmButtonText.get_rect(center=(width/2,accuseY + self.converter.conv_y(75)))
        self.SniffingEl2ConfirmButtonColor = (0,89,19)
        self.SniffingEl2ConfirmButtonRect = pygame.Rect(self.converter.conv_x(5),SniffingY + self.converter.conv_y(66),width - self.converter.conv_x(10),self.converter.conv_y(22))

    
        # Fond
        self.generalRectHeight = self.converter.conv_y(137)
        self.generalSurface = pygame.Surface((width,self.generalRectHeight + 1000),pygame.SRCALPHA)
        self.generalRect = pygame.Rect(0,0,width,self.generalRectHeight)

    def opening(self):
        self.pos = pygame.mouse.get_pos()
        self.running = True

    def handling_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: ##Si le joueur appuie sur la croix de la fenetre
                self.commonVar.update_saving_json()   
                self.commonVar.update_common_json()
                pygame.quit() ##Le jeu s'arrete

            if not hover(event,self.generalSurface.get_rect(topleft=self.pos))[0]:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                self.pos = pygame.mouse.get_pos()

            keys = pygame.key.get_pressed()
            if keys[keybinds['openMenu']]:
                self.running = False

            survol = False

            tempHelpWantedRect = pygame.Rect(self.pos[0],self.pos[1],self.helpWantedRect[2],self.helpWantedRect[3])
            tempShareTrustRect = pygame.Rect(self.pos[0],self.pos[1]+self.shareTrustRect[1],self.shareTrustRect[2],self.shareTrustRect[3])
            tempAttackRect = pygame.Rect(self.pos[0],self.pos[1]+self.attackRect[1],self.attackRect[2],self.attackRect[3])
            tempAccuseRect = pygame.Rect(self.pos[0],self.pos[1]+self.accuseRect[1],self.accuseRect[2],self.accuseRect[3])
            tempSniffingRect = pygame.Rect(self.pos[0],self.pos[1]+self.SniffingRect[1],self.SniffingRect[2],self.SniffingRect[3])

            if hover(event,tempHelpWantedRect)[0]:
                self.helpWantedRectColor = (50,50,50)
                survol = True
                if hover(event,tempHelpWantedRect)[1]:
                    if not self.helpWantedOpened:
                        self.helpWantedOpened = True
                        self.shareTrustOpened = False
                        self.attackOpened = False
                        self.accuseOpened = False
                    else:
                        self.helpWantedOpened = False
            else:
                self.helpWantedRectColor = (71,71,71)
            
            if hover(event,tempShareTrustRect)[0]:
                self.shareTrustRectColor = (50,50,50)
                survol = True
                if hover(event,tempShareTrustRect)[1]:
                    if not self.shareTrustOpened:
                        self.helpWantedOpened = False
                        self.shareTrustOpened = True
                        self.attackOpened = False
                        self.accuseOpened = False
                    else:
                        self.shareTrustOpened = False
            else:
                self.shareTrustRectColor = (71,71,71)
            
            if hover(event,tempAttackRect)[0]:
                self.attackRectColor = (50,50,50)
                survol = True
                if hover(event,tempAttackRect)[1]:
                    if not self.attackOpened:
                        self.helpWantedOpened = False
                        self.shareTrustOpened = False
                        self.attackOpened = True
                        self.accuseOpened = False
                    else:
                        self.attackOpened = False
            else:
                self.attackRectColor = (71,71,71)
            
            if hover(event,tempAccuseRect)[0]:
                self.accuseRectColor = (50,50,50)
                survol = True
                if hover(event,tempAccuseRect)[1]:
                    if not self.accuseOpened:
                        self.helpWantedOpened = False
                        self.shareTrustOpened = False
                        self.attackOpened = False
                        self.accuseOpened = True
                        self.SniffingOpenend = False 
                    else:
                        self.accuseOpened = False
            else:
                self.accuseRectColor = (71,71,71)
                
            if hover(event,tempSniffingRect)[0]:
                self.SniffingRectColor = (50,50,50)
                survol = True
                if hover(event,tempSniffingRect)[1]:
                    if not self.SniffingOpened:
                        self.helpWantedOpened = False
                        self.shareTrustOpened = False
                        self.attackOpened = False
                        self.accuseOpened = False
                        self.SniffingOpenend = True 
                    else:
                        self.SniffingOpened = False
            else:
                self.SniffingRectColor = (71,71,71)

            # EVENEMENTS DU MENU DEMANDES D'AIDE
            if self.helpWantedOpened:
                tempAccept = pygame.Rect(self.helpWantedEl1AcceptButtonBgRect[0] + self.pos[0],self.helpWantedEl1AcceptButtonBgRect[1] + self.pos[1],self.helpWantedEl1AcceptButtonBgRect[2],self.helpWantedEl1AcceptButtonBgRect[3])
                tempBetray = pygame.Rect(self.helpWantedEl1BetrayButtonBgRect[0] + self.pos[0],self.helpWantedEl1BetrayButtonBgRect[1] + self.pos[1],self.helpWantedEl1BetrayButtonBgRect[2],self.helpWantedEl1BetrayButtonBgRect[3])
                tempRefuse = pygame.Rect(self.helpWantedEl1RefuseButtonBgRect[0] + self.pos[0],self.helpWantedEl1RefuseButtonBgRect[1] + self.pos[1],self.helpWantedEl1RefuseButtonBgRect[2],self.helpWantedEl1RefuseButtonBgRect[3])
                
                if hover(event,tempAccept)[0]:
                    self.helpWantedEl1AcceptButtonBgColor = (59,158,80)
                    survol = True
                    if hover(event,tempAccept)[1]:
                        self.help_wanted_accepted()
                else:
                    self.helpWantedEl1AcceptButtonBgColor = (0,89,19)

                if hover(event,tempBetray)[0]:
                    self.helpWantedEl1BetrayButtonBgColor = (18,147,193)
                    survol = True
                    if hover(event,tempBetray)[1]:
                        self.help_wanted_betrayed()
                else:
                    self.helpWantedEl1BetrayButtonBgColor = (0,77,105)
                    
                if hover(event,tempRefuse)[0]:
                    self.helpWantedEl1RefuseButtonBgColor = (214,42,42)
                    survol = True
                    if hover(event,tempRefuse)[1]:
                        self.help_wanted_refused()
                else:
                    self.helpWantedEl1RefuseButtonBgColor = (120,11,11)

                tempNext = pygame.Rect(self.helpWantedEl1PageNextButtonRect[0]+self.pos[0],self.helpWantedEl1PageNextButtonRect[1]+self.pos[1],self.helpWantedEl1PageNextButtonRect[2],self.helpWantedEl1PageNextButtonRect[3])
                tempPrec = pygame.Rect(self.helpWantedEl1PagePrecButtonRect[0]+self.pos[0],self.helpWantedEl1PagePrecButtonRect[1]+self.pos[1],self.helpWantedEl1PagePrecButtonRect[2],self.helpWantedEl1PagePrecButtonRect[3])

                if hover(event,tempNext)[0] or hover(event,tempPrec)[0]:
                    survol = True

            #EVENEMENTS DU MENU PARTAGER SA CONFIANCE
            if self.shareTrustOpened:
                tempNext1 = pygame.Rect(self.shareTrustEl1NextButtonRect[0]+self.pos[0],self.shareTrustEl1NextButtonRect[1]+self.pos[1],self.shareTrustEl1NextButtonRect[2],self.shareTrustEl1NextButtonRect[3])
                tempPrec1 = pygame.Rect(self.shareTrustEl1PrecButtonRect[0]+self.pos[0],self.shareTrustEl1PrecButtonRect[1]+self.pos[1],self.shareTrustEl1PrecButtonRect[2],self.shareTrustEl1PrecButtonRect[3])

                tempNext2 = pygame.Rect(self.shareTrustEl2NextButtonRect[0]+self.pos[0],self.shareTrustEl2NextButtonRect[1]+self.pos[1],self.shareTrustEl2NextButtonRect[2],self.shareTrustEl2NextButtonRect[3])
                tempPrec2 = pygame.Rect(self.shareTrustEl2PrecButtonRect[0]+self.pos[0],self.shareTrustEl2PrecButtonRect[1]+self.pos[1],self.shareTrustEl2PrecButtonRect[2],self.shareTrustEl2PrecButtonRect[3])

                if hover(event,tempNext1)[0] or hover(event,tempPrec1)[0] or hover(event,tempNext2)[0] or hover(event,tempPrec2)[0]:
                    survol = True
                    
                
                tempConfirmButton = pygame.Rect(self.shareTrustEl3ConfirmButtonRect[0]+self.pos[0],self.shareTrustEl3ConfirmButtonRect[1]+self.pos[1],self.shareTrustEl3ConfirmButtonRect[2],self.shareTrustEl3ConfirmButtonRect[3])

                if hover(event,tempConfirmButton)[0]:
                    self.shareTrustEl3ConfirmButtonColor = (59,158,80)
                    survol = True
                    if hover(event,tempConfirmButton)[1]:
                        self.share_trust_confirm()
                else:
                    self.shareTrustEl3ConfirmButtonColor = (0,89,19)

            #EVENEMENTS DU MENU ATTAQUER
            if self.attackOpened:
                tempNext = pygame.Rect(self.attackEl1NextButtonRect[0]+self.pos[0],self.attackEl1NextButtonRect[1]+self.pos[1],self.attackEl1NextButtonRect[2],self.attackEl1NextButtonRect[3])
                tempPrec = pygame.Rect(self.attackEl1PrecButtonRect[0]+self.pos[0],self.attackEl1PrecButtonRect[1]+self.pos[1],self.attackEl1PrecButtonRect[2],self.attackEl1PrecButtonRect[3])

                if hover(event,tempNext)[0] or hover(event,tempPrec)[0]:
                    survol = True
                
                tempConfirmButton = pygame.Rect(self.attackEl2ConfirmButtonRect[0]+self.pos[0],self.attackEl2ConfirmButtonRect[1]+self.pos[1],self.attackEl2ConfirmButtonRect[2],self.attackEl2ConfirmButtonRect[3])

                if hover(event,tempConfirmButton)[0]:
                    self.attackEl2ConfirmButtonColor = (59,158,80)
                    survol = True
                else:
                    self.attackEl2ConfirmButtonColor = (0,89,19)

            if survol:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


    def update(self):
        self.helpWantedRectSPace = 0
        self.shareTrustRectSpace = 0
        self.attackRectSpace = 0
        self.accuseRectSpace = 0
        self.SniffingRectSpace = 0

        if self.helpWantedOpened:
            self.helpWantedRectSPace = 105
        if self.shareTrustOpened:
            self.shareTrustRectSpace = 161
        if self.attackOpened:
            self.attackRectSpace = 95
        if self.accuseOpened:
            self.accuseRectSpace = 113
        if self.SniffingOpened:
            self.SniffingRectSpace = 120

        width = self.converter.conv_x(205)
        height = self.converter.conv_y(32)
        menusFont = pygame.font.Font(Font.jaini,self.converter.conv_y(25))

        self.helpWantedRect = pygame.Rect(0,0,width,height)
        self.helpWantedText = menusFont.render("Demandes d'aide (0)",True,(255,255,255))
        self.helpWantedTextRect = self.helpWantedText.get_rect(center=(width/2-10,height/2))
        
        long = self.helpWantedRectSPace
        self.shareTrustRect = pygame.Rect(0,height + long + 3,width,height)
        self.shareTrustText = menusFont.render("Partager sa confiance",True,(255,255,255))
        self.shareTrustTextRect = self.helpWantedText.get_rect(center=(width/2-10,3 + long + height + height/2))
        
        long += self.shareTrustRectSpace
        self.attackRect = pygame.Rect(0,height*2 + long + 6,width,height)
        self.attackText = menusFont.render("Attaquer",True,(255,255,255))
        self.attackTextRect = self.helpWantedText.get_rect(center=(width/2-10,6 + long + height*2 + height/2))
        
        long += self.attackRectSpace
        self.accuseRect = pygame.Rect(0,height*3 + long + 9,width,height)
        self.accuseText = menusFont.render("Accuser",True,(255,255,255))
        self.accuseTextRect = self.helpWantedText.get_rect(center=(width/2-10,9 + long + height*3 + height/2))

        long += self.accuseRectSpace
        self.generalRectHeight = self.converter.conv_y(137) + long
        self.generalRect = pygame.Rect(0,0,width,self.generalRectHeight)
        
        long += self.SniffingRectSpace
        self.SniffingRect = pygame.Rect(0,height*4 + long + 12,width,height)
        self.SniffingText = menusFont.render("Sniff",True,(255,255,255))
        self.SniffingTextRect = self.helpWantedText.get_rect(center=(width/2-10,12 + long + height*4 + height/2))
        
        long += self.SniffingRectSpace
        self.generalRectHeight = self.converter.conv_y(137) + long
        self.generalRect = pygame.Rect(0,0,width,self.generalRectHeight)

    def display(self):
        self.screen.blit(self.generalSurface,self.pos)
        self.generalSurface.fill((0,0,0,0))
        pygame.draw.rect(self.generalSurface,(98,98,98),self.generalRect,border_radius=10)

        pygame.draw.rect(self.generalSurface,self.helpWantedRectColor,self.helpWantedRect,border_top_left_radius=10,border_top_right_radius=10)
        self.generalSurface.blit(self.helpWantedText,self.helpWantedTextRect)
        if self.helpWantedOpened:
            self.generalSurface.blit(self.helpWantedEl1PdpImage,self.helpWantedEl1PdpRect)
            self.generalSurface.blit(self.helpWantedEl1Name,self.helpWantedEl1NameRect)
            self.generalSurface.blit(self.helpWantedEl1TreeNumber,self.helpWantedEl1TreeNumberRect)
            pygame.draw.rect(self.generalSurface,(217,217,217),self.helpWantedEl1TrustBgRect)
            pygame.draw.rect(self.generalSurface,self.helpWantedEl1TrustColor,self.helpWantedEl1TrustRect)
            pygame.draw.rect(self.generalSurface,self.helpWantedEl1AcceptButtonBgColor,self.helpWantedEl1AcceptButtonBgRect,border_radius=4)
            self.generalSurface.blit(self.helpWantedEl1AcceptButtonText,self.helpWantedEl1AcceptButtonTextRect)
            pygame.draw.rect(self.generalSurface,self.helpWantedEl1BetrayButtonBgColor,self.helpWantedEl1BetrayButtonBgRect,border_radius=4)
            self.generalSurface.blit(self.helpWantedEl1BetrayButtonText,self.helpWantedEl1BetrayButtonTextRect)
            pygame.draw.rect(self.generalSurface,self.helpWantedEl1RefuseButtonBgColor,self.helpWantedEl1RefuseButtonBgRect,border_radius=4)
            self.generalSurface.blit(self.helpWantedEl1RefuseButtonText,self.helpWantedEl1RefuseButtonTextRect)
            self.generalSurface.blit(self.helpWantedEl1PageNumberText,self.helpWantedEl1PageNumberTextRect)
            self.generalSurface.blit(self.NextButtonImage,self.helpWantedEl1PageNextButtonRect)
            self.generalSurface.blit(self.PrecButtonImage,self.helpWantedEl1PagePrecButtonRect)

        if self.shareTrustOpened:
            self.generalSurface.blit(self.shareTrustEl1TrustText,self.shareTrustEl1TrustTextRect)
            self.generalSurface.blit(self.NextButtonImage,self.shareTrustEl1NextButtonRect)
            self.generalSurface.blit(self.PrecButtonImage,self.shareTrustEl1PrecButtonRect)
            self.generalSurface.blit(self.shareTrustEl1PdpImage,self.shareTrustEl1PdpRect)
            self.generalSurface.blit(self.shareTrustEl1NameText,self.shareTrustEl1NameRect)
            pygame.draw.rect(self.generalSurface,(217,217,217),self.shareTrustEl1TrustBgRect)
            pygame.draw.rect(self.generalSurface,self.shareTrustEl1TrustColor,self.shareTrustEl1TrustRect)
            self.generalSurface.blit(self.shareTrustEl2ShareText,self.shareTrustEl2ShareTextRect)
            self.generalSurface.blit(self.NextButtonImage,self.shareTrustEl2NextButtonRect)
            self.generalSurface.blit(self.PrecButtonImage,self.shareTrustEl2PrecButtonRect)
            self.generalSurface.blit(self.shareTrustEl2PdpImage,self.shareTrustEl2PdpRect)
            self.generalSurface.blit(self.shareTrustEl2NameText,self.shareTrustEl2NameRect)
            pygame.draw.rect(self.generalSurface,(217,217,217),self.shareTrustEl2TrustBgRect)
            pygame.draw.rect(self.generalSurface,self.shareTrustEl2TrustColor,self.shareTrustEl2TrustRect)
            pygame.draw.rect(self.generalSurface,self.shareTrustEl3ConfirmButtonColor,self.shareTrustEl3ConfirmButtonRect,border_radius=4)
            self.generalSurface.blit(self.shareTrustEl3ConfirmButtonText,self.shareTrustEl3ConfirmButtonTextRect)

        if self.attackOpened:
            self.generalSurface.blit(self.attackEl1PageText,self.attackEl1PageTextRect)
            self.generalSurface.blit(self.NextButtonImage,self.attackEl1NextButtonRect)
            self.generalSurface.blit(self.PrecButtonImage,self.attackEl1PrecButtonRect)
            self.generalSurface.blit(self.attackEl1PdpImage,self.attackEl1PdpRect)
            self.generalSurface.blit(self.attackEl1NameText,self.attackEl1NameRect)
            pygame.draw.rect(self.generalSurface,(217,217,217),self.attackEl1TrustBgRect)
            pygame.draw.rect(self.generalSurface,self.attackEl1TrustColor,self.attackEl1TrustRect)
            pygame.draw.rect(self.generalSurface,self.attackEl2ConfirmButtonColor,self.attackEl2ConfirmButtonRect,border_radius=4)
            self.generalSurface.blit(self.attackEl2ConfirmButtonText,self.attackEl2ConfirmButtonTextRect)
            
        if self.accuseOpened:
            self.generalSurface.blit(self.accuseEl1PageText,self.accuseEl1PageTextRect)
            self.generalSurface.blit(self.NextButtonImage,self.accuseEl1NextButtonRect)
            self.generalSurface.blit(self.PrecButtonImage,self.accuseEl1PrecButtonRect)
            self.generalSurface.blit(self.accuseEl1PdpImage,self.accuseEl1PdpRect)
            self.generalSurface.blit(self.accuseEl1NameText,self.accuseEl1NameRect)
            pygame.draw.rect(self.generalSurface,(217,217,217),self.accuseEl1TrustBgRect)
            pygame.draw.rect(self.generalSurface,self.accuseEl1TrustColor,self.accuseEl1TrustRect)
            pygame.draw.rect(self.generalSurface,self.accuseEl2ConfirmButtonColor,self.accuseEl2ConfirmButtonRect,border_radius=4)
            self.generalSurface.blit(self.accuseEl2ConfirmButtonText,self.accuseEl2ConfirmButtonTextRect)
        
        if self.SniffingOpened :
            self.generalSurface.blit(self.SniffingEl1PageText,self.SniffingEl1PageTextRect)
            self.generalSurface.blit(self.NextButtonImage,self.SniffingEl1NextButtonRect)
            self.generalSurface.blit(self.PrecButtonImage,self.SniffingEl1PrecButtonRect)
            self.generalSurface.blit(self.SniffingEl1PdpImage,self.SniffingEl1PdpRect)
            self.generalSurface.blit(self.SniffingEl1NameText,self.SniffingEl1NameRect)
            pygame.draw.rect(self.generalSurface,(217,217,217),self.SniffingEl1TrustBgRect)
            pygame.draw.rect(self.generalSurface,self.SniffingEl1TrustColor,self.SniffingEl1TrustRect)
            pygame.draw.rect(self.generalSurface,self.SniffingEl2ConfirmButtonColor,self.SniffingEl2ConfirmButtonRect,border_radius=4)
            self.generalSurface.blit(self.SniffingEl2ConfirmButtonText,self.SniffingEl2ConfirmButtonTextRect)
        

        pygame.draw.rect(self.generalSurface,self.shareTrustRectColor,self.shareTrustRect)
        self.generalSurface.blit(self.shareTrustText,self.shareTrustTextRect)
        
        pygame.draw.rect(self.generalSurface,self.attackRectColor,self.attackRect)
        self.generalSurface.blit(self.attackText,self.attackTextRect)
        
        if self.accuseOpened:
            pygame.draw.rect(self.generalSurface,self.accuseRectColor,self.accuseRect)
        else:
            pygame.draw.rect(self.generalSurface,self.accuseRectColor,self.accuseRect,border_bottom_left_radius=10,border_bottom_right_radius=10)
        self.generalSurface.blit(self.accuseText,self.accuseTextRect)

        pygame.draw.rect(self.generalSurface,self.SniffingRectColor,self.SniffingRect)
        self.generalSurface.blit(self.SniffingText,self.SniffingTextRect)
        
        pygame.display.flip()

    def run(self,game):
        while self.running:
            self.handling_event()
            game.display()
            self.update()
            self.display()

    def help_wanted_accepted(self):
        pass

    def help_wanted_betrayed(self):
        pass

    def help_wanted_refused(self):
        pass

    def share_trust_confirm(self):
        pass