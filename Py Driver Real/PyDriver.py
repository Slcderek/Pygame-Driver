import sys, pygame, math

# Starter code for an adventure game. Written by David Johnson for CS 1400 University of Utah.

# Finished game authors:Luke Witzel and Derek Tinoco
#
#

def pixel_collision(mask1, rect1, mask2, rect2):
    """
    Check if the non-transparent pixels of one mask contacts the other.
    """
    offset_x = rect2[0] - rect1[0]
    offset_y = rect2[1] - rect1[1]
    # See if the two masks at the offset are overlapping.
    overlap = mask1.overlap(mask2, (offset_x, offset_y))
    return overlap != None

# def level1

def main():

    # Initialize pygame
    pygame.init()

    map = pygame.image.load("background1.png")
    # Store window width and height in different forms for easy access
    map_size = map.get_size()
    map_rect = map.get_rect()

    # create the window based on the map size
    screen = pygame.display.set_mode(map_size)
    map = map.convert_alpha()
    map.set_colorkey((0, 0, 0))
    map_mask = pygame.mask.from_surface(map)

    # Create the player data
    player = pygame.image.load("racecar.png").convert_alpha()
    player = pygame.transform.smoothscale(player, (50, 50))
    player_rect = player.get_rect()
    player_mask = pygame.mask.from_surface(player)

    # Create the key
    key = pygame.image.load("start.png").convert_alpha()
    key = pygame.transform.smoothscale(key, (40, 40))
    key_rect = key.get_rect()
    key_rect.center = (300, 450)
    key_mask = pygame.mask.from_surface(key)

    # Create the door
    door = pygame.image.load("start.png").convert_alpha()
    door = pygame.transform.smoothscale(door, (50, 50))
    door_rect = door.get_rect()
    door_rect.center = (290, 300)
    door_mask = pygame.mask.from_surface(door)

    start_screen = pygame.image.load("startscreen.png")
    start_screen_size = start_screen.get_size()
    start_screen_rect = start_screen.get_rect()
    screen = pygame.display.set_mode(start_screen_size)  # create a screen
    start_screen = start_screen.convert_alpha()
    start_screen.set_colorkey((150, 150, 150))
    start_screen_mask = pygame.mask.from_surface(start_screen)
    # The frame tells which sprite frame to draw
    frame_count = 0

    game_over_screen = pygame.image.load("gameover.png")
    game_over_screen_rect = game_over_screen.get_rect()
    game_over_screen = game_over_screen.convert_alpha()
    game_over_screen = pygame.transform.smoothscale(game_over_screen, (map_size))

    start_flag = pygame.image.load('start.png').convert_alpha()
    game_started = False

    starter_screen = True
    first_level = True
    second_level = True


    # The clock helps us manage the frames per second of the animation
    clock = pygame.time.Clock()

    # Get a font - there is some problem on my Mac that makes this pause for 10s of seconds sometimes.
    # I will see if I can find a fix.
    myfont = pygame.font.SysFont('monospace', 24)

    # The started variable records if the start color has been clicked and the level started
    started = False

    key_found = False
    # The is_alive variable records if anything bad has happened (off the path, touch guard, etc.)
    is_alive = True

    # Hide the arrow cursor and replace it with a sprite.
    pygame.mouse.set_visible(False)

    # This is the main game loop. In it, we must:
    # - check for events
    # - update the scene
    # - draw the scene
    start_screen_click = False
    start_flag_clicked = False
    is_game_over = False

    while is_alive:
        # Check events by looping over the list of events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_alive = False

        # Position the player to the mouse location
        pos = pygame.mouse.get_pos()
        player_rect.center = pos

        # See if we touch the maze walls

        #if started logic happens
        # This is before clicking the screen
        if starter_screen == True:
            if not start_screen_click:
                screen.blit(start_screen, start_screen_rect)

        #this gon be where the flag button appears
        if start_screen_click == True:
            screen.fill((0, 0, 0))  # This helps check if the image path is transparent
            screen.blit(map, map_rect)
            screen.blit(player, player_rect)
            starter_screen = False
            screen.blit(door, door_rect)
            # put something here that will set start_flag_clicked to true once clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if screen.blit(door, door_rect).collidepoint(pos):
                    start_flag_clicked = True

        #this is where the fun begins (the game)
        if start_flag_clicked == True:
            if start_flag_clicked == True:
                screen.fill((0, 0, 0))  # This helps check if the image path is transparent
                screen.blit(map, map_rect)
                screen.blit(player, player_rect)
                if pixel_collision(player_mask, player_rect, map_mask, map_rect):
                    print("colliding", frame_count)  # Don't leave this in the game
                    is_game_over = True
                    if is_game_over == True:
                        screen.blit(game_over_screen, game_over_screen_rect)



        if event.type == pygame.MOUSEBUTTONDOWN:
            start_screen_click = True



        # Draw the background
        # screen.fill((0,0,0)) # This helps check if the image path is transparent
        # screen.blit(map, map_rect)

        # # Draw the player character
        # screen.blit(player, player_rect)
        # if not key_found:
        #     screen.blit(key, key_rect)
        #     screen.blit(door, door_rect)

        # og start screen
        # if not start_screen_click:
        #     screen.blit(start_screen, start_screen_rect)
        # if start_screen_click:


        # Write some text to the screen. You can do something like this to show some hints or whatever you want.
        label = myfont.render("By Luke and Derek!", True, (255,255,0))
        screen.blit(label, (20,20))

        # Every time through the loop, increase the frame count.
        frame_count += 1

        # Bring drawn changes to the front
        pygame.display.update()

        # This tries to force the loop to run at 30 fps
        clock.tick(33)

        if start_screen_click == False:
            screen.blit(start_screen, start_screen_rect)
    pygame.quit()
    sys.exit()


# Start the program
main()