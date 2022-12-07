import sys, pygame, random
from PyDRIVERObjects import *
pygame.init()
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height)) #create a screen
driver = pygame.image.load("sharky.png")
rat = pygame.transform.smoothscale(rat, (80,80))
rat_rect = rat.get_rect()
rat_rects = []

friend_image = pygame.image.load("fishe.png")
friend_image = pygame.transform.smoothscale(friend_image, (90,90))
friend_rect = friend_image.get_rect()
friend_rect.center = (400, 200)
pygame.key.set_repeat(1)
while True: #this is the GAME loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            rat_rect.move_ip(-5,0)
        rat = pygame.transform.rotate(rat, 90)
        if event.key == pygame.K_RIGHT:
            rat_rect.move_ip(5, 0)
        rat = pygame.transform.rotate(rat, 90)
        if event.key == pygame.K_UP:
            rat_rect.move_ip(0, -10)
        if event.key == pygame.K_DOWN:
            rat_rect.move_ip(0, 10)
        if event.key == pygame.K_0:
            pos = pygame.mouse.get_pos()
            rat_rect.center = pos
    colliding = rat_rect.colliderect(friend_rect)
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
    screen.blit(rat, rat_rect)
    # screen.blit(friend_image, friend_rect)
    # rat_rect.move_ip(1,0)
    if not colliding:
        screen.blit(friend_image, friend_rect)
    pygame.display.flip()


    pygame.time.wait(0)
