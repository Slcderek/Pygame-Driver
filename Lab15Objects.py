# Example pygame program

import sys, pygame, random
#classes define the behavir of an object.
#class and object are interchangable
#Template or outlines are more classes
class Food:
    def __init__(self, position):
        self.position = position
        self.stored_food = 1
#the init part creates or intializes
    def draw(self, screen):
        pygame.draw.circle(screen, (30, 230, 30), self.position, int(self.stored_food))
#'self' refers to the object itself, it is an implied parameter.
    #it describes the object that was used to call the
    #function!!!
    def grow(self):
        self.stored_food += 0.01


class Krabs:
    speed = 5
    def __init__(self, image, position):
        self.image = image
        self.rectangle = self.image.get_rect()
        self.rectangle.center = position
        self.health = 20

    def draw(self, screen):
        screen.blit(self.image, self.rectangle)

    def move(self):
        x_change = random.randint(-Krabs.speed, Krabs.speed)
        y_change = random.randint(-Krabs.speed, Krabs.speed)
        self.rectangle.move_ip(x_change, y_change)
        self.health -= 0.15

    def eat(self, food_list):
        for food in food_list:
            # Test if the position of the food is inside the rectangle for the krab.
            if self.rectangle.collidepoint(food.position[0], food.position[1]):
                self.health += food.stored_food
                food_list.remove(food) # Remove the the eaten food from the list of food. It is OK to remove as we return after eating 1 food.
                return

    def spawn(self):
        if self.health > 50:
            self.health -= 20
            return Krabs(self.image, self.rectangle.center)
        else:
            return None


