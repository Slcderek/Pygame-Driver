import sys, pygame, random
import pygame
from DriverObjects import *
pygame.init()
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height)) #create a screen
racecar = pygame.image.load("racecar.png")
racecar = pygame.transform.smoothscale(racecar, (80,80))
racecar_rect = racecar.get_rect()
racecar_rects = []

trophy_image = pygame.image.load("trophy.png")
trophy_image = pygame.transform.smoothscale(trophy_image, (30,30))
trophy_rect = trophy_image.get_rect()
trophy_rect.center = (400, 200)
pygame.key.set_repeat(1)
while True: #this is the GAME loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pos = pygame.mouse.get_pos()
        racecar_rect.center = pos
    colliding = racecar_rect.colliderect(trophy_rect)
    print("colliding", colliding)
        #update positions
    # x = random.randint(0, screen_width)
    # y = random.randint(0, screen_height)
    #
    # new_rat_rect = rat.get_rect()
    # new_rat_rect.center = (x, y)
    # rat_rects.append(new_rat_rect)
    # rat_rect.center = (x,y)
    # rat_rect.move_ip(1,0)
    screen.fill( (30,90,100) ) #drawing everything
    screen.blit(racecar, racecar_rect)
    # screen.blit(friend_image, friend_rect)
    # rat_rect.move_ip(1,0)
    if not colliding:
        screen.blit(trophy_image, trophy_rect)
    pygame.display.flip()


    pygame.time.wait(0)
