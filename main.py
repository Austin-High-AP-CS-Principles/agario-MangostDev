import pygame, sys, random, math


class Food(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, color):
        super(Food, self).__init__() #calling on the constructor for the sprite class
        self.radius = 5
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center = (random.randint(10,790), random.randint(10, 590)))
    #def relocate(self)

class Enemy(pygame.sprite.Sprite):
    # Constructor
    def __init__(self):
        super(Enemy, self).__init__() #calling on the constructor for the sprite class
        self.radius = random.randint(10,20)
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.index = 0
        self.speed = 3
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, "Red", (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center = (random.randint(10,790), random.randint(10, 590)))
        self.direction = random.uniform(0.0, 6.28)
        self.deltax = self.speed * math.cos(self.direction)
        self.deltay = self.speed * math.sin(self.direction)
        #self.speed = 10 pixels per tick

    def move(self, count):
        if self.rect.left <= -0 or self.rect.right >= 790:
            self.deltax *= -1
        if self.rect.top <= -10 or self.rect.bottom >= 590:
            self.deltay *= -1

        self.rect.centerx += self.deltax
        self.rect.centery += self.deltay

    def grow(self, radius):
        self.radius += radius
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.speed *= .9
        self.deltax = self.speed * math.cos(self.direction)
        self.deltay = self.speed * math.sin(self.direction)

    def collision(self):
        for obj in objects:
            if obj != self:
                if pygame.sprite.collide_rect(self, obj): 
                    print(obj)
                    if self.radius > obj.radius:
                        self.grow(obj.radius)
                        obj.kill()

class Player(Enemy):
    # Constructor
    def __init__(self):
        super(Player, self).__init__() #calling on the constructor for the sprite class
        self.radius = 15
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.color = "Blue"
        pygame.draw.circle(self.image, "Blue", (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center = (random.randint(10,200), random.randint(10, 160)))

    def move(self):
        mx,my = pygame.mouse.get_pos()
        distx = mx - self.rect.centerx
        disty = self.rect.centery - my
        disty *= -1
        angle = math.atan2(disty,distx)
        self.deltax = self.speed * math.cos(angle)
        self.deltay = self.speed * math.sin(angle)
        self.rect.centerx += self.deltax
        self.rect.centery += self.deltay
        

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Agar.io")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create Text
font = pygame.font.Font(None,100)
text_surface = font.render("Game Over", False,"Red")
text_surface_two = font.render("You Win!", False, "Green")

enemies = pygame.sprite.Group()
for num in range(10):
    enemies.add(Enemy())

meals = pygame.sprite.Group()
for num in range(20):
    meals.add(Food("Green"))

player = Player()

objects = pygame.sprite.Group()
objects.add(enemies)
objects.add(meals)
objects.add(player)
        
# Create clock to later control frame rate
clock = pygame.time.Clock()

# Main game loop
count = 0
running = True
while running:
    count += 1
    # Event handling
    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running = False
    # Fill the screen with a color (e.g., white)
    screen.fill(WHITE)

    # Create more food on a timer
    if count % 25 == 0:
        if len(meals.sprites()) < 15:
            meals.add(Food("Green"))
            objects.add(meals)

    #Paste all of the food objects onto the screen.

    objects.draw(screen)

    player.move()

    for enemy in enemies:
        enemy.move(count)
        enemy.collision()
        player.collision()

    #for obj in objects:
    #    for other in objects:
    #        if obj != other and type(obj) != Food:
    #            collide = pygame.sprite.collide_rect(obj, other)
    #            if collide:
    #                if obj.radius > other.radius:
    #                    obj.grow(other.radius)
    #                    other.kill()

    # Check if the player is still alive
    if pygame.sprite.Sprite.alive(player) == False:
        screen.blit(text_surface,(200,250))

    # Check if there are any enemies
    if len(enemies.sprites()) == 0:
        screen.blit(text_surface_two,(200,250))
        
        

    # Update the display
    pygame.display.flip()

    # Set a frame rate to 60 frames per second
    clock.tick(60)


# Quit Pygame properly
pygame.quit()
sys.exit()