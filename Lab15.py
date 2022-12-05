# Example pygame program

import sys, pygame, random
from Lab15Objects import *

def main():
    pygame.init()

    size = width, height = (600, 400)

    # make screen
    screen = pygame.display.set_mode(size)
    # make a Mr.Krabs object
    Krabs_image = pygame.image.load("220px-Mr._Krabs.svg.png")
    Krabs_image = pygame.transform.smoothscale(Krabs_image, (100,100))

    # Make some initial krabs
    krab_list = []
    for count in range(10):
        mrKrabs = Krabs(Krabs_image, (300, 200))
        krab_list.append(mrKrabs)
#even though there are 2 parameters, the self
    #part is implied. This shii is seen in leetcode asf!
    # make some initial food
    food_list = []
    for count in range(50):
        position = (random.randrange(0, width), random.randrange(0, height))
        food_item = Food(position)
        food_list.append(food_item)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()

        # Move the krabs
        for krab in krab_list:
            krab.move()

        # Add two new food items here each turn
        for count in range(2):
            position = (random.randrange(0, width), random.randrange(0, height))
            food_item = Food(position)
            food_list.append(food_item)
        # Add code to call grow on every food object in food list.
        for food in food_list:
            food.grow()
            #food_list = [food.grow() for food in food_list]
            #we dont want to use list comprehension
            # that shii is trash

        # Make every krab in the krab_list eat.
        for krab in krab_list:
            krab.eat(food_list)
        # Write a list comprehension to remove krabs with health <= 0
        #iterate over the krabs
        # if the krabs health is <= 0
        #remove from list
        # for krab in krab_list:
        #     if krab.health <= 0:
        #         krab.draw(screen)
        krab_list = [krab for krab in krab_list if krab.health > 0]
        values = [1, -2, 3, -4, 5]
        positive_squared_values = [value ** 2 for value in values if value > 0 ]

        #positive_squared_values=[]
        # for value in values:
        #     if (value > 0)
        #     squared_values.append(value**2)
        # Add in code to let the krabs reproduce by calling spawn.
        #krab.spawn() -> return new krab OR none
        for krab in krab_list:
            spawn = krab.spawn()
            if spawn:
                krab_list.append(spawn)
        # clear the screen
        screen.fill((120,120,120))
        for food in food_list:
            food.draw(screen)
        for krab in krab_list:
            krab.draw(screen)

        # update the display
        pygame.display.update()

if __name__ == "__main__":
        main()