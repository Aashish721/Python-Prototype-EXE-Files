import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Run little dino, run!")

# Background setup
bg = []
try:
    for i in range(1, 5):
        img = pygame.image.load(f'Images-4-dino/bg{i}.png').convert_alpha()
        bg.append(pygame.transform.scale(img, (800, 500)))

except pygame.error:
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont(None, 36)


#-----------Player Setup----------------
dino = pygame.image.load('Images-4-dino/dino.png').convert_alpha()
dino_img = pygame.transform.scale(dino, (50, 50))
x = 100
y = 400

