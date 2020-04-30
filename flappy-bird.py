import pygame

black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()
surface = pygame.display.set_mode((800, 400))
pygame.display.set_caption("flappy-bird")
clock = pygame.time.Clock()

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()