import pygame
import threading
from Classes.Generator import Generator
import os
from random import randint

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


def generation(rows, cols, buttons):
    gen = Generator(rows, cols)

    while not gen.done:
        gen.move()

    return gen.Grid.grid, gen.start, gen.last, gen.random_buttons(buttons)


def custom(rows, cols, theme, buttons):
    grid, startpoint, endpoint, button_list = generation(rows, cols, buttons)

    cell_width = WIDTH / cols
    cell_height = HEIGHT / rows

    theme_dir = os.path.join(image_dir, "themes")
    themes = os.path.join(theme_dir, theme)
    normal_block = pygame.image.load(os.path.join(themes, "normal.png"))
    normal_block = pygame.transform.scale(normal_block, (int(cell_width), int(cell_height)))
    special_block = pygame.image.load(os.path.join(themes, "special.png"))
    special_block = pygame.transform.scale(special_block, (int(cell_width), int(cell_height)))
    off_button = pygame.image.load(os.path.join(themes, "off_button.png"))
    off_button = pygame.transform.scale(off_button, (int(cell_width), int(cell_height)))
    on_button = pygame.image.load(os.path.join(themes, "on_button.png"))
    on_button = pygame.transform.scale(on_button, (int(cell_width), int(cell_height)))
    closed_trapdoor = pygame.image.load(os.path.join(themes, "closed_trapdoor.png"))
    closed_trapdoor = pygame.transform.scale(closed_trapdoor, (int(cell_width), int(cell_height)))
    opened_trapdoor = pygame.image.load(os.path.join(themes, "opened_trapdoor.png"))
    opened_trapdoor = pygame.transform.scale(opened_trapdoor, (int(cell_width), int(cell_height)))

    specialblocklist = []
    isopen = False

    wall_color = WHITE
    if theme == "futuristic":
        wall_color = BLACK

    for r in range(rows):
        for c in range(cols):
            if randint(1, 100) == 10:
                specialblocklist.append([c, r])

    while True:
        win.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        for r in range(rows):
            for c in range(cols):

                for s in specialblocklist:
                    if s[0] == c and s[1] == r:
                        win.blit(special_block, (c*cell_width, r*cell_height))
                        break
                else:
                    win.blit(normal_block, (c*cell_width, r*cell_height))

                for b in button_list:
                    if b[0] != c or b[1] != r:
                        continue
                    win.blit(on_button if b[2] else off_button, (c*cell_width, r*cell_height))

                if endpoint[0] == c and endpoint[1] == r:
                    if isopen:
                        win.blit(opened_trapdoor, (c*cell_width, r*cell_height))
                    else:
                        win.blit(closed_trapdoor, (c * cell_width, r * cell_height))

                if not grid[c][r].up:
                    pygame.draw.line(win, wall_color, (c * cell_width, r * cell_height),
                                     ((c + 1) * cell_width, r * cell_height), 1)

                if not grid[c][r].down:
                    pygame.draw.line(win, wall_color, (c * cell_width, (r + 1) * cell_height),
                                     ((c + 1) * cell_width, (r + 1) * cell_height), 1)

                if not grid[c][r].left:
                    pygame.draw.line(win, wall_color, (c * cell_width, r * cell_height),
                                     (c * cell_width, (r + 1) * cell_height), 1)

                if not grid[c][r].right:
                    pygame.draw.line(win, wall_color, ((c + 1) * cell_width, r * cell_height),
                                     ((c + 1) * cell_width, (r + 1) * cell_height), 1)

        clock.tick(60)
        pygame.display.update()

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


custom(50, 50, "dungeon", 5)
