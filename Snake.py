import pygame

width = 500
height = 500
rows = 20
window = pygame.display.set_mode((width, height))

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
    # snake = Snake((255, 0, 0), (10, 10))

    clock = pygame.time.Clock()
    while True:
        pygame.time.delay(50)
        clock.tick(10)
        clearWindow()
        drawGrid()
        pygame.display.update()

main()
