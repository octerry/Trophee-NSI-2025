import pygame
from SpriteBank import logo

class Menus:
    def __init__(self,screen):
        self.screen = screen
        self.running = True

        self.clock = pygame.time.Clock()

        self.init_bg()

    def handling_event(self): # Gérer toutes les actions que le joueur fait
        for event in pygame.event.get(): ## pygame.event.get() -> liste des évènements en cours
            if event.type == pygame.QUIT: ## Si le joueur appuie sur la croix de la fenetre
                pygame.quit() ## Le jeu s'arrete

    def update(self):
        self.update_bg()

    def display(self):
        self.draw_bg()

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_event()
            self.update()
            self.display()
            self.clock.tick(60)
            print(self.clock.get_fps())

    def init_bg(self):
        self.logoBgSurface = pygame.Surface((self.screen.get_width(), self.screen.get_height()),pygame.SRCALPHA) ## Créer une surface pour ajouter de la transparence aux logos
        self.logoBg = logo["Fond"] ## Récupérer le sprite des logos de fond
        self.logoBg = pygame.transform.scale(self.logoBg,(946*1.3, 128*1.3)) ## Grandir les logos de 1,3
        self.logoBg = pygame.transform.rotate(self.logoBg,-45)
        self.logoBg.set_alpha(25) ## Mettre les sprites transparents
        
        ## Créer les cadres du sprite pour les positionner
        self.n_lines = 2

        self.logoBgRectTabA = [
            ## Le cadre du sprite( potion du point haut-droite -> ( x_précalculé, y_qui_s_adapte ) ) , y_qui_s_adapte
            [ self.logoBg.get_rect( topleft= ( 870*2 , -( self.screen.get_width() - 870*2 ) ) ) , -( self.screen.get_width() + 870 ) ] ,
            [ self.logoBg.get_rect( topleft= ( 870 , -( self.screen.get_width() - 870 ) ) ) , -( self.screen.get_width() + 870 ) ] ,
            [ self.logoBg.get_rect( topleft= ( 0 , -( self.screen.get_width() + 0 ) ) ) , -( self.screen.get_width() + 870 ) ] ,
            [ self.logoBg.get_rect( topleft= ( -870 , -( self.screen.get_width() + 870 ) ) ) , -( self.screen.get_width() + 870 ) ] ,
        ]
        
        self.logoBgRectTabB = [ 
            ## Le cadre du sprite( potion du point haut-droite -> ( x_précalculé, y_qui_s_adapte ) ) , y_qui_s_adapte
            [ self.logoBg.get_rect( topleft= ( 870*2 , -( self.screen.get_width() - 870*2 ) + 300 ) ) , -( self.screen.get_width() + 870 ) + 300 ] ,
            [ self.logoBg.get_rect( topleft= ( 870 , -( self.screen.get_width() - 870 ) + 300 ) ) , -( self.screen.get_width() + 870 ) + 300 ] ,
            [ self.logoBg.get_rect( topleft= ( 0 , -( self.screen.get_width() + 0 ) + 300  ) ) , -( self.screen.get_width() + 870 ) + 300 ] ,
            [ self.logoBg.get_rect( topleft= ( -870 , -( self.screen.get_width() + 870 ) + 300 ) ) , -( self.screen.get_width() + 870 ) + 300 ] ,
        ]

    def update_bg(self):
        prec = self.logoBgRectTabA[-1][0] ## Element précédent
        for i in range(len(self.logoBgRectTabA)): ## Chaque sprite sur la ligne
            logoBgRect = self.logoBgRectTabA[i]
            if logoBgRect[0].bottomleft[0] <= self.screen.get_width(): ## Tant que les logos ne sortent pas de l'écran
                if prec.bottomleft[0] >= -92 or logoBgRect[0].bottomleft[0] > 0: ## Bouger seulement si le précédent est affiché sur l'écran
                    self.logoBgRectTabA[i][0].move_ip(1, 1) ## On fait glisser les logos
            else:
                self.logoBgRectTabA[i][0].update((-870, self.logoBgRectTabA[i][1], logoBgRect[0].width, logoBgRect[0].height)) ## Sinon on les remets tout à gauche
            prec = logoBgRect[0]

        prec = self.logoBgRectTabB[-1][0] ## Element précédent [ligne][element][type (0 -> cadre)]
        for i in range(len(self.logoBgRectTabB)): ## Chaque sprite sur la ligne
            logoBgRect = self.logoBgRectTabB[i]
            if logoBgRect[0].bottomleft[0] <= self.screen.get_width(): ## Tant que les logos ne sortent pas de l'écran
                if prec.bottomleft[0] >= -92 or logoBgRect[0].bottomleft[0] > 0: ## Bouger seulement si le précédent est affiché sur l'écran
                    self.logoBgRectTabB[i][0].move_ip(-1, -1) ## On fait glisser les logos
            else:
                coor = (self.screen.get_width() + 870, self.logoBgRectTabB[i][1])
                logoBgRect.update((coor[0], coor[1], logoBgRect[0].width, logoBgRect[0].height)) ## Sinon on les remets tout à gauche
            prec = logoBgRect[0]

    def draw_bg(self):
        self.draw_gradient_background(self.screen)

        for logoBgRect in self.logoBgRectTabA:
            for i in range(self.n_lines):
                rect = logoBgRect[0]
                temp_rect = [rect[0], rect[1] + 600*i, rect[2], rect[3]]
                self.screen.blit(self.logoBg, temp_rect)

        
        for logoBgRect in self.logoBgRectTabB:
            for i in range(self.n_lines):
                rect = logoBgRect[0]
                temp_rect = [rect[0], rect[1] + 600*i, rect[2], rect[3]]
                self.screen.blit(self.logoBg, temp_rect)

    def draw_gradient_background(self,surface):
        height = surface.get_height()
        
        # On dessine ligne par ligne chaque couleur du dégradé
        for y in range(height):
            
            ratio = y / height ## Ratio d'avancement par rapport à la hauteur (0 -> haut / 1 -> bas)

            color1 = [2,51,126]
            color2 = [1,105,193]

            r = color1[0] + (color2[0] - color1[0]) * ratio
            g = color1[1] + (color2[1] - color1[1]) * ratio
            b = color1[2] + (color2[2] - color1[2]) * ratio

            ## On dessine la ligne à partir de la gauche (0,y) jusqu'à la droite (width, y)
            pygame.draw.line(surface, (int(r), int(g), int(b)), (0,y), (surface.get_width(), y))