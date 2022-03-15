import pygame

from garden import *

running = True
# very WIP
garden_offset = [150, 100]
garden_size = [16, 8]
tile_size = 100
garden_contents = [[0 for ix in range(garden_size[0])] for iy in range(garden_size[1])]

background_colour = (40, 87, 23)
(width, height) = (1920, 1080)

game_space = pygame.display.set_mode((width, height))
pygame.display.set_caption('Test')


base_garden = GardenSpace(game_space, garden_size, garden_offset, tile_size)

while running:
    game_space.fill(GREEN)

    base_garden.draw_base_garden()
    plot_clicked = base_garden.draw_overlay_garden(pygame.mouse.get_pos())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            if event.type == pygame.MOUSEBUTTONUP:
                try:
                    garden_contents[plot_clicked[1]][plot_clicked[0]] += 1
                except Exception:
                    pass

    base_garden.test_overlay(garden_contents)




    # test stuff


    pygame.display.update()

for squad in garden_contents:
    print(squad)
