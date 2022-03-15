import pygame

from garden import *

running = True
# very WIP
coord = [0, 0]
garden_offset = [150, 100]
tile_size = 100

test_colour = (255,255,255)
background_colour = (40, 87, 23)

(width, height) = (1920, 1080)

game_space = pygame.display.set_mode((width, height))
pygame.display.set_caption('Test')
game_space.fill(background_colour)

base_garden = GardenSpace(game_space, 5, 5, garden_offset, tile_size)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:

    game_space.fill(background_colour)

    base_garden.draw_base_garden()
    base_garden.draw_overlay_garden(pygame.mouse.get_pos())
    # test stuff
    coord = pygame.mouse.get_pos()

    pygame.display.update()