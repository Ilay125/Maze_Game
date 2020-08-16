import pygame
import threading
from Classes.Generator import Generator

pygame.init()

WIDTH = 1200
HEIGHT = 1000

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARKRED = (180, 0, 0)

win = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def action(args):
    pass

def button(msg, x, y, w, h, ic, ac, xoffset = 10, yoffset = 10, font="arial", fontSize=30, tcolor=BLACK, action=None, args=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(win, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            if args is not None:
                action(args)
            else:
                action()
    else:
        pygame.draw.rect(win, ic, (x, y, w, h))

    font = pygame.font.SysFont(font, fontSize, True)
    screen_text = font.render(msg, True, tcolor)
    win.blit(screen_text, (x+(w/2)+xoffset, y+(h/2)+yoffset))


def generation(rows, cols):
    gen = Generator(rows, cols)

    while not gen.done:
        gen.move()

    return gen.Grid.grid, gen.start, gen.last

def menu():
    while True:
        win.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Start", WIDTH//2-75, HEIGHT//2-25, 150, 50, 10, -15, DARKRED, RED)
        button("Custom", WIDTH // 2 - 75, HEIGHT // 2 + 50, 150, 50, 10, -15, DARKRED, RED)

        clock.tick(30)
        pygame.display.update()

menu()
