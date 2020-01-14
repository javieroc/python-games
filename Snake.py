import random
import pygame
import tkinter as tk
from tkinter import messagebox

width = 500
height = 500
rows = 20
window = pygame.display.set_mode((width, height))


class Cube(object):

    rows = 20
    width = 500

    def __init__(self, start, color=(255,0,0)):
        self.pos = start
        self.dirx = 1
        self.diry = 0
        self.color = color


    def setDir(self, dirx, diry):
        self.dirx = dirx
        self.diry = diry


    def move(self):
        self.pos = (self.pos[0] + self.dirx, self.pos[1] + self.diry)


    def draw(self):
        dis = self.width // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(window, self.color, (i*dis+1,j*dis+1, dis-1, dis-1))


class Snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dirx = 1
        self.diry = 0


    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and self.dirx != 1:
                self.dirx = -1
                self.diry = 0
                self.turns[self.head.pos[:]] = [self.dirx, self.diry]

            elif keys[pygame.K_RIGHT] and self.dirx != -1:
                self.dirx = 1
                self.diry = 0
                self.turns[self.head.pos[:]] = [self.dirx, self.diry]

            elif keys[pygame.K_UP] and self.diry != 1:
                self.dirx = 0
                self.diry = -1
                self.turns[self.head.pos[:]] = [self.dirx, self.diry]

            elif keys[pygame.K_DOWN] and self.diry != -1:
                self.dirx = 0
                self.diry = 1
                self.turns[self.head.pos[:]] = [self.dirx, self.diry]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.setDir(turn[0],turn[1])
                c.move()
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.dirx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows-1, c.pos[1])
                elif c.dirx == 1 and c.pos[0] >= c.rows-1:
                    c.pos = (0,c.pos[1])
                elif c.diry == 1 and c.pos[1] >= c.rows-1:
                    c.pos = (c.pos[0], 0)
                elif c.diry == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0],c.rows-1)
                else:
                    c.move()


    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirx, tail.diry

        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0]-1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0]+1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1]+1)))

        self.body[-1].dirx = dx
        self.body[-1].diry = dy


    def draw(self):
        for i, c in enumerate(self.body):
            c.draw()

    def reset(self, pos):
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirx = 0
        self.diry = 1



def drawGrid():
    dw = width // rows
    x = 0
    y = 0
    for n in range(rows):
        x += dw
        y += dw
        pygame.draw.line(window, (255, 255, 255), (x, 0), (x, height)) # Draw vertical lines
        pygame.draw.line(window, (255, 255, 255), (0, y), (width, y)) # Draw horizontal lines


def clearWindow():
    window.fill((0, 0, 0))


def generateRandomPos(forbiddenPos):
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        # Make sure the random pos that was generated won't be a position of a part of the snake.
        if len(list(filter(lambda z:z.pos == (x,y), forbiddenPos))) > 0:
            continue
        else:
            break

    return (x,y)


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    snake = Snake((255, 0, 0), (10, 10))
    snack = Cube(generateRandomPos(snake.body), color=(0,255,0))
    clock = pygame.time.Clock()
    while True:
        pygame.time.delay(50)
        clock.tick(10)
        snake.move()

        if snake.body[0].pos == snack.pos:
            snake.addCube()
            snack = Cube(generateRandomPos(snake.body), color=(0,255,0))

        head = snake.body[0]
        if head.pos in list(map(lambda z:z.pos,snake.body[1:])):
            print('Score: ', len(snake.body))
            message_box('You Lost!', 'Play again...')
            snake.reset((10,10))

        clearWindow()
        drawGrid()
        snake.draw()
        snack.draw()
        pygame.display.update()

main()
