# a simple dice rolling game

import random
import pygame

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Dice Racers")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# main game loop state
running = True
dice = [2, 4, 5, 6]


def draw_dice(side, x, y):

    dot_size = 4

    # draw the dice box outline
    pygame.draw.rect(screen, (0, 0, 0), (x - 20, y - 20, 40, 40), 2)

    # draw the dots
    if side == 1:
        pygame.draw.circle(screen, (0, 0, 0), (x, y), dot_size)

    elif side == 2:
        pygame.draw.circle(screen, (0, 0, 0), (x - 10, y - 10), dot_size)
        pygame.draw.circle(screen, (0, 0, 0), (x + 10, y + 10), dot_size)

    elif side == 3:
        pygame.draw.circle(screen, (0, 0, 0), (x - 10, y - 10), dot_size)
        pygame.draw.circle(screen, (0, 0, 0), (x, y), dot_size)
        pygame.draw.circle(screen, (0, 0, 0), (x + 10, y + 10), dot_size)

    elif side == 4:
        pygame.draw.circle(screen, (0, 0, 0), (x - 10, y - 10), dot_size)
        pygame.draw.circle(screen, (0, 0, 0), (x + 10, y - 10), dot_size)
        pygame.draw.circle(screen, (0, 0, 0), (x - 10, y + 10), dot_size)
        pygame.draw.circle(screen, (0, 0, 0), (x + 10, y + 10), dot_size)

    elif side == 5:
        pygame.draw.circle(screen, (0, 0, 0), (x - 10, y - 10), dot_size)
        pygame.draw.circle(screen, (0, 0, 0), (x + 10, y - 10), dot_size)
        pygame.draw.circle(screen, (0, 0, 0), (x - 10, y + 10), dot_size)
        pygame.draw.circle(screen, (0, 0, 0), (x + 10, y + 10), dot_size)
        pygame.draw.circle(screen, (0, 0, 0), (x, y), dot_size)

    elif side == 6:
        pygame.draw.circle(screen, (0, 0, 0), (x - 10, y - 10), dot_size)
        pygame.draw.circle(screen, (0, 0, 0), (x + 10, y - 10), dot_size)
        pygame.draw.circle(screen, (0, 0, 0), (x - 10, y + 10), dot_size)
        pygame.draw.circle(screen, (0, 0, 0), (x + 10, y + 10), dot_size)
        pygame.draw.circle(screen, (0, 0, 0), (x - 10, y), dot_size)
        pygame.draw.circle(screen, (0, 0, 0), (x + 10, y), dot_size)


def draw_screen():
    # clear the screen
    screen.fill((255, 255, 255))

    # loop through dice and draw them all
    for i in range(len(dice)):
        draw_dice(dice[i], 50 + (i * 50), 100)

    row_position = 100
    row_offset = 50
    offerings = []

    # display a list of possible pairs of dice
    for i in range(len(dice)):
        for j in range(i + 1, len(dice)):
            dice_spots = [0, 1, 2, 3]
            dice_spots.remove(i)
            dice_spots.remove(j)

            offer_1 = dice[i] + dice[j]
            offer_2 = dice[dice_spots[0]] + dice[dice_spots[1]]

            offers = [offer_1, offer_2]
            offers.sort()

            offering_string = str(offers[0]) + " - " + str(offers[1])

            # check if the pair has already been displayed
            if offering_string not in offerings:
                offerings.append(offering_string)

                # display the pair i and j
                draw_dice(dice[i], 300, row_position)
                draw_dice(dice[j], 350, row_position)

                # draw the pair formed by the remaining dice
                draw_dice(dice[dice_spots[0]], 450, row_position)
                draw_dice(dice[dice_spots[1]], 500, row_position)

                row_position += row_offset

    # update the screen
    pygame.display.update()


def fetch_events():
    global running, dice
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # check for key presses
        if event.type == pygame.KEYDOWN:
            # check for the escape key
            if event.key == pygame.K_ESCAPE:
                running = False

            # check for the return key
            if event.key == pygame.K_RETURN:
                # roll the dice
                for i in range(len(dice)):
                    dice[i] = random.randint(1, 6)

                # sort the dice
                dice.sort()


while running:

    fetch_events()

    draw_screen()

    # clock the game at 60 fps
    pygame.time.Clock().tick(60)
