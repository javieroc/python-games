import pygame
import random

colors = [(255,0,0,0), (0,255,0), (0,0,255)]

class Player():
    def __init__(self, id):
        self.id = id
        self.x = random.randint(0,800)
        self.y = random.randint(0,800)
        self.width = 50
        self.height = 50
        self.color = colors[random.randint(0,2)]
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel
