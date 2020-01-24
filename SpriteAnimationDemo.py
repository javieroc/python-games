import pygame

WIDTH = 1000
HEIGHT = 700
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        sheet = pygame.image.load('assets/links.gif').convert_alpha()
        self.image = pygame.transform.scale(sheet, (100, 100))
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        # self.rect.centerx = WIDTH / 2 - 480   #center of rectangle
        # self.rect.bottom = HEIGHT - 5  #pixels up from the bottom
        self.speedx = 0
        self.speedy = 0
        self.walkingright = []
        self.walkingleft = []
        self.walkingup = []
        self.walkingdown = []
        self.direction = 'R'

        # Facing Right
        for x in range(0, 100*7+1, 100):
            # Use a transparent surface as the base image (pass pygame.SRCALPHA).
            image = pygame.Surface([100, 100], pygame.SRCALPHA)
            image.blit(sheet, (0,0), (x, 0, 100, 100))
            self.walkingright.append(image)
        # Facing Down
        for x in range(100*8, 100*15+1, 100):
            # Use a transparent surface as the base image (pass pygame.SRCALPHA).
            image = pygame.Surface([100, 100], pygame.SRCALPHA)
            image.blit(sheet, (0,0), (x, 0, 100, 100))
            self.walkingdown.append(image)
        # Facing Left
        for x in range(100*16, 100*23+1, 100):
            # Use a transparent surface as the base image (pass pygame.SRCALPHA).
            image = pygame.Surface([100, 100], pygame.SRCALPHA)
            image.blit(sheet, (0,0), (x, 0, 100, 100))
            self.walkingleft.append(image)
        # Facing Up
        for x in range(100*24, 100*31+1, 100):
            # Use a transparent surface as the base image (pass pygame.SRCALPHA).
            image = pygame.Surface([100, 100], pygame.SRCALPHA)
            image.blit(sheet, (0,0), (x, 0, 100, 100))
            self.walkingup.append(image)

    def update(self):
        pos_x = self.rect.x
        # You also need the y position for the vertical movement.
        pos_y = self.rect.y
        if self.direction == "R":
            frame = (pos_x // 30) % len(self.walkingright)
            self.image = self.walkingright[frame]
        if self.direction == "L":
            frame = (pos_x // 30) % len(self.walkingleft)
            self.image = self.walkingleft[frame]
        if self.direction == "U":
            frame = (pos_y // 30) % len(self.walkingup)
            self.image = self.walkingup[frame]
        if self.direction == "D":
            frame = (pos_y // 30) % len(self.walkingdown)
            self.image = self.walkingdown[frame]

        self.speedx = 0 #Need these to make sure
        self.speedy = 0 #Sprite stops moving on keyup
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
            self.direction = 'L'
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
            self.direction = 'R'
        if keystate[pygame.K_UP]:
            self.speedy = -5
            self.direction = 'U'
        if keystate[pygame.K_DOWN]:
            self.speedy = 5
            self.direction = 'D'
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        #Set Walls for Width and Height
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


def main():
    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        all_sprites.update()
        screen.fill(WHITE)
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()

main()
