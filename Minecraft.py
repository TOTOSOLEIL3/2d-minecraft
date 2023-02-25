import pygame

# Initialiser Pygame
pygame.init()

# Définir les couleurs
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BROWN = (153, 76, 0)
GRAY = (192, 192, 192)

# Définir les dimensions du monde
TILE_SIZE = 50
MAP_WIDTH = 20
MAP_HEIGHT = 15

# Créer la fenêtre
width = TILE_SIZE * MAP_WIDTH
height = TILE_SIZE * MAP_HEIGHT
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Minecraft en 2D")

# Créer la carte du monde
world_map = [
    [GRAY] * MAP_WIDTH for _ in range(MAP_HEIGHT)
]

# Ajouter des arbres
world_map[3][2] = BROWN
world_map[3][3] = GREEN
world_map[3][4] = GREEN
world_map[2][3] = GREEN
world_map[4][3] = GREEN

# Boucle principale du jeu
running = True
while running:
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Dessiner le monde
    for row in range(MAP_HEIGHT):
        for column in range(MAP_WIDTH):
            pygame.draw.rect(screen, world_map[row][column], 
                             [column * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE])
    
    # Rafraîchir l'affichage
    pygame.display.update()

# Quitter Pygame
pygame.quit()
