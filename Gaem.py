import pygame
import threading
from Classes.Generator import Generator
import os
from Classes.Console import Console

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


def write(txt, x, y, font="arial", color=BLACK, size=30, aa=True, angle=0):
    temp = pygame.font.SysFont(font, size, True)
    temp = temp.render(txt, aa, color)
    temp = pygame.transform.rotate(temp, angle)
    win.blit(temp, (x, y))


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


def verify_custom_form(args):
    rows, cols, buttons, theme = args
    if rows.isnumeric():
        rows = int(rows)
    else:
        custom_form(True)

    if cols.isnumeric():
        cols = int(cols)
    else:
        custom_form(True)

    if buttons.isnumeric():
        buttons = int(buttons)
    else:
        custom_form(True)

    if theme.lower() not in ["dungeon", "futuristic", "mordor"]:
        custom_form(True)

    print(rows, cols, theme, buttons)
    #custom(rows, cols, theme, buttons)



def custom_form(error=False):
    rows_console = Console()
    cols_console = Console(False)
    buttons_console = Console(False)
    theme_console = Console(False)

    consoles = [rows_console, cols_console, buttons_console, theme_console]

    index = 0

    while True:
        clock.tick(30)
        win.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN or event.key == pygame.K_TAB:
                    index += 1
                    if index > 3:
                        index = 0

                    consoles[index].active = True
                    consoles[index-1 if index > 0 else 3].active = False

                if event.key == pygame.K_UP:
                    index -= 1
                    if index < 0:
                        index = 3

                    consoles[index].active = True
                    consoles[index + 1 if index < 3 else 0].active = False

                if event.key == pygame.K_BACKSPACE:
                    if index == 0:
                        rows_console.delete()
                    elif index == 1:
                        cols_console.delete()
                    elif index == 2:
                        buttons_console.delete()
                    elif index == 3:
                        theme_console.delete()
                else:
                    if index == 0:
                        rows_console.write(event.unicode)
                    elif index == 1:
                        cols_console.write(event.unicode)
                    elif index == 2:
                        buttons_console.write(event.unicode)
                    elif index == 3:
                        theme_console.write(event.unicode)

        write(rows_console.txt, 300, 170, size=50)
        write(cols_console.txt, 270, 270, size=50)
        write(buttons_console.txt, 340, 370, size=50)
        write(theme_console.txt, 900, 470, size=50)

        arr_y = 185 + index * 100

        for i, console in enumerate(consoles):
            console.animation()
            console.txt = "_" if len(console.txt) == 0 and not console.active else console.txt

        pygame.draw.polygon(win, BLACK, ((125, arr_y), (125, arr_y + 30), (140, arr_y + 15)))

        write("Rows:", 150, 170, size=50)
        write("Cols:", 150, 270, size=50)
        write("Buttons:", 150, 370, size=50)
        write("Theme (Dungeon, Futuristic, Mordor):", 150, 470, size=50)

        write("*The input is invalid." if error else "", 150, 600, color=RED)

        button("Submit", WIDTH/2 - 225, HEIGHT - 300, 450, 150, DARKRED, RED, fontSize=50, action=verify_custom_form,
               args=(rows_console.txt, cols_console.txt, buttons_console.txt, theme_console.txt))
        pygame.display.update()


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

custom_form()
