import sys, pygame, time
# Starter code for an adventure game. Written by David Johnson for CS 1400 University of Utah.
# Finished game authors:Luke Witzel and Derek Tinoco

def pixel_collision(mask1, rect1, mask2, rect2):
    """
    Check if the non-transparent pixels of one mask contacts the other.
    """
    offset_x = rect2[0] - rect1[0]
    offset_y = rect2[1] - rect1[1]
    # See if the two masks at the offset are overlapping.
    overlap = mask1.overlap(mask2, (offset_x, offset_y))
    return overlap != None

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

    #map 2
    map2 = pygame.image.load("background2.png")
    # Store window width and height in different forms for easy access
    map2_size = map2.get_size()
    map2_rect = map2.get_rect()
    screen = pygame.display.set_mode(map2_size)
    map2 = map2.convert_alpha()
    map2.set_colorkey((0, 0, 0))
    map2_mask = pygame.mask.from_surface(map2)

    #map 3
    map3 = pygame.image.load("background3.png")
    # Store window width and height in different forms for easy access
    map3_size = map3.get_size()
    map3_rect = map3.get_rect()
    screen = pygame.display.set_mode(map2_size)
    map3 = map3.convert_alpha()
    map3.set_colorkey((0, 0, 0))
    map3_mask = pygame.mask.from_surface(map3)

    #map 4
    map4 = pygame.image.load("background4.png")
    # Store window width and height in different forms for easy access
    map4_size = map4.get_size()
    map4_rect = map4.get_rect()
    screen = pygame.display.set_mode(map2_size)
    map4 = map4.convert_alpha()
    map4.set_colorkey((0, 0, 0))
    map4_mask = pygame.mask.from_surface(map4)

    # Create the player data
    player = pygame.image.load("racecar.png").convert_alpha()
    player = pygame.transform.smoothscale(player, (50, 50))
    player_rect = player.get_rect()
    player_mask = pygame.mask.from_surface(player)

    # gas data
    gas = pygame.image.load("gas.png").convert_alpha()
    gas = pygame.transform.smoothscale(gas,(35,35))
    gas_rect = gas.get_rect()
    gas_mask = pygame.mask.from_surface(gas)
    gas_rect.center = (650, 280)

    # Create the key
    key = pygame.image.load("start.png").convert_alpha()
    key = pygame.transform.smoothscale(key, (40, 40))
    key_rect = key.get_rect()
    key_rect.center = (300, 450)
    key_mask = pygame.mask.from_surface(key)

    # Create the starter game flag
    starter_flag = pygame.image.load("start.png").convert_alpha()
    starter_flag = pygame.transform.smoothscale(starter_flag, (50, 50))
    starter_flag_rect = starter_flag.get_rect()
    starter_flag_rect.center = (290, 300)
    starter_flag_mask = pygame.mask.from_surface(starter_flag)
    #creates the cement
    cement = pygame.image.load("cement.png").convert_alpha()
    cement = pygame.transform.smoothscale(cement, (100, 100))
    cement_rect = cement.get_rect()
    cement_rect.center = (350, 530)
    cement_mask = pygame.mask.from_surface(cement)

    #creates the oil
    oil = pygame.image.load("oil.png").convert_alpha()
    oil = pygame.transform.smoothscale(oil, (70, 70))
    oil_rect = oil.get_rect()
    oil_rect.center = (630, 550)
    oil_mask = pygame.mask.from_surface(oil)

    # creates the unscrambler
    unscrambler = pygame.image.load("unscrambler.png").convert_alpha()
    unscrambler = pygame.transform.smoothscale(unscrambler, (100, 100))
    unscrambler_rect = unscrambler.get_rect()
    unscrambler_rect.center = (640, 550)
    unscrambler_mask = pygame.mask.from_surface(unscrambler)

    #Creates the finish line
    finish_line = pygame.image.load("finishline.png").convert_alpha()
    finish_line = pygame.transform.smoothscale(finish_line, (100, 100))
    finish_line_rect = finish_line.get_rect()
    finish_line_rect.center = (325, 240)
    finish_line_mask = pygame.mask.from_surface(finish_line)

    start_screen = pygame.image.load("startscreen.png")
    start_screen_size = start_screen.get_size()
    start_screen_rect = start_screen.get_rect()
    screen = pygame.display.set_mode(start_screen_size)  # create a screen
    start_screen = start_screen.convert_alpha()
    start_screen.set_colorkey((150, 150, 150))
    start_screen_mask = pygame.mask.from_surface(start_screen)
    # The frame tells which sprite frame to draw
    frame_count = 0

    #game over screen
    game_over_screen = pygame.image.load("gameover.png")
    game_over_screen_rect = game_over_screen.get_rect()
    game_over_screen = game_over_screen.convert_alpha()
    game_over_screen = pygame.transform.smoothscale(game_over_screen, (map_size))
    game_over_screen_mask = pygame.mask.from_surface(game_over_screen)
    #game won screen
    game_won_screen = pygame.image.load("gamewon.png")
    game_won_screen_rect = game_won_screen.get_rect()
    game_won_screen = game_won_screen.convert_alpha()
    game_won_screen = pygame.transform.smoothscale(game_won_screen, (map_size))
    game_won_screen_mask = pygame.mask.from_surface(game_won_screen)


    starter_screen = True


    # The clock helps us manage the frames per second of the animation
    clock = pygame.time.Clock()

    # Get a font - there is some problem on my Mac that makes this pause for 10s of seconds sometimes.
    # I will see if I can find a fix.
    myfont = pygame.font.SysFont('monospace', 24)


    # The is_alive variable records if anything bad has happened (off the path, touch guard, etc.)
    is_alive = True

    # Hide the arrow cursor and replace it with a sprite.
    pygame.mouse.set_visible(False)

    # This is the main game loop. In it, we must:
    # - check for events
    # - update the scene
    # - draw the scene
    start_screen_click = False
    first_starter_flag_clicked = False
    is_game_over = False
    second_start_flag_clicked = False
    second_level_start = False
    second_level = False
    third_start_flag_clicked = False
    third_level_start = False
    third_level = False
    touch_gas = False
    touch_cement = False
    touch_trophy = False
    touch_unscrambler = False
    is_game_won = False
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

        #this is where the flag button appears
        if start_screen_click == True:
            screen.fill((0, 0, 0))  # This helps check if the image path is transparent
            screen.blit(gas, gas_rect)
            screen.blit(map, map_rect)
            screen.blit(player, player_rect)
            starter_screen = False
            screen.blit(starter_flag, starter_flag_rect)
            # put something here that will set start_flag_clicked to true once clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if screen.blit(starter_flag, starter_flag_rect).collidepoint(pos):
                    first_starter_flag_clicked = True

        #this is where the game will actually begin.
        if first_starter_flag_clicked == True:
                screen.fill((0, 0, 0))  # This helps check if the image path is transparent
                screen.blit(map, map_rect)
                screen.blit(player, player_rect)
                screen.blit(level_1_hint, (300, 600))
                if touch_gas == False:
                    screen.blit(gas, gas_rect)
                if pixel_collision(player_mask, player_rect, map_mask, map_rect):
                    is_game_over = True
                    touch_gas = None
                if pixel_collision(player_mask, player_rect, gas_mask, gas_rect):
                    touch_gas = True
                if pixel_collision(player_mask, player_rect, finish_line_mask, finish_line_rect) and is_game_over == False:
                    print("congrats! You've passed the first level")
                    second_level_start = True
                    touch_gas = False
                    touch_cement = False

        if second_level_start == True and is_game_over == False:
                    is_game_over = False
                    first_starter_flag_clicked = None
                    screen.fill((0, 0, 0))  # This helps check if the image path is transparent
                    screen.blit(map2, map2_rect)
                    screen.blit(player, player_rect)
                    if second_start_flag_clicked == False:
                        screen.blit(starter_flag, starter_flag_rect)
                    # put something here that will set start_flag_clicked to true once clicked
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if screen.blit(starter_flag, starter_flag_rect).collidepoint(pos):
                            second_level = True
                            touch_gas = None
        #checks if the second level has started yet, only after flag is clicked
        if second_level == True:
                    start_screen_click = False
                    screen.fill((0, 0, 0))  # This helps check if the image path is transparent
                    screen.blit(map2, map2_rect)
                    screen.blit(oil, oil_rect)
                    screen.blit(player, player_rect)
                    screen.blit(level_2_hint, (300, 650))
                    if touch_cement == False:
                        screen.blit(cement, cement_rect)
                        if pixel_collision(player_mask, player_rect, oil_mask, oil_rect):
                            is_game_over = True
                    if pixel_collision(player_mask, player_rect, map2_mask, map2_rect):
                            is_game_over = True
                            touch_cement = None
                    if pixel_collision(player_mask, player_rect, cement_mask, cement_rect) and is_game_over == False:
                            touch_cement = True

                    if pixel_collision(player_mask, player_rect, finish_line_mask, finish_line_rect) and is_game_over == False:
                        print("congrats! You've passed the second level")
                        third_level_start = True
                        touch_cement = False
                        second_level = None


        #checks if the third level has started yet, will happen only after clicking flag
        if third_level_start == True :
            is_game_over = False
            second_level_start = None
            screen.fill((0, 0, 0))  # This helps check if the image path is transparent
            screen.blit(map3, map3_rect)
            screen.blit(player, player_rect)
            if third_start_flag_clicked == False:
                screen.blit(starter_flag, starter_flag_rect)
            # put something here that will set start_flag_clicked to true once clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if screen.blit(starter_flag, starter_flag_rect).collidepoint(pos):
                    third_level = True

        #sets the transparency and the stage
        if third_level == True:
            start_screen_click = False
            screen.fill((0, 0, 0))
            screen.blit(player, player_rect)
            screen.blit(level_3_hint, (300, 650))
            if touch_unscrambler == False:
                screen.blit(map4, map4_rect)
                screen.blit(unscrambler, unscrambler_rect)
            if touch_unscrambler == True:
                screen.blit(map3, map3_rect)
                screen.blit(player, player_rect)
                screen.blit(level_4_hint, (300, 650))
            if pixel_collision(player_mask, player_rect, map3_mask, map3_rect):
                is_game_over = True
                touch_trophy = None
            if pixel_collision(player_mask, player_rect, finish_line_mask,
                finish_line_rect) and is_game_over == False:
                print("congrats! You've passed all the levels")
                is_game_won = True
            # if pixel_collision(player_mask, player_rect, map3_mask, map3_rect):
            #     is_game_over = True
            #     touch_trophy = None
            if screen.blit(unscrambler, unscrambler_rect).collidepoint(pos) and is_game_over == False:
                touch_unscrambler = True
        #code below checks if the game has started
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_screen_click = True
        #below are the objectives for the levels
        if touch_gas == True:
            screen.blit(finish_line, finish_line_rect)
        if touch_cement == True:
            screen.blit(finish_line, finish_line_rect)
        if touch_trophy == True:
            screen.blit(finish_line, finish_line_rect)
        if touch_unscrambler == True:
           screen.blit(finish_line, finish_line_rect)


        #game over code here
        if is_game_over == True:
            screen.blit(game_over_screen, game_over_screen_rect)
        if is_game_won == True:
            screen.blit(game_won_screen, game_won_screen_rect)


        # Write some text to the screen. You can do something like this to show some hints or whatever you want.
        label = myfont.render("By Luke and Derek!", True, (255,255,0))
        screen.blit(label, (20,20))

        level_1_hint = myfont.render("hint:collect the gas and then finish the race!", True, (0,0,0))
        level_2_hint = myfont.render("hint:cement dust can soak up oil!", True, (0,0,0))
        level_3_hint = myfont.render("hint:The map must be unscrambled before it can be won", True, (255, 255, 255))
        level_4_hint = myfont.render("hint:Take what is rightfully yours and \n win the game!", True, (255, 255, 255))

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
