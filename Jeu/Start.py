import pygame
from pathlib import Path

class Window:
    def __init__ (self,screen):
        self.screen = screen ##Avoir les informations sur l'écran (taille) 
        self.running = True ##Pour le couper quand on veut
        directory = Path(__file__).parent ##Chemin d'accès vers le programme

        # Setup le titre de la fenetre
        pygame.display.set_caption("Nox Villae")

        # Setup l'icon de la fenetre
        iconSprite = f'{directory}/Ressource/icon.ico'
        icon = pygame.image.load(iconSprite)
        pygame.display.set_icon(icon)

        self.clock = pygame.time.Clock()

        self.loading()

    def handling_event(self): ##Tous les évenements (joueur -> jeu) seront ici
        for event in pygame.event.get():
            if event.type == pygame.QUIT: ##Si le joueur appuie sur la croix de la fenetre
                self.running = False ##Le jeu s'arrete

    def update(self): ##Tous les trucs à actualiser (colition,interractions automatiques) seront ici'
        pass

    def display(self): ##Toutes les fonctions pygame pour afficher seront ici
        self.screen.fill((16,24,36))

        self.screen.blit(self.gameTitleText, self.gameTitleRect)
        self.screen.blit(self.percentage, self.percentageRect)
        self.screen.blit(self.underText, self.underTextRect)
        pygame.draw.rect(self.screen,(31,42,59),self.loadingBack,border_radius=5)
        pygame.draw.rect(self.screen,(85,127,135),self.loadingLine,border_top_left_radius=5,border_bottom_left_radius=5)

        pygame.display.flip() ##Actualiser

    def run(self):
        while self.running:
            self.handling_event()
            self.menus.run()
            self.game.run(self) 
            self.display()
            self.clock.tick(30)

    def loading(self):
        from Converter import Converter
        self.converter = Converter(screen)

        self.gameTitleFont = pygame.font.Font(None, self.converter.conv_y(250))
        self.gameTitleText = self.gameTitleFont.render("Nox Villae",True,(255,255,255))
        self.gameTitleRect = self.gameTitleText.get_rect(center=(self.screen.get_width()/2,self.screen.get_height()/2 - self.converter.conv_y(190)))

        underFont = pygame.font.Font(None, self.converter.conv_y(50))
        self.underText = underFont.render("Définition des rôles",True,(255,255,255))
        self.underTextRect = self.underText.get_rect(center = (self.screen.get_width()/2, self.converter.conv_y(700)))

        progress = 0.17

        self.loadingBack = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(1265),self.converter.conv_y(45))
 
        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))

        self.display()

        #RoleDefinition
        import RoleDefinition

        progress = 1/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))
        
        self.underText = underFont.render("Récupération des données enregistrées",True,(255,255,255))
        self.underTextRect = self.underText.get_rect(center = (self.screen.get_width()/2, self.converter.conv_y(700)))

        self.display()

        #CommonVar
        import CommonVar

        progress = 2/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))

        self.underText = underFont.render("Initialisation des fonctions secondaires",True,(255,255,255))
        self.underTextRect = self.underText.get_rect(center = (self.screen.get_width()/2, self.converter.conv_y(700)))

        self.display()

        #Font
        import Font

        progress = 3/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))


        self.display()

        #Keybinds
        import Keybinds

        progress = 4/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))

        self.display()

        #Converter
        import Converter

        progress = 5/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))

        self.display()

        #CommonFonction
        import CommonFonction

        progress = 6/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))

        self.display()

        #SaveMenu
        import SaveMenu

        progress = 7/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))

        self.display()

        #KeybindingMenu
        import KeybindingMenu

        progress = 8/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))

        self.display()

        #GeneralSettingsMenu
        import GeneralSettingsMenu

        progress = 9/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))

        self.display()

        #SettingsMenu
        import SettingsMenu

        progress = 10/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))

        self.display()

        #ShowDataMenu
        import ShowDataMenu

        progress = 11/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))

        self.underText = underFont.render("Compilation des ressources",True,(255,255,255))
        self.underTextRect = self.underText.get_rect(center = (self.screen.get_width()/2, self.converter.conv_y(700)))

        self.display()

        #SpriteBank
        import SpriteBank

        progress = 12/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))
        
        self.underText = underFont.render("Initialisation des fonctions secondaires",True,(255,255,255))
        self.underTextRect = self.underText.get_rect(center = (self.screen.get_width()/2, self.converter.conv_y(700)))

        self.display()

        #BackgroundRandomSimulation
        import BackgroundRandomSimulation

        progress = 13/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))

        self.display()

        from Menus import Menus # -------------

        progress = 14/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))

        self.display()

        #FloatingMenu
        import FloatingMenu

        progress = 15/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))

        self.underText = underFont.render("Initialisation des bots",True,(255,255,255))
        self.underTextRect = self.underText.get_rect(center = (self.screen.get_width()/2, self.converter.conv_y(700)))

        self.display()

        #Choose
        import Choose

        progress = 16/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))

        self.underText = underFont.render("Initialisation des fonctions secondaires",True,(255,255,255))
        self.underTextRect = self.underText.get_rect(center = (self.screen.get_width()/2, self.converter.conv_y(700)))

        self.display()

        #NightAction
        import NightAction

        progress = 17/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))

        self.display()

        #WitchChoice
        import WitchChoice

        progress = 18/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))

        self.display()

        #ClairvoyantReveal
        import ClairvoyantReveal

        progress = 19/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))

        self.display()

        #PyromaniacChoice
        import PyromaniacChoice

        progress = 20/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))

        self.display()

        #Vote
        import Vote

        progress = 21/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))

        self.display()

        from Game import Game # -------------

        progress = 22/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))

        self.underText = underFont.render("Démarrage",True,(255,255,255))
        self.underTextRect = self.underText.get_rect(center = (self.screen.get_width()/2, self.converter.conv_y(700)))

        self.display()

        self.menus = Menus(self.screen,self) # -------------

        progress = 23/24

        self.loadingLine = pygame.rect.Rect(self.converter.conv_x(328),self.converter.conv_y(635),self.converter.conv_x(progress * 1265),self.converter.conv_y(45))

        self.percentage = pygame.font.Font(None, self.converter.conv_y(65)).render(f'{int(progress*100)}%',True,(255,255,255))
        self.percentageRect = self.percentage.get_rect(topright = ((self.converter.conv_x(328),self.converter.conv_y(635))))

        self.display()

        self.game = Game(self.screen) # -------------

pygame.init()
# AJOUTER pygame.FULLSCREEN QUAND ON AURA FINI DE CODER
screen = pygame.display.set_mode((0,0)) ##Définir un écran ((0,0) c'est pour dire plein écran et pygame.FULLSCREEN pour être considéré comme plein écran par Windows)
game = Window(screen) ##Appeller la classe
game.run() ##Lancer le jeu


from CommonVar import CommonVar
commonVar = CommonVar()

commonVar.update_saving_json()
pygame.quit()