#from TestUI import *
import pygame.time

from garden import *
from button import *

# very WIP
garden_offset = (150, 100)
garden_size = (16, 8)
tile_size = 100
garden_contents = [[0 for ix in range(garden_size[0])] for iy in range(garden_size[1])]
clock = pygame.time.Clock()

background_colour = (40, 87, 23)
width, height = (1920, 1080)

game_space = pygame.display.set_mode((width, height))
pygame.display.set_caption('Test')

base_garden = GardenSpace(game_space, garden_size, garden_offset, tile_size)

testbutton = Button("beans", (10, 10), (100, 100), 20, GREY, "wtf")


def screen_layering(mouse_coordinates):
    game_space.fill(GREEN)

    base_garden.draw_base_garden()
    base_garden.test_overlay(garden_contents)

    testbutton.pack_button(game_space)


def game_loop(running):
    while running:
        mouse_coordinates = pygame.mouse.get_pos()

        screen_layering(mouse_coordinates)

        plot_clicked = base_garden.draw_overlay_garden(mouse_coordinates)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            else:
                if event.type == pygame.MOUSEBUTTONUP:
                    # lazy solution
                    try:
                        garden_contents[plot_clicked[1]][plot_clicked[0]] += 1
                    except Exception:
                        pass

                if testbutton.button_event_check(event, mouse_coordinates):
                    testbutton.update_button(testbutton.clicked_text)

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()


game_loop(True)

for squad in garden_contents:
    print(squad)
