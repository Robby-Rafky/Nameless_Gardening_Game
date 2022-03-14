from garden import *

running = True
coord = [0, 0]
test_colour = (255,255,255)
background_colour = (40, 87, 23)
(width, height) = (1920, 1080)
game_space = pygame.display.set_mode((width, height))
pygame.display.set_caption('Test')
game_space.fill(background_colour)
base_garden = GardenSpace(game_space, 5, 5)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game_space.fill(background_colour)

    coord = pygame.mouse.get_pos()
    pygame.draw.rect(game_space, (255, 0, 0), (coord[0]-25, coord[1]-25, 50, 50), 2)
    base_garden.draw_base_garden()

    pygame.display.update()