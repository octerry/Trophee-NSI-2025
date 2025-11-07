import pygame

from Keybinds import keybinds
from Converter import Converter
from NightAction import NightAction
from WitchChoice import WitchChoice
from ClairvoyantReveal import ClairvoyantReveal
from PyromaniacChoice import PyromaniacChoice
from CommonFonction import hover, fade_in, fade_out
from CommonVar import directory
import CommonVar
import Font
import Choose
import SpriteBank

class InTent:
    def __init__(self,screen):
        self.screen = screen
        self.running = True
        self.night = True

        self.commonVar = CommonVar.CommonVar()
        self.converter = Converter(self.screen)
        self.nightAction = NightAction(self.screen)
        self.witchChoice = WitchChoice(self.screen)
        self.clairvoyantReveal = ClairvoyantReveal(self.screen)
        self.pyromaniacChoice = PyromaniacChoice(self.screen)

        self.killEvent = pygame.USEREVENT + 1

        self.frame = 1

        self.bgImage = SpriteBank.fondMap['DansLaTente']
        self.bgImage = pygame.transform.scale(self.bgImage,self.screen.get_size())
        self.bgRect = self.screen.get_rect()

        self.playerSurface = pygame.Surface((self.converter.conv_x(256*1.75),self.converter.conv_y(256*1.75)),pygame.SRCALPHA)
        self.playerImage = SpriteBank.perso[CommonVar.savingDico["creatureSprites"][0]-1]['Static']['Arriere'][0]
        self.playerImage = pygame.transform.scale(self.playerImage,(self.converter.conv_x(256*1.75),self.converter.conv_y(256*1.75)))
        self.playerAlpha = 0

        self.playerPos = [832,1400]
        self.playerMoving = True

        self.transitionBgSurface = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.fadeColor = [0,0,0,0]

        self.roleDico = {
            'Loup-garou':[
                '   En temps que Loup-garou, votre but est de tuer tous les villageois,',
                'et pour se faire chaque nuit vous pourrez voter en groupe pour la',
                'personne que vous voulez tuer pendant la nuit.',
                '',
                '   Si à la fin de la partie il ne reste plus que des Loups-garous,',
                'vous avez gagné.',],
            'Loup Noir':[
                "   En temps que Infeste Père des loups, vous jouez et votez avec les",
                "loups, vous avez une capacité en plus de pouvoir infecter une personne",
                "qui deviendra un simple Loup-garou à partir de la prochaine nuit",
                "",
                "   Si à la fin de la partie il ne reste plus que des Loups-garous",
                "vous avez gagné"
            ],
            'Loup Blanc':[
                '   En temps que Loup-garou Blanc, vous jouez avec les Loups-garous',
                'mais vous devez aussi tuer tous les loups pour gagner. Chaque nuit',
                'vous votez avec les Loups-garous mais une une nuit sur deux vous',
                "devez voter pour tuer l'un des Loups-garous",
                '',
                '   Si à la fin de la partie il ne reste plus que vous,',
                'vous avez gagné'],
            'Voyante':[
                '   En temps que Voyante, vous êtes un villageois avec un pouvoir,',
                'chaque nuit vous pouvez choisir une personne et son rôle vous sera',
                'révélé. De plus, votre confiance augmente si le rôle de cette personne',
                'est dans le camp des villageois, sinon il descends.',
                '',
                '   Si à la fin de la partie il ne reste plus que des villageois,',
                'vous avez gagné.',],
            'Salvateur':[
                '   En temps que Salvateur, vous êtes un villageois avec un pouvoir,',
                "celui de pouvoir protéger pendant la nuit une personne de n'importe",
                'quelle attaque. Vous pouvez utiliser ce pouvoir sur vous-même mais',
                'il est impossible de protéger deux nuits de suite la même personne.',
                '',
                '   Si à la fin de la partie il ne reste plus que des villageois,',
                'vous avez gagné.'],
            'Sorciere':[
                '   En temps que Sorcière, vous jouez avec les villageois et chaque',
                "nuit vous avez le choix d'utiliser une de vos potions à utilisation",
                'unique ou ne rien faire:',
                '',
                ' - Potion de vie : la personne tuée par les Loups-garou pendant la nuit',
                "vous est désignée et la personne est réssucité au reveil.",
                '',
                ' - Potion de mort : vous pouvez tuer ,indépendement des morts pendant',
                'la nuit, une personne au choix dans les personnes encore en vie.',
                '',
                '   Si à la fin de la partie il ne reste plus que des villageois,',
                'vous avez gagné.',],
            'Renard':[
                '   En temps que Renard, vous jouez avec les villageois et vous pouvez',
                "reniffler trois personnes chaque nuit, si l'une de ces trois personnes",
                'est un loup, vous êtes prévenu et vous pouvez recommencer la nuit',
                'suivante, sinon vous perdez votre pouvoir et devenez un simple villageois.',
                '',
                '   Si à la fin de la partie il ne reste plus que des villageois,',
                'vous avez gagné.'],
            'Pyromancien':[
                '   En temps que pyromane, vous jouez seul et chaque nuit vous avez le',
                "choix entre :",
                "- déverser de l'essence sur quelqu'un qui se saura pas qu'il a été choisit",
                "- allumer la mêche et tuer toutes les personnes qui ont de l'essence sur",
                'eux.',
                '',
                '   Si à la fin de la partie il ne reste plus que vous,',
                'vous avez gagné'],
            'Cupidon':[
                '   En temps que Cupidon, vous jouez avec les villageois et au premier',
                "tour vous pouvez mettre en couple deux personne qui mourrons si",
                "l'autre meurt",
                '',
                '   Si à la fin de la partie il ne reste plus que des villageois,',
                'vous avez gagné'],
            'Chasseur':[
                '   En temps que Chasseur, vous jouez avec les villageois et votre',
                "rôle ne sert qu'au moment ou vous mourez, vous pouvez alors désigner",
                "quelqu'un qui mourra avec vous."
                '',
                '   Si à la fin de la partie il ne reste plus que des villageois,',
                'vous avez gagné'],
            'Petite Fille':[
                '   En temps que Petite Fille, vous jouez avec les villageois et vous',
                'observez les loups-garous chaque nuit mais vous devez rester discret',
                'en cliquant sur les signes qui apparaissent et qui pourrait donner',
                'des signes aux loups sur votre identité.',
                '',
                '   Si à la fin de la partie il ne reste plus que des villageois,',
                'vous avez gagné'
            ],
            'Voleur':[
                '   En temps que Voleur, vous jouez avec les villageois et vous pouvez,',
                'une nuit sur deux, échanger le rôle de deux personnes y compris vous.',
                '',
                '   Si à la fin de la partie il ne reste plus que des villageois,',
                'vous avez gagné.'
            ],
            'Bouc Emissaire':[
                "   En temps que Bouc Emissaire, vous êtes un simple villageois.",
                "Cependant, si il y a une égalité lors du vote du village vous",
                "serez éliminé même si vous n'avez aucun vote sur vous",
                "",
                "   Si à la fin de la partie il ne reste plus que des villageois,",
                "vous avez gagné"
            ],
            'Jumaux':[
                "   En temps qu'un des jumaux, vous êtes un simple villageois qui connait",
                "l'identité de l'autre jumaux",
                "",
                "   Si à la fin de la partie il ne reste plus que des villageois,",
                "vous avez gagné"
            ],
            'Villageois':[
                "   En temps que Villageois simple, vous n'avez pas de pouvoir mais",
                'vous pouvez, comme tout le monde, voter la journée et deviner les',
                'rôles de vos voisins.',
                '',
                '   Si à la fin de la partie il ne reste plus que des villageois,',
                'vous avez gagné'],
            'noRole':[
                "   Vous n'avez pas encore de role"
            ]
        }

        self.roleSentence = {
            'Loup':['Votez pour la personne à tuer cette nuit','Sortir de la tente',[112,0,2],self.werewolf_turn],
            'Loup Noir':["Maintenant vous pouvez décider d'infecter une personne",'Sortir de la tente',[112,0,2],self.black_werewolf_turn],
            'Loup Blanc':['Maintenant choisissez un LOUP à tuer','Sortir de la tente',[112,0,2],self.white_werewolf_turn],
            'Sorciere':['Choisissez la potion à utiliser cette nuit',"Sortir de la tente",[83,0,96],self.witch_turn],
            'Chasseur':["Quelqu'un vous a tué, choisissez quelqu'un pour venir avec vous","Viser une tente",[112,0,2],self.hunter_turn],
            'Voyante':['Choisissez la personne à révéler','Sortir la boule de crystal',[0,7,131],self.clairvoyant_turn],
            'Salvateur':['Choisissez la persone à protéger',"Sortir protéger une tente",[0,45,96],self.salvator_turn],
            'Cupidon':['Choisissez les personnes à mettre en couple',"Sortir de la tente",[131,0,83],self.cupidon_turn],
            'Petite Fille':['Espionnez discretement le vote des loups-garous',"Entre-ouvrir la tente",[0,87,97],self.little_girl_turn],
            'Pyromancien':['Sortez préparer votre incendie',"Sortir de la tente",[112,0,2],self.pyromaniac_turn],
            'Bouc Emissaire':["Vous n'avez rien à faire cette nuit","Dormir",[0,87,97],self.villager_turn],
            'Renard':['Choisissez les personnes à reniffler cette nuit',"Sortir de la tente",[0,7,131],self.fox_turn],
            'Jumaux':["Vous n'avez rien à faire cette nuit","Dormir",[0,87,97],self.villager_turn],
            'Villageois':["Vous n'avez rien à faire cette nuit","Dormir",[0,87,97],self.villager_turn],
            'noRole':["Pourquoi resteriez vous éveillé ? il n'y a rien de dangereux",'Dormir',[0,87,97],self.villager_turn]
        }

        playerRole = CommonVar.savingDico['creatureRoles'][0]
        if not playerRole:
            playerRole = 'noRole'
        self.roleExplicationShow = False
        self.roleExplicationTitleFont = pygame.font.Font(Font.jacquard,self.converter.conv_y(134))
        self.roleExplicationTitleText = self.roleExplicationTitleFont.render(playerRole,True,(0,0,0))
        self.roleExplicationTitleTextRect = self.roleExplicationTitleText.get_rect(center=(self.screen.get_width()-self.converter.conv_x(400),self.converter.conv_y(100)))
        self.roleExplicationTitleBgRect = pygame.Rect(self.screen.get_width()-(len(playerRole)*self.converter.conv_x(60)+self.converter.conv_x(800))/2,self.converter.conv_y(34),len(playerRole)*self.converter.conv_x(60),self.converter.conv_y(134))
        self.roleExplicationTitleBgColor = (217,217,217)

        paragaphFont = pygame.font.Font(Font.IMfell,self.converter.conv_y(50))
        paragaph = self.roleDico[playerRole]
        self.roleExplicationBgRect = pygame.Rect(self.converter.conv_x(100),self.converter.conv_y(198),self.screen.get_width()-self.converter.conv_x(200),len(paragaph)*self.converter.conv_y(60)+self.converter.conv_y(60))
        
        for i in range(len(paragaph)):
            setattr(self,f'roleExplicationText{i}',paragaphFont.render(paragaph[i],True,(255,255,255)))
            setattr(self,f'roleExplicationText{i}Rect',getattr(self,f'roleExplicationText{i}').get_rect(topleft=(self.converter.conv_x(150),self.converter.conv_y(218 + 60*i))))
            
        if playerRole[:3] == "Loup":
            playerRole = "Loup"
        self.actionShow = False
        self.actionTitleFont = pygame.font.Font(Font.jacquard,self.converter.conv_y(134))
        self.actionTitleText = self.actionTitleFont.render('Action de Rôle',True,(0,0,0))
        self.actionTitleTextRect = self.actionTitleText.get_rect(center=(self.converter.conv_x(500),self.converter.conv_y(100)))
        self.actionTitleBgRect = pygame.Rect(self.converter.conv_x(100),self.converter.conv_y(34),14*self.converter.conv_x(57),self.converter.conv_y(134))
        self.actionTitleBgColor = (217,217,217)

        self.actionBgRect = pygame.Rect(self.converter.conv_x(100),self.converter.conv_y(198),self.screen.get_width()-self.converter.conv_x(200),self.converter.conv_y(220))
        if CommonVar.savingDico['cycle'] != 1 and playerRole == 'Cupidon':
            playerRole == "Villageois"
        elif CommonVar.savingDico['creatureTentState'][0] and playerRole == 'Chasseur':
            playerRole == "Villageois"

        if playerRole[:4] == "Loup":
            playerRole = "Loup"
        self.actionText = paragaphFont.render(self.roleSentence[playerRole][0],True,(255,255,255))
        self.actionTextRect = self.actionText.get_rect(center=(self.screen.get_width()/2,self.converter.conv_y(250)))
        self.actionButtonRect = pygame.Rect(self.screen.get_width()/2-len(self.roleSentence[playerRole][1])/2*self.converter.conv_x(50),self.converter.conv_y(300),len(self.roleSentence[playerRole][1])*self.converter.conv_x(50),self.converter.conv_y(100))
        self.actionButtonFont = pygame.font.Font(Font.jaini,self.converter.conv_y(100))
        self.actionButtonText = self.actionButtonFont.render(self.roleSentence[playerRole][1],True,(255,255,255))
        self.actionButtonTextRect = self.actionButtonText.get_rect(topleft=(self.actionButtonRect[0]+self.converter.conv_x(30),self.actionButtonRect[1]-self.converter.conv_y(20)))
        self.actionButtonEvent = self.roleSentence[playerRole][3]
        playerRole = CommonVar.savingDico['creatureRoles'][0]

        self.order = ['Cupidon','Voyante','Salvateur','Loup-garou','Loup Blanc','Pyromane','Sorciere','Renard','Villageois']

    def handling_event(self,window):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: ##Si le joueur appuie sur la croix de la fenetre
                self.commonVar.update_saving_json()
                self.commonVar.update_common_json()
                pygame.quit() ##Le jeu s'arrete

            survol = False
            if hover(event,self.roleExplicationTitleBgRect)[0]:
                survol = True
                self.roleExplicationTitleBgColor = (217,217,255)
                if hover(event,self.roleExplicationTitleBgRect)[1]:
                    self.roleExplicationShow = not self.roleExplicationShow
                    self.actionShow = False
            else:
                self.roleExplicationTitleBgColor = (217,217,217)

            if hover(event,self.actionTitleBgRect)[0] and self.night:
                survol = True
                self.actionTitleBgColor = (217,217,255)
                if hover(event,self.actionTitleBgRect)[1]:
                    self.actionShow = not self.actionShow
                    self.roleExplicationShow = False
            else:
                self.actionTitleBgColor = (217,217,217)

            if hover(event,self.actionButtonRect)[0] and self.actionShow:
                survol = True
                if hover(event,self.actionButtonRect)[1]:
                    self.actionButtonEvent(window)

            keys = pygame.key.get_pressed()
            if keys[keybinds['openMenu']]:
                self.fade_to_menus(window)

            if survol :
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def update(self):
        if self.playerMoving:
            self.playerImage = SpriteBank.perso[CommonVar.savingDico["creatureSprites"][0]-1]['Run']['Gauche'][self.frame]
            self.playerImage = pygame.transform.scale(self.playerImage,(self.converter.conv_x(256*1.75),self.converter.conv_y(256*1.75)))
            self.playerImage.set_alpha(self.playerAlpha)
            self.playerPos[1] -= self.converter.conv_y(25*0.75)
            self.playerPos[0] -= self.converter.conv_x(45*0.75)
            if self.playerPos[1] <= self.converter.conv_y(800):
                if self.playerAlpha < 250:
                    self.playerAlpha += 10
            if self.playerPos[0] <= self.converter.conv_x(self.screen.get_width()/2-self.converter.conv_x(128*1.75)):
                self.playerMoving = False
        else:
            self.playerAlpha = 255
            self.playerImage = SpriteBank.perso[CommonVar.savingDico["creatureSprites"][0]-1]['Static']['Arriere'][self.frame//2 + 1]
            self.playerImage = pygame.transform.scale(self.playerImage,(self.converter.conv_x(256*1.75),self.converter.conv_y(256*1.75)))
            self.playerImage.set_alpha(self.playerAlpha)

    def display(self):
        self.screen.blit(self.bgImage,self.bgRect)

        self.screen.blit(self.playerSurface,(self.playerPos[0],self.playerPos[1],self.converter.conv_x(256*1.75),self.converter.conv_y(256*1.75)))
        self.playerSurface.fill((0,0,0,0))
        self.playerSurface.blit(self.playerImage,(0,0),(0,0,self.converter.conv_x(256*1.75),self.converter.conv_y(256*1.75)))

        pygame.draw.rect(self.screen,self.roleExplicationTitleBgColor,self.roleExplicationTitleBgRect,border_radius=20)
        self.screen.blit(self.roleExplicationTitleText,self.roleExplicationTitleTextRect)
        if self.night:
            pygame.draw.rect(self.screen,self.actionTitleBgColor,self.actionTitleBgRect,border_radius=20)
            self.screen.blit(self.actionTitleText,self.actionTitleTextRect)

        if self.roleExplicationShow:
            if CommonVar.savingDico['creatureRoles'][0]:
                if (CommonVar.savingDico['creatureRoles'][0] == "Renard" and not CommonVar.savingDico['foxPower']) or (CommonVar.savingDico['creatureRoles'][0] == "Cupidon" and CommonVar.savingDico['cycle'] != 1):
                    paragaph = self.roleDico['Villageois']
                else:
                    paragaph = self.roleDico[CommonVar.savingDico['creatureRoles'][0]]
            else:
                paragaph = self.roleDico['noRole']
            pygame.draw.rect(self.screen,(51,45,45),self.roleExplicationBgRect,border_radius=30)
            for i in range(len(paragaph)):
                self.screen.blit(getattr(self,f'roleExplicationText{i}'),getattr(self,f'roleExplicationText{i}Rect'))
        
        if self.actionShow:
            pygame.draw.rect(self.screen,(51,45,45),self.actionBgRect,border_radius=30)
            self.screen.blit(self.actionText,self.actionTextRect)
            if CommonVar.savingDico['creatureRoles'][0]:
                pygame.draw.rect(self.screen,self.roleSentence['noRole'][2],self.actionButtonRect,border_radius=30)
            else:
                pygame.draw.rect(self.screen,self.roleSentence['noRole'][2],self.actionButtonRect,border_radius=30)
            self.screen.blit(self.actionButtonText,self.actionButtonTextRect)

        ## Affichage du fondu enchainé (calque noir)
        self.screen.blit(self.transitionBgSurface,(0,0))
        self.transitionBgSurface.fill(self.fadeColor)

        if not self.nightAction.running:
            pygame.display.flip()

    def run(self,window):
        while self.running and window.game.running:
            if not self.nightAction.running and not self.witchChoice.running:
                self.handling_event(window)
                self.update()
                self.display()

    def fade_out(self):
        self.running = True
        if self.nightAction.running:
            fade_in(self.nightAction, 60)
        else:
            pygame.display.set_caption("Nox Villae [En jeu]")
            fade_in(self, 60)
            self.playerAlpha = 0
            self.playerPos = [self.converter.conv_x(2120),self.converter.conv_y(1080)]
            self.playerMoving = True

    def fade_to_menus(self,window):
        fade_out(self, 60)
        fade_in(window.menus, 60)
        window.menus.start_threading()

    def fade_to_vote(self,window):

        for i in range(CommonVar.savingDico['creatureNumber']):
            CommonVar.savingDico['creaturePositions'][i] = window.game.tentPositions[CommonVar.savingDico['creatureTent'][i]]
        CommonVar.savingDico['creatureDestinations'] = [None for _ in range(CommonVar.savingDico['creatureNumber'])]
        
        self.time = True
        self.startingTime = 0
        self.timer = pygame.USEREVENT +1
        pygame.time.set_timer(self.timer,1000,100)
        self.timeShow = int(CommonVar.savingDico['timeRemaining']) - self.startingTime
        self.timeShowConvert = str(self.timeShow//60).zfill(2) + ':' + str(self.timeShow%60).zfill(2)
        
        fade_in(window.game.vote, 60, window)

    def fade_to_night_action(self):
        self.get_out_animation()
        fade_out(self, 60)
        self.playerPos[1] = self.converter.conv_y(1400)
        self.nightAction.role = CommonVar.savingDico['creatureRole'][0]
        self.nightAction.fade_out()

    def werewolf_turn(self,window): # TOUR DES LOUPS
        self.wolf_turn(window)
        
        self.fade_to_vote(window)

    def wolf_turn(self,window):

        self.get_out_animation()
        self.nightAction.maxSelection = 1
        self.nightAction.running = True
        self.nightAction.autoChoosing = True
        self.nightAction.werewolf_init()
                
        while self.nightAction.werewolfRunning:
            self.nightAction.werewolf_run()
            self.nightAction.run(window)
            
        playerChoose = self.nightAction.tentPositions.index(self.nightAction.selectedConfirmPosition[0])
        playerChoose = CommonVar.savingDico['creatureTent'].index(playerChoose)
        self.nightAction.werewolfChoose[playerChoose] += 1
        self.toKill = Choose.max_tab_i(self.nightAction.werewolfChoose)

        if self.toKill:
            self.nightAction.title = f"Les loups on décidé de tuer {CommonVar.savingDico['creatureId'][self.toKill]}"
            self.nightAction.werewolf_goto(CommonVar.savingDico['creatureTent'][self.toKill])
        else:
            self.nightAction.title = f"Les loups n'ont pas réussi à se décider"

        self.nightAction.titleText = self.nightAction.titleFont.render(self.nightAction.title,True,(255,255,255))
        self.nightAction.titleTextRect = self.nightAction.titleText.get_rect(center=(self.screen.get_width()/2,self.converter.conv_y(100)))
        self.nightAction.titleRect = pygame.Rect(self.screen.get_width()/2 - len(self.nightAction.title)*self.converter.conv_x(30)/2,self.converter.conv_y(60),len(self.nightAction.title)*self.converter.conv_x(30),self.converter.conv_y(80))

        while self.nightAction.running:
            self.nightAction.werewolf_run()
            self.nightAction.run(window)

        if self.toKill and not CommonVar.savingDico['witchUseHeal'] and CommonVar.savingDico['protected'] != self.toKill:
            self.kill(self.toKill)
            self.voteText = f"le village a décidé d'éliminer {CommonVar.savingDico['creatureId'][self.toKill]} ({max(self.nightAction.werewolfChoose)} voix)"
        self.votePossibility = False
        pygame.time.set_timer(self.killEvent,5000)
        self.selectionSelectedRectShow = False


    def white_werewolf_turn(self,window):
        self.wolf_turn(window)

        if CommonVar.savingDico['cycle']%2 == 0:
            self.nightAction.titleText = self.nightAction.titleFont.render("Votez pour le loup à tuer",True,(255,255,255))
            self.nightAction.titleTextRect = self.nightAction.titleText.get_rect(center=(self.screen.get_width()/2,self.converter.conv_y(100)))
            self.nightAction.titleRect = pygame.Rect(self.screen.get_width()/2 - len(self.nightAction.title)*self.converter.conv_x(30)/2,self.converter.conv_y(60),len(self.nightAction.title)*self.converter.conv_x(30),self.converter.conv_y(80))

            self.nightAction.running = True
            self.nightAction.autoChoosing = False
            while self.nightAction.running:
                self.nightAction.run(window)
                pygame.display.flip()

            playerChoice = self.nightAction.tentPositions.index(self.nightAction.selectedConfirmPosition[0])
            playerChoice = CommonVar.savingDico['creatureTent'].index(playerChoice)
            self.kill(playerChoice)

        self.fade_to_vote(window)

    def black_werewolf_turn(self,window):
        self.fade_to_vote(window)

    def clairvoyant_turn(self,window):
        self.nightAction.titleText = self.nightAction.titleFont.render("Votez pour la tente à scruter",True,(255,255,255))
        self.nightAction.titleTextRect = self.nightAction.titleText.get_rect(center=(self.screen.get_width()/2,self.converter.conv_y(100)))
        self.nightAction.titleRect = pygame.Rect(self.screen.get_width()/2 - len(self.nightAction.title)*self.converter.conv_x(30)/2,self.converter.conv_y(60),len(self.nightAction.title)*self.converter.conv_x(30),self.converter.conv_y(80))

        self.nightAction.maxSelection = 1

        self.nightAction.autoChoosing = False
        self.fade_to_night_action()
        while self.nightAction.running:
            self.nightAction.run(window)
            pygame.display.flip()

        self.clairvoyantReveal.targetId = self.nightAction.tentPositions.index(self.nightAction.selectedConfirmPosition[0])
        self.clairvoyantReveal.targetId = CommonVar.savingDico['creatureTent'].index(self.clairvoyantReveal.targetId)
        self.clairvoyantReveal.running = True
        self.clairvoyantReveal.update_text()
        self.clairvoyantReveal.run()

        self.fade_to_vote(window)

    def cupidon_turn(self,window):
        if CommonVar.savingDico['cycle'] == 1:
            self.nightAction.titleText = self.nightAction.titleFont.render("Votez pour le couple inséparable",True,(255,255,255))
            self.nightAction.titleTextRect = self.nightAction.titleText.get_rect(center=(self.screen.get_width()/2,self.converter.conv_y(100)))
            self.nightAction.titleRect = pygame.Rect(self.screen.get_width()/2 - len(self.nightAction.title)*self.converter.conv_x(30)/2,self.converter.conv_y(60),len(self.nightAction.title)*self.converter.conv_x(30),self.converter.conv_y(80))

            self.nightAction.maxSelection = 2

            self.nightAction.autoChoosing = True
            self.fade_to_night_action()
            while self.nightAction.running:
                self.nightAction.run(window)
                pygame.display.flip()

            tabId = []
            for i in range(2):
                playerChoice = self.nightAction.tentPositions.index(self.nightAction.selectedConfirmPosition[i])
                playerChoice = CommonVar.savingDico['creatureTent'].index(playerChoice)
                tabId.append(playerChoice)
            
            CommonVar.savingDico['lovers'] = tabId

        self.fade_to_vote(window)

    def witch_turn(self,window):
        CommonVar.savingDico['witchUseHeal'] = False

        self.witchChoice.running = True
        fade_out(self, 60)
        fade_in(self.witchChoice, 60)
        self.witchChoice.run()

        if self.witchChoice.chosen == "death":
            self.nightAction.maxSelection = 1
            self.nightAction.titleText = self.nightAction.titleFont.render("Votez pour la personne à empoisonner",True,(255,255,255))
            self.nightAction.titleTextRect = self.nightAction.titleText.get_rect(center=(self.screen.get_width()/2,self.converter.conv_y(100)))
            self.nightAction.titleRect = pygame.Rect(self.screen.get_width()/2 - len(self.nightAction.title)*self.converter.conv_x(30)/2,self.converter.conv_y(60),len(self.nightAction.title)*self.converter.conv_x(30),self.converter.conv_y(80))

            self.nightAction.autoChoosing = False
            self.fade_to_night_action()
            while self.nightAction.running:
                self.nightAction.run(window)
                pygame.display.flip()

            playerChoice = self.nightAction.tentPositions.index(self.nightAction.selectedConfirmPosition[0])
            playerChoice = CommonVar.savingDico['creatureTent'].index(playerChoice)
            self.kill(playerChoice)
        elif self.witchChoice.chosen == "revive":
            CommonVar.savingDico['witchUseHeal'] = True

        self.fade_to_vote(window)

    def salvator_turn(self,window):
        self.nightAction.titleText = self.nightAction.titleFont.render("Votez pour la personne à protéger",True,(255,255,255))
        self.nightAction.titleTextRect = self.nightAction.titleText.get_rect(center=(self.screen.get_width()/2,self.converter.conv_y(100)))
        self.nightAction.titleRect = pygame.Rect(self.screen.get_width()/2 - len(self.nightAction.title)*self.converter.conv_x(30)/2,self.converter.conv_y(60),len(self.nightAction.title)*self.converter.conv_x(30),self.converter.conv_y(80))

        self.nightAction.maxSelection = 1

        self.nightAction.running = True
        self.nightAction.autoChoosing = True
        while self.nightAction.running:
            self.nightAction.run(window)
            pygame.display.flip()

        
        playerChoice = self.nightAction.tentPositions.index(self.nightAction.selectedConfirmPosition[0])
        playerChoice = CommonVar.savingDico['creatureTent'].index(playerChoice)
        CommonVar.savingDico['protected'] = playerChoice

        self.fade_to_vote(window)

    def fox_turn(self,window):
        if CommonVar.savingDico['foxPower']:
            self.nightAction.titleText = self.nightAction.titleFont.render("Votez pour les personnes à renifler",True,(255,255,255))
            self.nightAction.titleTextRect = self.nightAction.titleText.get_rect(center=(self.screen.get_width()/2,self.converter.conv_y(100)))
            self.nightAction.titleRect = pygame.Rect(self.screen.get_width()/2 - len(self.nightAction.title)*self.converter.conv_x(30)/2,self.converter.conv_y(60),len(self.nightAction.title)*self.converter.conv_x(30),self.converter.conv_y(80))

            self.nightAction.maxSelection = 3

            self.nightAction.running = True
            self.nightAction.autoChoosing = False
            while self.nightAction.running:
                self.nightAction.run(window)
                pygame.display.flip()

            tabId = []
            for i in range(3):
                playerChoice = self.nightAction.tentPositions.index(self.nightAction.selectedConfirmPosition[i])
                playerChoice = CommonVar.savingDico['creatureTent'].index(playerChoice)
                tabId.append(playerChoice)

            if not any(tabId):
                CommonVar.savingDico['foxPower'] = False

        self.fade_to_vote(window)

    def hunter_turn(self,window):
        if not CommonVar.savingDico['creatureTentState'][0]:
            self.nightAction.titleText = self.nightAction.titleFont.render("On vous a tué, emportez quelqu'un avec vous",True,(255,255,255))
            self.nightAction.titleTextRect = self.nightAction.titleText.get_rect(center=(self.screen.get_width()/2,self.converter.conv_y(100)))
            self.nightAction.titleRect = pygame.Rect(self.screen.get_width()/2 - len(self.nightAction.title)*self.converter.conv_x(30)/2,self.converter.conv_y(60),len(self.nightAction.title)*self.converter.conv_x(30),self.converter.conv_y(80))

            self.nightAction.maxSelection = 1

            self.nightAction.running = True
            self.nightAction.autoChoosing = False
            while self.nightAction.running:
                self.nightAction.run(window)
                pygame.display.flip()

            playerChoice = self.nightAction.tentPositions.index(self.nightAction.selectedConfirmPosition[0])
            playerChoice = CommonVar.savingDico['creatureTent'].index(playerChoice)
            self.kill(playerChoice)

        self.fade_to_vote(window)

    def pyromaniac_turn(self,window):
        self.pyromaniacChoice.running = True
        self.pyromaniacChoice.run()

        if self.pyromaniacChoice.chosen == "keg":
            self.nightAction.titleText = self.nightAction.titleFont.render("Choisissez chez qui cacher un tonneau explosif",True,(255,255,255))
            self.nightAction.titleTextRect = self.nightAction.titleText.get_rect(center=(self.screen.get_width()/2,self.converter.conv_y(100)))
            self.nightAction.titleRect = pygame.Rect(self.screen.get_width()/2 - len(self.nightAction.title)*self.converter.conv_x(30)/2,self.converter.conv_y(60),len(self.nightAction.title)*self.converter.conv_x(30),self.converter.conv_y(80))

            self.nightAction.maxSelection = 1

            self.nightAction.running = True
            self.nightAction.autoChoosing = False
            while self.nightAction.running:
                self.nightAction.run(window)
                pygame.display.flip()

            playerChoice = self.nightAction.tentPositions.index(self.nightAction.selectedConfirmPosition[0])
            playerChoice = CommonVar.savingDico['creatureTent'].index(playerChoice)
            CommonVar.savingDico['pyromaniacTarget'].append(playerChoice )
        else:
            if CommonVar.savingDico['pyromaniacTarget'] == []:
                pass
            else:
                for target in CommonVar.savingDico['pyromaniacTarget']:
                    self.kill(target)
                CommonVar.savingDico['pyromaniacTarget'] = []

        self.fade_to_vote(window)

    def little_girl_turn(self,window):
        
        self.get_out_animation()

        self.nightAction.titleText = self.nightAction.titleFont.render("Voici tous les votes des loups-garous",True,(255,255,255))
        self.nightAction.maxSelection = 1
        self.nightAction.running = True
        self.nightAction.werewolf_init()
                
        while self.nightAction.werewolfRunning:
            self.nightAction.werewolf_run()
            self.nightAction.run(window)
            
        self.fade_to_vote(window)

    def villager_turn(self,window):
        self.fade_to_vote(window)

    def get_out_animation(self):
        self.playerImage = SpriteBank.perso[CommonVar.savingDico["creatureSprites"][0]-1]['Run']['Droite'][self.frame]
        self.playerImage = pygame.transform.scale(self.playerImage,(self.converter.conv_x(256*1.75),self.converter.conv_y(256*1.75)))
        while self.playerPos[1] < self.converter.conv_y(1000):
            self.playerPos[1] += self.converter.conv_y(25*0.75)
            self.playerPos[0] += self.converter.conv_x(45*0.75)
            self.playerAlpha -= 25
            self.playerImage.set_alpha(self.playerAlpha)
            self.display()
            
    def kill(self,selectedId):
        CommonVar.savingDico['creatureTentState'][selectedId] = False