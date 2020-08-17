import pygame
import threading
from Classes.Generator import Generator
import os

pygame.init()

WIDTH = 1200
HEIGHT = 1000

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARKRED = (180, 0, 0)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator: The Gaem Edition")

clock = pygame.time.Clock()

folder_path = os.path.dirname(__file__)
image_dir = os.path.join(folder_path, "images")

def action(args):
    pass

def button(msg, x, y, w, h, ic, ac, font="arial", fontSize=30, tcolor=BLACK, action=None, args=None):
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
    win.blit(screen_text, (x-screen_text.get_rect().width/2+w/2, y-screen_text.get_rect().height/2+h/2))


def generation(rows, cols):
    gen = Generator(rows, cols)

    while not gen.done:
        gen.move()

    return gen.Grid.grid, gen.start, gen.last

def menu():
    menu_dir = os.path.join(image_dir, "menu")
    title_img = pygame.image.load(os.path.join(menu_dir, "title.png"))

    while True:
        win.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.blit(title_img, (0, 0))

        button("Start", WIDTH//2-225, HEIGHT//2-75, 450, 150, DARKRED, RED, fontSize=50)
        button("Custom", WIDTH // 2 - 225, HEIGHT // 2 + 125, 450, 150, DARKRED, RED, fontSize=50)

        clock.tick(30)
        pygame.display.update()

menu()
