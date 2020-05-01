import pygame
import time
from random import randint

black = (0, 0, 0)
white = (255, 255, 255)
green = (34, 139, 34)
sky_blue = (0, 204, 255)

pygame.init()

surfaceWidth = 800
surfaceHeight = 500

imageHeight = 24
imageWidth = 34

surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
pygame.display.set_caption("flappy-bird")
clock = pygame.time.Clock()

bird_img = pygame.image.load("images/bird.png")


def blocks(x_block, y_block, block_width, block_height, gap):
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
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def msgSurface(text):
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    largeText = pygame.font.Font("freesansbold.ttf", 150)

    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
    surface.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Press any key to continue.', smallText)
    titleTextRect.center = surfaceWidth / 2, ((surfaceHeight / 2) + 100)
    surface.blit(typTextSurf, typTextRect)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() == None:
        clock.tick()

    main()


def gameOver():
    msgSurface("You fell!")


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
    gap = imageHeight * 3
    block_move = 6

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

        if y > surfaceHeight - 40 or y < 0:
            gameOver()

        if x_block < (-1*block_width):
            x_block = surfaceWidth
            block_height = randint(0, (surfaceHeight / 2))

        if x + imageWidth > x_block:
            if x < x_block + block_width:
                print("possibly within the boundaries of x")
                if y < block_height:
                    print("Y crossover UPPER!")
                    if x - imageWidth < block_width + x_block:
                        print("game over hit upper")
                        gameOver()

        if x + imageWidth > x_block:
            print("x crossover")

            if y + imageHeight > block_height + gap:
                print("Y crossover lower")

                if x < block_width + x_block:
                    print('game over LOWER')
                    gameOver()


        pygame.display.update()
        clock.tick(60)


main()
pygame.quit()
quit()
