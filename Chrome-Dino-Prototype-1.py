import pygame
import random
import sys

clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Game 1")

# Background setup
img1 = pygame.image.load('bg1.png').convert_alpha()
bg1 = pygame.transform.scale(img1, (800, 400))
img2 = pygame.image.load('bg2.png').convert_alpha()
bg2 = pygame.transform.scale(img2, (800, 400))
img3 = pygame.image.load('bg3.png').convert_alpha()
bg3 = pygame.transform.scale(img3, (800, 400))
img4 = pygame.image.load('bg4.png').convert_alpha()
bg4 = pygame.transform.scale(img4, (800, 400))
bg_frames = [bg1, bg2, bg3, bg4]

# Player setup
dino = pygame.image.load('dino.png').convert_alpha()
dino_img = pygame.transform.scale(dino, (50, 50))
x = 100
y = 300
velocity_y = 0

# Obstacle setup
obs_x = random.randint(800, 900)
obs_y = 300

bg_frame = 0

# Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
   
    bg_frame += 0.01
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_SPACE] and y == 300:
        velocity_y = -15
    
    velocity_y += 1
    y += velocity_y
    
    if y >= 300:
        y = 300
        velocity_y = 0
        
    if bg_frame >= len(bg_frames):
        bg_frame = 0

    
    screen.blit(bg_frames[int(bg_frame)], (0, 0))
    
    player = pygame.Rect(x, y, 50, 50)
    obs = pygame.Rect(obs_x, obs_y, 40, 40)
    
    
    pygame.draw.rect(screen, (255, 0, 0), obs) 
    
    obs_x -= 5
    if obs_x < -40:
        obs_x = random.randint(800, 1100)
        
    if player.colliderect(obs):
        print("You Lost")
        pygame.quit()
        sys.exit()
        
   
    screen.blit(dino_img, (x, y))
    
    clock.tick(60)
    pygame.display.update()
