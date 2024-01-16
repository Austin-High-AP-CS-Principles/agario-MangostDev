'''
Tutorial demonstrates how to create a game window with Python Pygame.

Any pygame program that you create will have this basic code
'''

import pygame
import sys
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, rad,color,x,y):
        super(Enemy,self).__init__()
        

    def move(self, count):
        if self.rect.left <= -0 or self.rect.right >= 800:
            self.deltax *= -1
        if self.rect.top <= -100 or self.rect.bottom >= 600:
            self.deltay *= -1
                    

        self.rect.centerx += self.deltax
        self.rect.centery += self.deltay

        if count%20 == 0:
            self.index = (self.index+1)%3
            self.image = self.images[self.index]

class Food(pygame.sprite.Sprite):
    def __init__(self, color):
        super(Food,self).__init__()
        self.color = color
        self.radius = 10
        self.image = pygame.Surface((self.radius*2,self.radius*2),pygame.SRCALPHA,32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image,color, (self.radius,self.radius), self.radius)
        self.rect = self.image.get_rect(center = (random.randint(10,790),random.randint(10,790)))




# Initialize Pygame and give access to all the methods in the package
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Tutorial")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create clock to later control frame rate
clock = pygame.time.Clock()

meals = pygame.sprite.Group() # Group is a high powered list
for num in range(20):
    meals.add(Food("Red"))

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (e.g., white)
    screen.fill(WHITE)

    # Paste all of the Food objects on the screen
    meals.draw(screen)

    # Update the display
    pygame.display.flip()

    # Set a frame rate to 60 frames per second
    clock.tick(60)

# Quit Pygame properly
pygame.quit()
sys.exit()