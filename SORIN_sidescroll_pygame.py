#import all systems
import pygame
import sys
import random

pygame.init()


#Constants for gameplay
SCREEN_WIDTH, SCREEN_HEIGHT = 1080, 720
PLAYER_SPEED = 5
ENEMY_SPEED = 2
BULLET_SPEED = 10
GRAVITY = 0.5
JUMP_STRENGTH = 10
KEY_PRESS_JUMP = 0
PLAYER_HP = 10
ENEMY_HP = 7.5
DAMAGE = 2.5
ENEMY_DAMAGE = 2

enemy_counter = 0
damage_applied = False
direction = 1



#Create window
screen = pygame.display.swaet_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Platformer Shooter")


#Player setup
player = pygame.Rect(50, 50, 40, 60)
player_velocity = [0, 0]

#Enemy setup
enemy = pygame.Rect(700, 50, 40, 60)
enemy_velocity = [0, 0]

#Bullet setup
bullets = []


#define versatile functions
def ground_collision(obj, obj_velocity):
    if obj.y > SCREEN_HEIGHT - obj.height:
        obj.y = SCREEN_HEIGHT - obj.height
        obj_velocity[1] = 0
        
def wall_collision(obj, obj_velocity):
    if obj.x < 0:
        obj.x = 0
    if obj.x > SCREEN_WIDTH - obj.width:
        obj.x = SCREEN_WIDTH - obj.width
        
def create_enemy():
    enemy = pygame.Rect(random.randint(200, SCREEN_WIDTH - 50), 50, 40, 60)
    enemy_velocity = [0, 0]
    ENEMY_HP = 5
    ENEMY_SPEED
    return enemy, enemy_velocity, ENEMY_HP, ENEMY_SPEED

# Initialize the first enemy
enemy, enemy_velocity, ENEMY_HP, ENEMY_SPEED = create_enemy()

class Bullet: 
    def __init__(self, rect, direction):
        self.rect = rect
        self.direction = direction

# Game running & shooting
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_rect = pygame.Rect(player.x + player.width // 2, player.y + player.height // 2, BULLET_SPEED * direction, 10)
                bullet = Bullet(bullet_rect, direction)
                bullets.append(bullet)

               
                

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        direction = -1
        player.x -= PLAYER_SPEED
    if keys[pygame.K_d]:
        direction = 1
        player.x += PLAYER_SPEED 
    if keys[pygame.K_w] and ((player.y == SCREEN_HEIGHT - player.height)):         # Only jump if on the ground
       # or (player.x == 0 and player.y > (SCREEN_HEIGHT - 3*player.height)))):  # wall double jump
        
        player_velocity[1] = -12  # Negative value for upward movement
        player_velocity[1] += GRAVITY
        player.y += player_velocity[1]
        
        
    # Enemy Movement (manual)
    #     keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     enemy.x -= ENEMY_SPEED
    # if keys[pygame.K_RIGHT]:
    #     enemy.x += ENEMY_SPEED
    # if keys[pygame.K_UP] and (enemy.y == SCREEN_HEIGHT - enemy.height):
    #     enemy_velocity[1] = -12
    #     enemy_velocity[1] += GRAVITY
    #     enemy.y += enemy_velocity[1]
    
    # Enemy movement (automatic)
        
    if enemy.x - player.x > 0:
        enemy.x -= ENEMY_SPEED
    else: enemy.x += ENEMY_SPEED
        
            
    # Gravity
    player_velocity[1] += GRAVITY
    player.y += player_velocity[1]
    # Grav for enemies
    enemy_velocity[1] += GRAVITY
    enemy.y += enemy_velocity[1]
    
        
          
    # Collision detection with the ground
    ground_collision(player, player_velocity)
    ground_collision(enemy, enemy_velocity)
    
    wall_collision(player, player_velocity)
    wall_collision(enemy, enemy_velocity)
    
    

    
    # Bullet movement
    for bullet in bullets[:]:
        bullet_rect, direction = bullet_rect, bullet.direction # Unpack the Bullet object correctly
        bullet_rect = pygame.Rect(player.x + player.width // 2, player.y + player.height // 2, BULLET_SPEED * direction, 10)
        bullet_rect.x += direction * BULLET_SPEED
        if bullet_rect.colliderect(enemy):
            bullets.remove(bullet)
            ENEMY_HP -= DAMAGE
            if ENEMY_HP <= 0:
                print("Enemy Slain")
                # running = False
                enemy, enemy_velocity, ENEMY_HP, ENEMY_SPEED = create_enemy()
                # print(f'Before increasing: health ENEMY_HP = {ENEMY_HP}') ##keeps track of enemy hp
                ENEMY_HP = ENEMY_HP + (enemy_counter / 2)                 ##enemy hp increases by 0.5 increments
                # print(f'After increasing: health ENEMY_HP = {ENEMY_HP}')
                enemy_counter += 1
                print(f"Points: {100* int(enemy_counter)}")
                print(f"Enemy health: {ENEMY_HP}/{ENEMY_HP}")
            print(f"Enemy # {enemy_counter} -- health: {ENEMY_HP}")

                
    if enemy.colliderect(player) and not damage_applied:
        PLAYER_HP -= ENEMY_DAMAGE
        damage_applied = True
        print(f"Player health: {PLAYER_HP}")
        
        if PLAYER_HP <= 0:
            print("GAME OVER")
            running = False
    elif not enemy.colliderect(player):
        damage_applied = False



                
    # Drawing
    screen.fill((0, 0, 0))  # Clear screen
    pygame.draw.rect(screen, (255, 192, 203), player)  # Draw player
    pygame.draw.rect(screen, (0, 255, 20), enemy)  # Draw enemy
    for bullet in bullets:
        pygame.draw.ellipse(screen, (120, 140, 255), bullet)  # Draw bullets
        
    # if arc_visible:
    #     arc_rect = pygame.Rect(player.x + player.width // 2, player.y - 30, 40, 100)
    #     pygame.draw.arc(screen, (150, 150, 255), arc_rect, -1.30, 1.30, 2)
    #     if arc_rect.colliderect(enemy) and damage_applied == False:
    #         entity_collision(arc_rect, ARC_DAMAGE, enemy, ENEMY_HP)
    #     elif not arc_rect.colliderect(enemy):
    #         damage_applied = False
            
    print(direction)
    # Update display
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()
sys.exit()
