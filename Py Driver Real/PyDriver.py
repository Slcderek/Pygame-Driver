import pygame
from DriverObjects import *
pygame.init()

start_screen = pygame.image.load("startscreen.png")
start_screen_size = start_screen.get_size()
start_screen_rect = start_screen.get_rect()
screen = pygame.display.set_mode(start_screen_size) #create a screen
start_screen = start_screen.convert_alpha()
start_screen.set_colorkey((150, 150, 150))
start_screen_mask= pygame.mask.from_surface(start_screen)

map = pygame.image.load("background1.png")
map_size = map.get_size()
map_rect = map.get_rect()
screen = pygame.display.set_mode(map_size) #create a screen
map = map.convert_alpha()
map.set_colorkey((0, 0, 0))
map_mask= pygame.mask.from_surface(map)

racecar = pygame.image.load("racecar.png")
racecar = pygame.transform.smoothscale(racecar, (55,55))
racecar_rect = racecar.get_rect()
racecar_mask = pygame.mask.from_surface(racecar)
racecar_rects = []

start = pygame.image.load("start.png")
start = pygame.transform.smoothscale(start, (30,30))
# start_rek

trophy_image = pygame.image.load("trophy.png")
trophy_image = pygame.transform.smoothscale(trophy_image, (30,30))
trophy_rect = trophy_image.get_rect()
trophy_mask = pygame.mask.from_surface(trophy_image)
trophy_rect.center = (400, 200)
pygame.key.set_repeat(1)

def pixel_collision(mask1, rect1, mask2, rect2):
    offset_x = rect2[0] - rect1[0]
    offset_y = rect2[1] - rect1[1]
    # See if the two masks at the offset are overlapping.
    overlap = mask1.overlap(mask2, (offset_x, offset_y))
    return overlap

start_screen_click = False
while True: #this is the GAME loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pos = pygame.mouse.get_pos()
        racecar_rect.center = pos

    if pixel_collision(racecar_mask, racecar_rect, map_mask, map_rect):
        print("pixel collision")

    if pixel_collision(racecar_mask, racecar_rect, trophy_mask, trophy_rect):
        print("pixel collision")

    if event.type == pygame.MOUSEBUTTONDOWN:
        start_screen_click = True
    screen.fill( (0,0,0) ) #drawing everything
    screen.blit(map, map_rect)
    screen.blit(racecar, racecar_rect)
    screen.blit(trophy_image,trophy_rect)
    if start_screen_click == False:
        screen.blit(start_screen, start_screen_rect)
    pygame.display.flip()


    pygame.time.wait(0)
