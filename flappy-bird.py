import pygame
import time
from random import randint, randrange


sunset = (253, 72, 47)

white = (255, 255, 255)
green = (34, 139, 34)
sky_blue = (0, 204, 255)

greenyellow = (184, 255, 0)
brightblue = (47, 228, 253)
yellow = (255, 236, 0)
purple = (252, 67, 255)

colorChoices = [greenyellow, brightblue, yellow, purple]

pygame.init()

surfaceWidth = 800
surfaceHeight = 500

imageHeight = 24
imageWidth = 34

surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
pygame.display.set_caption("flappy-bird")
clock = pygame.time.Clock()

bird_img = pygame.image.load("images/bird.png")


def score(count):
    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render("Score: " + str(count), True, white)
    surface.blit(text, [0, 0])


def blocks(x_block, y_block, block_width, block_height, gap):
    colorChoice = colorChoices[randrange(0,len(colorChoices))]
    pygame.draw.rect(surface, green, [x_block, y_block, block_width, block_height])
    pygame.draw.rect(surface, green, [x_block, y_block+block_height+gap, block_width, surfaceHeight])


def replay_or_quit():
    for event in pygame.event.get([pygame.KEYUP, pygame.KEYDOWN, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            continue

        return event.key

    return None


def makeTextObjs(text, font):
    textSurface = font.render(text, True, sunset)
    return textSurface, textSurface.get_rect()


def msgSurface(text):
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    largeText = pygame.font.Font("freesansbold.ttf", 125)

    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
    surface.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Press any key to continue.', smallText)
    typTextRect.center = surfaceWidth / 2, ((surfaceHeight / 2) + 100)
    surface.blit(typTextSurf, typTextRect)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() == None:
        clock.tick()

    main()


def gameOver():
    msgSurface("You crashed!")


def bird(x, y, image):
    surface.blit(bird_img, (x, y))


def main():
    x = 150
    y = 200
    y_move = 0

    x_block = surfaceWidth
    y_block = 0

    block_width = 75
    block_height = randint(0, (surfaceWidth / 2))
    gap = imageHeight * 6
    block_move = 6

    current_score = 0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5

        y += y_move

        surface.fill(sky_blue)
        bird(x, y, bird_img)

        blocks(x_block, y_block, block_width, block_height, gap)
        x_block -= block_move

        score(current_score)

        if y > surfaceHeight - 40 or y < 0:
            gameOver()

        if x_block < (-1*block_width):
            x_block = surfaceWidth
            block_height = randint(0, (surfaceHeight / 2))
            current_score += 1

        if x + imageWidth > x_block:
            if x < x_block + block_width:
                if y < block_height:
                    if x - imageWidth < block_width + x_block:
                        gameOver()

        if x + imageWidth > x_block:
            if y + imageHeight > block_height + gap:
                if x < block_width + x_block:
                    gameOver()


        if x_block < (x - block_width) < x_block + block_move:
            current_score += 1

        if 3 <= current_score < 5:
            block_move = 6
            gap = imageHeight * 3.6
        if 5 <= current_score < 8:
            block_move = 7
            gap = imageHeight * 3.3
        if 8 <= current_score < 14:
            block_move = 8
            gap = imageHeight * 3.0

        pygame.display.update()
        clock.tick(60)


main()
pygame.quit()
quit()
