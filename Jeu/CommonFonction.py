import pygame
import math
from Start import Window

def hover(event,rect): 
        mouse_pos = pygame.mouse.get_pos()
        if rect.collidepoint(mouse_pos): # Quand le rect rentre en "collision" avec la souris
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return True,True # Touche : True , Clique : True
            return True,False # Touche : True , Clique : False
        else:
            return False,False # Touche : False
        
def create_radial_vignette(size, multiplicator = 10):
    width, height = size
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    center_x, center_y = width // 2, height // 2
    max_distance = math.hypot(center_x, center_y) * (multiplicator*0.05 + 0.5)

    for y in range(height):
        for x in range(width):
            dx = x - center_x
            dy = y - center_y
            distance = math.hypot(dx, dy)

            alpha = min(255, max(0, int((distance / max_distance) * 200)))

            surface.set_at((x, y), (0, 0, 0, alpha))

    return surface

def fade_in(classe,tick:int,window=None):
    while classe.fadeColor[3] > 0:
        classe.fadeColor[3] -= math.log(classe.fadeColor[3]* (50*tick))
        if classe.fadeColor[3] >= 0:
            for event in pygame.event.get():
                classe.handling_event(event)
            classe.update()
            classe.display()
            classe.clock.tick(tick)
        else:
            classe.fadeColor[3] = 0

    classe.running = True
    try:
        if window: 
            classe.run(window)
        else:
            classe.run()
    except TypeError: 
        pass

def fade_out(classe,tick:int):
    while classe.fadeColor[3] < 255:
        classe.fadeColor[3] += math.exp(classe.fadeColor[3]/ tick)
        if classe.fadeColor[3] <= 255:
            for event in pygame.event.get():
                classe.handling_event(event)
            classe.update()
            classe.display()
            classe.clock.tick(tick)
        else:
            classe.fadeColor[3] = 255
            classe.display()

    classe.running = False