import pygame

import Font
from Keybinds import keybinds
from Converter import Converter
from CommonFonction import hover

class KeybindingMenu:
    def __init__(self,screen):
        self.screen = screen
        self.converter = Converter(self.screen)

        self.keybindFont = pygame.font.Font(Font.jaini, self.converter.conv_y(40))
        self.keybindBgSurface = pygame.Surface(self.screen.get_size(),pygame.SRCALPHA)

        self.rep = [['Avancer :',0,'up',0], ## Nom affiché, position verticale, nom de code, à droite
                    ['Reculer :',1,'down',0],
                    ['Droite :',2,'right',0],
                    ['Gauche :',3,'left',0],
                    ['Interragir :',5,'interract',0],

                    ['Écourter la journée :',0,'skipJourney',1],
                    ['Mode spéctateur :',1,'spectatorMode',1],
                    ['Centrer la caméra :',2,'centerCamera',1],
                    ['Ouvrir les menus :',4,'openMenu',1]]
        
        for el in self.rep:
            semiScreen = self.screen.get_width()/2
            setattr(self,f'{el[2]}Text',self.keybindFont.render(el[0],True,(255,255,255)))
            setattr(self,f'{el[2]}Rect',getattr(self,f'{el[2]}Text').get_rect(topleft=(self.converter.conv_x(100 + semiScreen*el[3]),self.converter.conv_y(420 + el[1]*50))))

            temp = keybinds[el[2]]
            temp = pygame.key.name(temp).capitalize()
            keybindLeft = self.converter.conv_x(300) + (semiScreen+self.converter.conv_x(100))*el[3]
            keybindTop = self.converter.conv_y(420 + el[1]*50)
            setattr(self,f'keybind{el[2]}Text',self.keybindFont.render(temp,True,(180,180,255)))
            setattr(self,f'keybind{el[2]}Rect',getattr(self,f'keybind{el[2]}Text').get_rect(topleft=(keybindLeft,keybindTop)))
            setattr(self,f'keybind{el[2]}BgRect',pygame.Rect(keybindLeft-self.converter.conv_x(10),keybindTop+self.converter.conv_y(10),getattr(self,f'keybind{el[2]}Rect').width+self.converter.conv_x(20),self.converter.conv_y(40)))
            setattr(self,f'keybind{el[2]}BgColor',(0,0,0,170))

    def keybinding(self,el,settingsMenu):
        temp = keybinds[el[2]]
        temp = pygame.key.name(temp).capitalize()
        setattr(self,f'keybind{el[2]}Text',self.keybindFont.render(temp,True,(180,180,255)))
        setattr(self,f'keybind{el[2]}BgColor',(180,180,255,255))

        pressed = False
        while not pressed:
            settingsMenu.display()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    keybinds[el[2]] = event.key
                    pressed = True

    def handling_event(self,survol,event,settingsMenu):
        for el in self.rep:
            temp = pygame.key.name(keybinds[el[2]]).capitalize()
            if hover(event, getattr(self,f'keybind{el[2]}BgRect'))[0]:
                setattr(self,f'keybind{el[2]}BgColor',(0,0,0,255))
                setattr(self,f'keybind{el[2]}Text',self.keybindFont.render(temp,True,(50,50,255)))
                survol = True
                if hover(event, getattr(self,f'keybind{el[2]}BgRect'))[1]:
                    self.keybinding(el,settingsMenu)
            else:
                setattr(self,f'keybind{el[2]}BgColor',(0,0,0,170))
                setattr(self,f'keybind{el[2]}Text',self.keybindFont.render(temp,True,(180,180,255)))

        return survol

    def update(self):
        for el in self.rep:
            semiScreen = self.screen.get_width()/2
            temp = keybinds[el[2]]
            temp = pygame.key.name(temp).capitalize()
            keybindLeft = self.converter.conv_x(300) + (semiScreen+self.converter.conv_x(100))*el[3]
            keybindTop = self.converter.conv_y(420 + el[1]*50)
            setattr(self,f'keybind{el[2]}Rect',getattr(self,f'keybind{el[2]}Text').get_rect(topleft=(keybindLeft,keybindTop)))
            setattr(self,f'keybind{el[2]}BgRect',pygame.Rect(keybindLeft-self.converter.conv_x(10),keybindTop+self.converter.conv_y(10),getattr(self,f'keybind{el[2]}Rect').width+self.converter.conv_x(20),self.converter.conv_y(40)))

    def display(self):
        ## Affichage des textes de keybind
        self.screen.blit(self.keybindBgSurface,(0,0))
        self.keybindBgSurface.fill((255,255,255,0))
        for el in self.rep:
            text = getattr(self,f'{el[2]}Text')
            rect = getattr(self,f'{el[2]}Rect')
            keybindText = getattr(self,f'keybind{el[2]}Text')
            keybindRect = getattr(self,f'keybind{el[2]}Rect')
            self.screen.blit(keybindText,keybindRect)
            self.screen.blit(text,rect)
            pygame.draw.rect(self.keybindBgSurface,(getattr(self,f'keybind{el[2]}BgColor')),getattr(self,f'keybind{el[2]}BgRect'),border_radius=self.converter.conv_y(10))