import pygame
import math 

from Keybinds import keybinds
from Converter import Converter
from CommonFonction import hover
from CommonVar import directory
import CommonVar
import Font
import RoleDefinition
import SpriteBank

class SaveMenu:
    def __init__(self,screen,background):
        self.screen = screen
        self.background = background
        self.running = False
        self.generalSettings = True ## True : parametres généraux , False : configuration des touches

        self.converter = Converter(self.screen)
        self.commonVar = CommonVar.CommonVar()

        self.homeIconImage = SpriteBank.logo['Home']
        self.homeIconRect = self.homeIconImage.get_rect()
        self.homeIconImage = pygame.transform.scale(self.homeIconImage, (self.converter.conv_x(100),self.converter.conv_y(100)))
        self.homeIconBgSurface = pygame.Surface((self.converter.conv_x(200),self.converter.conv_y(200)), pygame.SRCALPHA)
        self.homeIconBgAlpha = 120

        self.menuTitleFont = pygame.font.Font(Font.jaini, self.converter.conv_y(150))
        self.menuTitleText = self.menuTitleFont.render("Sauvegardes",True,(240,240,240))
        self.menuTitleRect = self.menuTitleText.get_rect(center=(self.screen.get_width()/2,self.converter.conv_y(150)))
        self.menuTitleBgSurface = pygame.Surface((self.screen.get_width(),self.converter.conv_y(300)), pygame.SRCALPHA)

        self.namesFont = pygame.font.Font(Font.jaini, self.converter.conv_y(70))
        self.elementFont = pygame.font.Font(Font.jaini, self.converter.conv_y(65))
        self.subtitleFont = pygame.font.Font(Font.jaini, self.converter.conv_y(50))

        for n in range(self.commonVar.nJson()):
            openSave = self.commonVar.openSave(n+1)

            x = self.converter.conv_x(1800)
            y = self.converter.conv_y(175)
            setattr(self,f'save{n}BgSurface',pygame.Surface((x,y),pygame.SRCALPHA))
            setattr(self,f'save{n}BgColor',120)

            setattr(self,f'save{n}TitleText',self.namesFont.render(f'Sauvegarde {n+1}',True,(255,255,255)))
            setattr(self,f'save{n}TitleRect',getattr(self,f'save{n}TitleText').get_rect(topleft=(self.converter.conv_x(25),0)))

            setattr(self,f'save{n}Name',openSave['creatureId'][0])
            setattr(self,f'save{n}NameText',self.elementFont.render(getattr(self,f'save{n}Name'),True,(0,0,0)))
            setattr(self,f'save{n}NameTextRect',getattr(self,f'save{n}NameText').get_rect(topleft=(self.converter.conv_x(35),self.converter.conv_y(70))))
            setattr(self,f'save{n}NameBgRect',pygame.Rect(self.converter.conv_x(25),self.converter.conv_y(85),len(getattr(self,f'save{n}Name'))*self.converter.conv_x(27)+self.converter.conv_x(20),self.converter.conv_y(70)))
            
            if openSave['creatureRoles'][0]:
                setattr(self,f'save{n}Role',openSave['creatureRoles'][0])
            else:
                setattr(self,f'save{n}Role','Aucun')
            setattr(self,f'save{n}RoleText',self.elementFont.render(getattr(self,f'save{n}Role'),True,(0,0,0)))
            x = max(self.converter.conv_x(400),len(getattr(self,f'save{n}Name'))*self.converter.conv_x(25)+self.converter.conv_x(50))
            setattr(self,f'save{n}RoleTextRect',getattr(self,f'save{n}RoleText').get_rect(topleft=(x + self.converter.conv_x(15),self.converter.conv_y(70))))
            setattr(self,f'save{n}RoleBgRect',pygame.Rect(x,self.converter.conv_y(85),len(getattr(self,f'save{n}Role'))*self.converter.conv_x(25)+self.converter.conv_x(20),self.converter.conv_y(70)))
            setattr(self,f'save{n}RoleTitle',self.subtitleFont.render('Rôle',True,(255,255,255)))
            setattr(self,f'save{n}RoleTitleRect',getattr(self,f'save{n}RoleTitle').get_rect(center=(x + self.converter.conv_x(35),self.converter.conv_y(55))))

            setattr(self,f'save{n}Mates',str(len(openSave['creatureMates'][0])))
            setattr(self,f'save{n}MatesText',self.elementFont.render(getattr(self,f'save{n}Mates'),True,(0,0,0)))
            setattr(self,f'save{n}MatesTextRect',getattr(self,f'save{n}MatesText').get_rect(topleft=(self.converter.conv_x(825),self.converter.conv_y(70))))
            setattr(self,f'save{n}MatesBgRect',pygame.Rect(self.converter.conv_x(817),self.converter.conv_y(85),len(getattr(self,f'save{n}Mates'))*self.converter.conv_x(25)+self.converter.conv_x(20),self.converter.conv_y(70)))
            setattr(self,f'save{n}MatesTitle',self.subtitleFont.render('Proche(s)',True,(255,255,255)))
            setattr(self,f'save{n}MatesTitleRect',getattr(self,f'save{n}MatesTitle').get_rect(center=(self.converter.conv_x(850),self.converter.conv_y(55))))

            setattr(self,f'save{n}Evilness',str(openSave['creatureEvilness'][0]))
            setattr(self,f'save{n}EvilnessText',self.elementFont.render(getattr(self,f'save{n}Evilness'),True,(0,0,0)))
            setattr(self,f'save{n}EvilnessTextRect',getattr(self,f'save{n}EvilnessText').get_rect(topleft=(self.converter.conv_x(1075),self.converter.conv_y(70))))
            setattr(self,f'save{n}EvilnessBgRect',pygame.Rect(self.converter.conv_x(1067),self.converter.conv_y(85),len(getattr(self,f'save{n}Evilness'))*self.converter.conv_x(25)+self.converter.conv_x(20),self.converter.conv_y(70)))
            setattr(self,f'save{n}EvilnessTitle',self.subtitleFont.render('Niveau de mal',True,(255,255,255)))
            setattr(self,f'save{n}EvilnessTitleRect',getattr(self,f'save{n}EvilnessTitle').get_rect(center=(self.converter.conv_x(1100),self.converter.conv_y(55))))
            
            setattr(self,f'save{n}CreatureNumber',str(openSave['creatureNumber']))
            setattr(self,f'save{n}CreatureNumberText',self.elementFont.render(getattr(self,f'save{n}CreatureNumber'),True,(0,0,0)))
            setattr(self,f'save{n}CreatureNumberTextRect',getattr(self,f'save{n}CreatureNumberText').get_rect(topleft=(self.converter.conv_x(1425),self.converter.conv_y(70))))
            setattr(self,f'save{n}CreatureNumberBgRect',pygame.Rect(self.converter.conv_x(1417),self.converter.conv_y(85),len(getattr(self,f'save{n}CreatureNumber'))*self.converter.conv_x(25)+self.converter.conv_x(20),self.converter.conv_y(70)))
            setattr(self,f'save{n}CreatureNumberTitle',self.subtitleFont.render('Nombre de villageois',True,(255,255,255)))
            setattr(self,f'save{n}CreatureNumberTitleRect',getattr(self,f'save{n}CreatureNumberTitle').get_rect(center=(self.converter.conv_x(1450),self.converter.conv_y(55))))

            width = getattr(self,f'save{n}BgSurface').get_width()
            setattr(self,f'save{n}Cycle',str(openSave['cycle']))
            setattr(self,f'save{n}CycleText',self.elementFont.render(getattr(self,f'save{n}Cycle'),True,(0,0,0)))
            setattr(self,f'save{n}CycleTextRect',getattr(self,f'save{n}CycleText').get_rect(topleft=(width - (len(getattr(self,f'save{n}CreatureNumber'))*self.converter.conv_x(25)+self.converter.conv_x(30)),self.converter.conv_y(70))))
            setattr(self,f'save{n}CycleBgRect',pygame.Rect(width - (len(getattr(self,f'save{n}CreatureNumber'))*self.converter.conv_x(25)+self.converter.conv_x(40)),self.converter.conv_y(85),len(getattr(self,f'save{n}Cycle'))*self.converter.conv_x(25)+self.converter.conv_x(20),self.converter.conv_y(70)))
            setattr(self,f'save{n}CycleTitle',self.elementFont.render('Cycle',True,(255,255,255)))
            setattr(self,f'save{n}CycleTitleRect',getattr(self,f'save{n}CycleTitle').get_rect(topright=(width - (len(getattr(self,f'save{n}CreatureNumber'))*self.converter.conv_x(25)+self.converter.conv_x(40)),self.converter.conv_y(70))))

            setattr(self,f'save{n}DeleteButtonRect',pygame.Rect(width-self.converter.conv_x(70),self.converter.conv_y(20),self.converter.conv_x(50),self.converter.conv_y(50)))
            setattr(self,f'save{n}DeleteButtonColor',(255,100,105))

        self.newSaveButtonSurface = pygame.Surface((self.converter.conv_x(644),self.converter.conv_y(175)),pygame.SRCALPHA)
        self.newSaveButtonColor = 120
        self.newSaveButtonPlusColor = (170,170,170)
        
    def hover_circle(self, event, circle_center, circle_radius):
        mouse_pos = pygame.mouse.get_pos()
        if math.dist(mouse_pos, circle_center) < circle_radius: # Quand la souris rentre dans le cercle
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return True,True # Touche : True , Clique : True
            return True,False # Touche : True , Clique : False
        else:
            return False,False # Touche : False

    def handling_event(self): ##Tous les évenements (joueur -> jeu) seront ici
        for event in pygame.event.get():
            if event.type == pygame.QUIT: ##Si le joueur appuie sur la croix de la fenetre
                self.commonVar.update_saving_json()
                self.commonVar.update_common_json()
                pygame.quit() ##Le jeu s'arrete
            
            keys = pygame.key.get_pressed()
            if keys[keybinds['openMenu']]:
                self.running = False
                self.background.alpha = 255
            
            survol = False

            if self.hover_circle(event, (150,self.screen.get_height() - 150), 70)[0]:
                self.homeIconBgAlpha = 120
                survol = True
                if self.hover_circle(event, (150,self.screen.get_height() - 150), 70)[1]:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    self.running = False
                    self.background.alpha = 255
            else:
                self.homeIconBgAlpha = 60

            if self.commonVar.nJson() < 3:
                coor = (self.screen.get_width()/2 - self.converter.conv_x(322),self.converter.conv_y(270) + self.converter.conv_y(190)*(self.commonVar.nJson()))
                if hover(event,self.newSaveButtonSurface.get_rect(topleft=coor))[0]:
                    self.newSaveButtonPlusColor = (255,255,255)
                    self.newSaveButtonColor = (50,50,50,220)
                    survol = True
                    if hover(event,self.newSaveButtonSurface.get_rect(topleft=coor))[1]:
                        self.commonVar.update_saving_json()
                        self.commonVar.create_new_save()
                        self.commonVar.update_saving_var()
                        self.update_display()
                else:
                    self.newSaveButtonPlusColor = (170,170,170)
                    self.newSaveButtonColor = (0,0,0,120)

            for n in range(self.commonVar.nJson()):
                coor = self.screen.get_width()/2-self.converter.conv_x(900),self.converter.conv_y(190)*n + self.screen.get_height()*(0.25)
                
                tempCross = pygame.Rect(coor[0] + getattr(self,f'save{n}DeleteButtonRect')[0],coor[1] + getattr(self,f'save{n}DeleteButtonRect')[1],getattr(self,f'save{n}DeleteButtonRect')[2],getattr(self,f'save{n}DeleteButtonRect')[3])
                hoverCross = hover(event,tempCross)

                if hoverCross[0]:
                    setattr(self,f'save{n}DeleteButtonColor',(255,100,105))
                    survol = True
                    if hoverCross[1]:
                        self.commonVar.del_save(n+1)
                        self.commonVar.update_saving_var()
                        self.update_display()
                else:
                    setattr(self,f'save{n}DeleteButtonColor',(176,19,24))

                if hover(event,getattr(self,f'save{n}BgSurface').get_rect(topleft=coor))[0] and not hoverCross[0]:
                    setattr(self,f'save{n}BgColor',(50,50,50,220))
                    survol = True
                    if hover(event,getattr(self,f'save{n}BgSurface').get_rect(topleft=coor))[1]:
                        self.commonVar.update_saving_json()
                        CommonVar.commonDico['saveChosen'] = n+1
                        self.commonVar.update_saving_var()
                else:
                    setattr(self,f'save{n}BgColor',(0,0,0,120))
                

            if survol:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def update(self):
        for n in range(self.commonVar.nJson()):
            openSave = self.commonVar.openSave(n+1)
            setattr(self,f'save{n}Name',openSave['creatureId'][0])
            if openSave['creatureRoles'][0]:
                setattr(self,f'save{n}Role',openSave['creatureRoles'][0])
            else:
                setattr(self,f'save{n}Role','Aucun')
            setattr(self,f'save{n}Mates',str(len(openSave['creatureMates'][0])))
            setattr(self,f'save{n}Evilness',str(openSave['creatureEvilness'][0]))
            setattr(self,f'save{n}CreatureNumber',str(openSave['creatureNumber']))
            setattr(self,f'save{n}Cycle',str(openSave['cycle']))

            setattr(self,f'save{n}NameText',self.elementFont.render(getattr(self,f'save{n}Name'),True,(0,0,0)))
            setattr(self,f'save{n}RoleText',self.elementFont.render(getattr(self,f'save{n}Role'),True,(0,0,0)))
            setattr(self,f'save{n}MatesText',self.elementFont.render(getattr(self,f'save{n}Mates'),True,(0,0,0)))
            setattr(self,f'save{n}EvilnessText',self.elementFont.render(getattr(self,f'save{n}Evilness'),True,(0,0,0)))
            setattr(self,f'save{n}CreatureNumberText',self.elementFont.render(getattr(self,f'save{n}CreatureNumber'),True,(0,0,0)))
            setattr(self,f'save{n}CycleText',self.elementFont.render(getattr(self,f'save{n}Cycle'),True,(0,0,0)))

    def update_display(self): ##Tous les trucs à actualiser (collision,interractions automatiques) seront ici
        for n in range(self.commonVar.nJson()):
            openSave = self.commonVar.openSave(n+1)

            x = self.converter.conv_x(1800)
            y = self.converter.conv_y(175)
            setattr(self,f'save{n}BgSurface',pygame.Surface((x,y),pygame.SRCALPHA))
            setattr(self,f'save{n}BgColor',120)

            setattr(self,f'save{n}TitleText',self.namesFont.render(f'Sauvegarde {n+1}',True,(255,255,255)))
            setattr(self,f'save{n}TitleRect',getattr(self,f'save{n}TitleText').get_rect(topleft=(self.converter.conv_x(25),0)))

            setattr(self,f'save{n}Name',openSave['creatureId'][0])
            setattr(self,f'save{n}NameText',self.elementFont.render(getattr(self,f'save{n}Name'),True,(0,0,0)))
            setattr(self,f'save{n}NameTextRect',getattr(self,f'save{n}NameText').get_rect(topleft=(self.converter.conv_x(35),self.converter.conv_y(70))))
            setattr(self,f'save{n}NameBgRect',pygame.Rect(self.converter.conv_x(25),self.converter.conv_y(85),len(getattr(self,f'save{n}Name'))*self.converter.conv_x(25)+self.converter.conv_x(20),self.converter.conv_y(70)))
            
            if openSave['creatureRoles'][0]:
                setattr(self,f'save{n}Role',openSave['creatureRoles'][0])
            else:
                setattr(self,f'save{n}Role','Aucun')
            setattr(self,f'save{n}RoleText',self.elementFont.render(getattr(self,f'save{n}Role'),True,(0,0,0)))
            x = max(self.converter.conv_x(400),len(getattr(self,f'save{n}Name'))*self.converter.conv_x(27)+self.converter.conv_x(70))
            setattr(self,f'save{n}RoleTextRect',getattr(self,f'save{n}RoleText').get_rect(topleft=(x + self.converter.conv_x(15),self.converter.conv_y(70))))
            setattr(self,f'save{n}RoleBgRect',pygame.Rect(x,self.converter.conv_y(85),len(getattr(self,f'save{n}Role'))*self.converter.conv_x(25)+self.converter.conv_x(20),self.converter.conv_y(70)))
            setattr(self,f'save{n}RoleTitle',self.subtitleFont.render('Rôle',True,(255,255,255)))
            setattr(self,f'save{n}RoleTitleRect',getattr(self,f'save{n}RoleTitle').get_rect(center=(x + self.converter.conv_x(35),self.converter.conv_y(55))))

            setattr(self,f'save{n}Mates',str(len(openSave['creatureMates'][0])))
            setattr(self,f'save{n}MatesText',self.elementFont.render(getattr(self,f'save{n}Mates'),True,(0,0,0)))
            setattr(self,f'save{n}MatesTextRect',getattr(self,f'save{n}MatesText').get_rect(topleft=(self.converter.conv_x(825),self.converter.conv_y(70))))
            setattr(self,f'save{n}MatesBgRect',pygame.Rect(self.converter.conv_x(817),self.converter.conv_y(85),len(getattr(self,f'save{n}Mates'))*self.converter.conv_x(25)+self.converter.conv_x(20),self.converter.conv_y(70)))
            setattr(self,f'save{n}MatesTitle',self.subtitleFont.render('Proche(s)',True,(255,255,255)))
            setattr(self,f'save{n}MatesTitleRect',getattr(self,f'save{n}MatesTitle').get_rect(center=(self.converter.conv_x(850),self.converter.conv_y(55))))

            setattr(self,f'save{n}Evilness',str(openSave['creatureEvilness'][0]))
            setattr(self,f'save{n}EvilnessText',self.elementFont.render(getattr(self,f'save{n}Evilness'),True,(0,0,0)))
            setattr(self,f'save{n}EvilnessTextRect',getattr(self,f'save{n}EvilnessText').get_rect(topleft=(self.converter.conv_x(1075),self.converter.conv_y(70))))
            setattr(self,f'save{n}EvilnessBgRect',pygame.Rect(self.converter.conv_x(1067),self.converter.conv_y(85),len(getattr(self,f'save{n}Evilness'))*self.converter.conv_x(25)+self.converter.conv_x(20),self.converter.conv_y(70)))
            setattr(self,f'save{n}EvilnessTitle',self.subtitleFont.render('Niveau de mal',True,(255,255,255)))
            setattr(self,f'save{n}EvilnessTitleRect',getattr(self,f'save{n}EvilnessTitle').get_rect(center=(self.converter.conv_x(1100),self.converter.conv_y(55))))
            
            setattr(self,f'save{n}CreatureNumber',str(openSave['creatureNumber']))
            setattr(self,f'save{n}CreatureNumberText',self.elementFont.render(getattr(self,f'save{n}CreatureNumber'),True,(0,0,0)))
            setattr(self,f'save{n}CreatureNumberTextRect',getattr(self,f'save{n}CreatureNumberText').get_rect(topleft=(self.converter.conv_x(1425),self.converter.conv_y(70))))
            setattr(self,f'save{n}CreatureNumberBgRect',pygame.Rect(self.converter.conv_x(1417),self.converter.conv_y(85),len(getattr(self,f'save{n}CreatureNumber'))*self.converter.conv_x(25)+self.converter.conv_x(20),self.converter.conv_y(70)))
            setattr(self,f'save{n}CreatureNumberTitle',self.subtitleFont.render('Nombre de villageois',True,(255,255,255)))
            setattr(self,f'save{n}CreatureNumberTitleRect',getattr(self,f'save{n}CreatureNumberTitle').get_rect(center=(self.converter.conv_x(1450),self.converter.conv_y(55))))

            width = getattr(self,f'save{n}BgSurface').get_width()
            setattr(self,f'save{n}Cycle',str(openSave['cycle']))
            setattr(self,f'save{n}CycleText',self.elementFont.render(getattr(self,f'save{n}Cycle'),True,(0,0,0)))
            setattr(self,f'save{n}CycleTextRect',getattr(self,f'save{n}CycleText').get_rect(topleft=(width - (len(getattr(self,f'save{n}CreatureNumber'))*self.converter.conv_x(25)+self.converter.conv_x(30)),self.converter.conv_y(70))))
            setattr(self,f'save{n}CycleBgRect',pygame.Rect(width - (len(getattr(self,f'save{n}CreatureNumber'))*self.converter.conv_x(25)+self.converter.conv_x(40)),self.converter.conv_y(85),len(getattr(self,f'save{n}Cycle'))*self.converter.conv_x(25)+self.converter.conv_x(20),self.converter.conv_y(70)))
            setattr(self,f'save{n}CycleTitle',self.elementFont.render('Cycle',True,(255,255,255)))
            setattr(self,f'save{n}CycleTitleRect',getattr(self,f'save{n}CycleTitle').get_rect(topright=(width - (len(getattr(self,f'save{n}CreatureNumber'))*self.converter.conv_x(25)+self.converter.conv_x(40)),self.converter.conv_y(70))))

            setattr(self,f'save{n}DeleteButtonRect',pygame.Rect(width-self.converter.conv_x(70),self.converter.conv_y(20),self.converter.conv_x(50),self.converter.conv_y(50)))
            setattr(self,f'save{n}DeleteButtonColor',(255,100,105))

    def display(self): ##Toutes les fonctions pygame pour afficher seront ici
        self.screen.fill((0,0,0))
        self.background.display()

        ## Affichage des sauvegardes
        for n in range(self.commonVar.nJson()):
            x = self.screen.get_width()/2-self.converter.conv_x(900)
            y = self.converter.conv_y(190)*n + self.screen.get_height()*(0.25)
            surface = getattr(self,f'save{n}BgSurface')
            self.screen.blit(getattr(self,f'save{n}BgSurface'),(x,y))
            pygame.draw.rect(getattr(self,f'save{n}BgSurface'),getattr(self,f'save{n}BgColor'),(0,0,self.converter.conv_x(1800),self.converter.conv_y(175)),border_radius=self.converter.conv_y(30))
            if CommonVar.commonDico['saveChosen'] == n+1:
                pygame.draw.rect(getattr(self,f'save{n}BgSurface'),(0,0,200,255),(0,0,self.converter.conv_x(1800),self.converter.conv_y(175)),border_radius=self.converter.conv_y(30),width=5)
            pygame.draw.rect(surface,(179,179,179),getattr(self,f'save{n}NameBgRect'),border_radius=15)
            surface.blit(getattr(self,f'save{n}NameText'),getattr(self,f'save{n}NameTextRect'))
            pygame.draw.rect(surface,(179,179,179),getattr(self,f'save{n}RoleBgRect'),border_radius=15)
            surface.blit(getattr(self,f'save{n}RoleText'),getattr(self,f'save{n}RoleTextRect'))
            surface.blit(getattr(self,f'save{n}RoleTitle'),getattr(self,f'save{n}RoleTitleRect'))
            pygame.draw.rect(surface,(179,179,179),getattr(self,f'save{n}MatesBgRect'),border_radius=15)
            surface.blit(getattr(self,f'save{n}MatesText'),getattr(self,f'save{n}MatesTextRect'))
            surface.blit(getattr(self,f'save{n}MatesTitle'),getattr(self,f'save{n}MatesTitleRect'))
            pygame.draw.rect(surface,(179,179,179),getattr(self,f'save{n}EvilnessBgRect'),border_radius=15)
            surface.blit(getattr(self,f'save{n}EvilnessText'),getattr(self,f'save{n}EvilnessTextRect'))
            surface.blit(getattr(self,f'save{n}EvilnessTitle'),getattr(self,f'save{n}EvilnessTitleRect'))
            pygame.draw.rect(surface,(179,179,179),getattr(self,f'save{n}CreatureNumberBgRect'),border_radius=15)
            surface.blit(getattr(self,f'save{n}CreatureNumberText'),getattr(self,f'save{n}CreatureNumberTextRect'))
            surface.blit(getattr(self,f'save{n}CreatureNumberTitle'),getattr(self,f'save{n}CreatureNumberTitleRect'))
            pygame.draw.rect(surface,(179,179,179),getattr(self,f'save{n}CycleBgRect'),border_radius=15)
            surface.blit(getattr(self,f'save{n}CycleText'),getattr(self,f'save{n}CycleTextRect'))
            surface.blit(getattr(self,f'save{n}CycleTitle'),getattr(self,f'save{n}CycleTitleRect'))
            surface.blit(getattr(self,f'save{n}TitleText'),getattr(self,f'save{n}TitleRect'))
            pygame.draw.rect(surface,getattr(self,f'save{n}DeleteButtonColor'),getattr(self,f'save{n}DeleteButtonRect'),border_radius=13)
            pygame.draw.line(surface,(255,255,255),(getattr(self,f'save{n}DeleteButtonRect')[0]+13,getattr(self,f'save{n}DeleteButtonRect')[1]+13),(getattr(self,f'save{n}DeleteButtonRect')[0]+37,getattr(self,f'save{n}DeleteButtonRect')[1]+37),7)
            pygame.draw.line(surface,(255,255,255),(getattr(self,f'save{n}DeleteButtonRect')[0]+37,getattr(self,f'save{n}DeleteButtonRect')[1]+13),(getattr(self,f'save{n}DeleteButtonRect')[0]+13,getattr(self,f'save{n}DeleteButtonRect')[1]+37),7)

        ## Affiche du bouton d'ajout de sauvegardes
        if self.commonVar.nJson() < 3:
            self.screen.blit(self.newSaveButtonSurface,(self.screen.get_width()/2 - self.converter.conv_x(322),self.converter.conv_y(270) + self.converter.conv_y(190)*(n+1)))
            pygame.draw.rect(self.newSaveButtonSurface,self.newSaveButtonColor,(0,0,self.converter.conv_y(644),self.converter.conv_y(175)),border_radius=self.converter.conv_y(30))
            pygame.draw.line(self.newSaveButtonSurface,self.newSaveButtonPlusColor,(292,175/2),(352,175/2),8)
            pygame.draw.line(self.newSaveButtonSurface,self.newSaveButtonPlusColor,(322,(175/2)-30),(322,(175/2)+30),8)

        ## Affichage de l'icon de menu
        self.screen.blit(self.homeIconBgSurface, (self.converter.conv_x(50),self.screen.get_height() - self.converter.conv_y(250)))
        pygame.draw.circle(self.homeIconBgSurface, (0, 0, 0, self.homeIconBgAlpha), (self.converter.conv_x(100),self.converter.conv_y(100)), self.converter.conv_y(70))
        self.screen.blit(self.homeIconImage,(100,self.screen.get_height() - 200))

        ## Affichage du titre et son fond
        pygame.draw.rect(self.menuTitleBgSurface,(0,0,0,120),(0,0,self.screen.get_width(),self.converter.conv_y(250)))
        self.screen.blit(self.menuTitleBgSurface,(0,0))
        self.screen.blit(self.menuTitleText, self.menuTitleRect)

        pygame.display.flip() ##Actualiser

    def run(self):
        while self.running:
            self.handling_event()
            self.display()