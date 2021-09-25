import os
import pygame
import time
import random

# initialize fonts so pygame can display text
pygame.font.init()

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
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0, 0))
        # render text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10)) # top left corner offset by 10
        # subtracting the label width ensures that theres enough space to hold label text
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
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