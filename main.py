import os
import pygame
import time
import random

# create pygame constants
WIDTH, HEIGHT = 750, 750
# pygame window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# converts images into pygame surfaces
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
# player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# load then scale the background to match window size
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))


def main():
    run = True
    fps = 60
    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0, 0))
        pygame.display.update()

    while run:
        clock.tick(fps)
        redraw_window()

        # check for event
        for event in pygame.event.get():
            # check if player has quit
            if event.type == pygame.QUIT:
                run = False

main()