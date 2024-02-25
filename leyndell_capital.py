import sys
import pygame


pygame.init()


screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption('Elden Ring Platformer')

# Background
background = pygame.image.load('Leyndell_Capital.png')


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#screen.blit((player,100,100))
    # Fill the screen with a color (RGB)
#screen.fill((0, 255, 0))

    # Update the display
pygame.display.flip()


pygame.quit()
