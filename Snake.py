import pygame

width = 500
height = 500
rows = 20
window = pygame.display.set_mode((width, height))


class Cube(object):

    rows = 20
    width = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color


    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)


    def draw(self):
        dis = self.width // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(window, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))


class Snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dirx = 0
        self.diry = 1


    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.dirnx = -1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_RIGHT]:
                self.dirnx = 1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_UP]:
                self.dirnx = 0
                self.dirny = -1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_DOWN]:
                self.dirnx = 0
                self.dirny = 1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move(c.dirnx,c.dirny)


    def addCube(self):
        pass


    def draw(self):
        for i, c in enumerate(self.body):
            c.draw()


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


def main():
    snake = Snake((255, 0, 0), (10, 10))
    clock = pygame.time.Clock()
    while True:
        pygame.time.delay(50)
        clock.tick(10)
        clearWindow()
        drawGrid()
        snake.move()
        snake.draw()
        pygame.display.update()

main()
