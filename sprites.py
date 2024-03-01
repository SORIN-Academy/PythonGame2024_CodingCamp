import pygame

class Monster(pygame.sprite.Sprite):
    def init(self, x, y):
        super().init()
        self.image = pygame.Surface((50, 50))  # Replace with monster image
        self.image.fill((255, 0, 0))  # Filling thesprite with red color for visibility
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2

    def update(self, player_position):
        """Update the monster's position. Example of simple AI chasing the player"""
        if self.rect.x < player_position[0]:
            self.rect.x += self.speed
        elif self.rect.x > player_position[0]:
            self.rect.x -= self.speed

        if self.rect.y < player_position[1]:
            self.rect.y += self.speed
        elif self.rect.y > player_position[1]:
            self.rect.y -= self.speed

    def draw(self, screen):
        """Draw the monster on the screen"""
        screen.blit(self.image, self.rect)


pygame.init()
screen = pygame.display.set_mode((800, 600))


monster = Monster(100, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Assume we have a player position here
    player_position = (400, 300)  # Placeholder for player position

    screen.fill((0, 0, 0))  # Clear the screen with black
    monster.update(player_position)
    monster.draw(screen)
    pygame.display.flip()

pygame.quit()
