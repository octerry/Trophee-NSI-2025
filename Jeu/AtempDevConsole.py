import pygame
import math

def create_radial_vignette(size):
    width, height = size
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    center_x, center_y = width // 2, height // 2
    max_distance = math.hypot(center_x, center_y) * 0.75

    for y in range(height):
        for x in range(width):
            # Distance entre le point et le centre
            dx = x - center_x
            dy = y - center_y
            distance = math.hypot(dx, dy)

            # Calcul alpha : plus proche du bord => plus opaque
            alpha = min(255, max(0, int((distance / max_distance) * 200)))

            surface.set_at((x, y), (0, 0, 0, alpha))

    return surface

# Exemple de boucle pygame avec vignette
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

vignette = create_radial_vignette((800, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Exemple de fond clair
    screen.blit(vignette, (0, 0))  # Superposer le calque vignette

    pygame.display.flip()
    clock.tick(60)

pygame.quit()