import pygame

from useful_functions import *

seed_image = pygame.image.load("Items\seed.png")
seed_image = pygame.transform.scale(seed_image, (80, 80))


def create_seed_image(colour):
    seed_final = seed_image.copy()
    seed_coloured = pygame.Surface(seed_image.get_size())
    seed_coloured.fill(colour)
    seed_final.blit(seed_coloured, (0, 0), special_flags=pygame.BLEND_MULT)

    return seed_final