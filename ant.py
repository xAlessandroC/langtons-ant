import os
import math
import pygame
import random

# Game variables
FPS = os.getenv("FPS", 120)
WIDTH = os.getenv("WIDTH", 1280)
HEIGHT = os.getenv("HEIGHT", 720)
RESOLUTION = os.getenv("RESOLUTION", 5)

REAL_WIDTH = math.floor(WIDTH / RESOLUTION)
REAL_HEIGHT = math.floor(HEIGHT / RESOLUTION)

# App variables
START_POS = (math.floor(REAL_WIDTH / 2), math.floor(REAL_HEIGHT / 2))
DIRECTIONS = ["N", "E", "S", "W"]
FACING = 0
RULE = os.getenv("RULE", "LR")
CELL_STATE = [[0 for _ in range(REAL_WIDTH)] for _ in range(REAL_HEIGHT)]

# Pygame variables
screen = None
clock = None
font = None

def setCell(x, y, color):
    pygame.draw.rect(screen, color, (x * RESOLUTION, y * RESOLUTION, RESOLUTION, RESOLUTION))
    # pygame.draw.rect(screen, "black", (x * RESOLUTION, y * RESOLUTION, RESOLUTION, RESOLUTION), 1)


def switchRight(facing):
    return (facing + 1) % 4


def switchLeft(facing):
    return (facing - 1) % 4


def goAheadByDirection(pos, facing):
    new_x = pos[0]
    new_y = pos[1]
    if DIRECTIONS[facing] == "N":
        new_y -= 1
    elif DIRECTIONS[facing] == "E":
        new_x += 1
    elif DIRECTIONS[facing] == "S":
        new_y += 1
    elif DIRECTIONS[facing] == "W":
        new_x -= 1

    new_x = new_x % REAL_WIDTH
    new_y = new_y % REAL_HEIGHT

    return (new_x, new_y)


if __name__ == "__main__":

    print("Settings:")
    print(f"# FPS: {FPS}")
    print(f"# WIDTH: {WIDTH}")
    print(f"# HEIGHT: {HEIGHT}")
    print(f"# RESOLUTION: {RESOLUTION}")
    print(f"# REAL_WIDTH: {REAL_WIDTH}")
    print(f"# REAL_HEIGHT: {REAL_HEIGHT}")

    # Init engine
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Monospace', 15)

    current_pos = START_POS
    step = 0
    formatted_rule = [*RULE]
    colors = ["white", "black"]
    for i in range(len(formatted_rule) - 2):
        colors.append(pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    running = True
    while running:
        # Poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game logic
        rule_idx = CELL_STATE[current_pos[1]][current_pos[0]]
        if formatted_rule[rule_idx] == "R":
            CELL_STATE[current_pos[1]][current_pos[0]] = (rule_idx + 1) % (len(formatted_rule))
            FACING = switchRight(FACING)
            current_pos = goAheadByDirection(current_pos, FACING)
        elif formatted_rule[rule_idx] == "L":
            CELL_STATE[current_pos[1]][current_pos[0]] = (rule_idx + 1) % (len(formatted_rule))
            FACING = switchLeft(FACING)
            current_pos = goAheadByDirection(current_pos, FACING)


        # Render screen
        step += 1
        screen.fill("white")
        for y in range(REAL_HEIGHT):
            for x in range(REAL_WIDTH):
                if CELL_STATE[y][x] != 0:
                    setCell(x, y, colors[CELL_STATE[y][x]])
        screen.blit(font.render("Step: {}".format(step), False, (0, 0, 0)), (0,0))
        screen.blit(font.render("Rule: {}".format(RULE), False, (0, 0, 0)), (0,15))

        # Update screen
        pygame.display.flip()
        # clock.tick(120)

    pygame.quit()