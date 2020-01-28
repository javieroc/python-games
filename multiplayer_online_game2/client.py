import pygame
from Network import Network

width = 800
height = 800
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

def draw_window(win, players):
    win.fill((255,255,255))
    for key, player in players.items():
        player.draw(win)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    socket = Network()
    player = socket.getData()
    print(player)
    while run:
        clock.tick(60)
        players = socket.send(player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        player.move()
        draw_window(win, players)

main()
