import pygame
import threading
from Classes.Generator import Generator
import os
from random import randint
from Classes.Console import Console
from time import time

pygame.init()

WIDTH = 1200
HEIGHT = 1000

sidebar_width = 200

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARKRED = (180, 0, 0)
CYAN = (0, 255, 255)
DARKCYAN = (0, 180, 180)
GRAY = (150, 150, 150)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator: The Gaem Edition")

clock = pygame.time.Clock()

folder_path = os.path.dirname(__file__)
image_dir = os.path.join(folder_path, "images")

loadingrun = False


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

def timer(start_time):
    this_time = int(time()-start_time)
    minutes = str(this_time//60) if len(str(this_time//60)) > 1 else f"0{str(this_time//60)}"
    seconds = str(this_time%60) if len(str(this_time%60)) > 1 else f"0{str(this_time%60)}"

    return f"{minutes}:{seconds}"


def loading_screen():
    state = 0

    x1 = WIDTH/2-105
    x2 = WIDTH/2
    square_state = 0

    while loadingrun:
        clock.tick(5)
        win.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        loading_text = "Loading"+"."*state
        button(loading_text, 0, 0, WIDTH, HEIGHT, WHITE, WHITE, fontSize=200, tcolor=RED)

        state += 1

        if state > 3:
            state = 0

        pygame.draw.rect(win, CYAN, (x1, HEIGHT-250, 100, 100))
        pygame.draw.rect(win, CYAN, (x2, HEIGHT-140, 100, 100))

        square_state += 1

        if (square_state // 2) % 2 == 0:
            x1 = WIDTH / 2 - 105
            x2 = WIDTH / 2
        else:
            x2 = WIDTH / 2 - 105
            x1 = WIDTH / 2

        pygame.display.update()


def verify_custom_form(args):
    rows, cols, buttons, theme = args
    if (rows == "" or rows == "_") and (cols == "" or cols == "_") and (buttons == "" or buttons == "_") and (theme == "" or theme == "_"):
        custom_form()
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
        if rows * cols - 2 < buttons:
            custom_form(True)
    else:
        custom_form(True)

    if theme.lower() not in ["dungeon", "futuristic", "mordor"]:
        custom_form(True)

    custom(rows, cols, theme, buttons)


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
                if event.key == pygame.K_ESCAPE:
                    menu()
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
                        rows_console.write(event.unicode, True)
                    elif index == 1:
                        cols_console.write(event.unicode, True)
                    elif index == 2:
                        buttons_console.write(event.unicode, True)
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


def generation(rows, cols, buttons):
    gen = Generator(rows, cols)

    while not gen.done:
        gen.move()

    return gen.Grid.grid, gen.start, gen.last, gen.random_buttons(buttons)


def finish(timer, mode):
    global loadingrun
    while True:
        win.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("YOU FINISHED THE LEVEL!", 0, 0, WIDTH, HEIGHT-200, WHITE, WHITE, tcolor=CYAN, fontSize=100)
        write(f"Time: {timer}", WIDTH // 2 - 200, 450, size=100)


        if mode == "custom":
            button("Main Menu", WIDTH // 2 - 200, HEIGHT // 2 + 300, 450, 150, DARKRED, RED, fontSize=50, action=menu)
        else:
            loadingrun = True
            button("Next Level", WIDTH // 2 - 500, HEIGHT // 2 + 300, 450, 150, DARKCYAN, CYAN, fontSize=50, action=loading_screen)
            #TODO main game
            button("Main Menu", WIDTH // 2 + 100, HEIGHT // 2 + 300, 450, 150, DARKRED, RED, fontSize=50, action=menu)


        clock.tick(30)
        pygame.display.update()



def custom(rows, cols, theme, buttons):
    global loadingrun
    loadingrun = True
    threading.Thread(target=loading_screen).start()
    grid, startpoint, endpoint, button_list = generation(rows, cols, buttons)
    loadingrun = False

    cell_width = (WIDTH-sidebar_width) / cols
    cell_height = HEIGHT / rows

    theme_dir = os.path.join(image_dir, "themes")
    themes = os.path.join(theme_dir, theme)

    normal_block = pygame.image.load(os.path.join(themes, "normal.png"))
    normal_block = pygame.transform.scale(normal_block, (int(cell_width) * 5, int(cell_height) * 5))
    special_block = pygame.image.load(os.path.join(themes, "special.png"))
    special_block = pygame.transform.scale(special_block, (int(cell_width) * 5, int(cell_height) * 5))
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

    wall_color = BLACK if theme == "futuristic" else WHITE

    for r in range(rows//5):
        for c in range(cols//5):
            if randint(1, 10) == 10:
                specialblocklist.append([c, r])

    cursor_rad = 8
    cx = startpoint[0]
    cy = startpoint[1]

    start_time = time()

    while True:

        win.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_UP or event.key == pygame.K_w) and grid[cx][cy].up:
                    if cy > 0:
                        cy -= 1
                if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and grid[cx][cy].down:
                    if cy < cols-1:
                        cy += 1
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and grid[cx][cy].left:
                    if cx > 0:
                        cx -= 1
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and grid[cx][cy].right:
                    if cx < rows-1:
                        cx += 1
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if not isopen:
            for b in button_list:
                if b[0] == cx and b[1] == cy:
                    b[2] = True
            count = 0
            for b in button_list:
                if b[2]:
                    count += 1
            if count == len(button_list):
                isopen = True
        else:
            if cx == endpoint[0] and cy == endpoint[1]:
                finish(timer(start_time), "custom")

        for r in range(rows//5+1):
            for c in range(cols//5+1):

                for s in specialblocklist:
                    if s[0] == c and s[1] == r:
                        win.blit(special_block, (c*int(cell_width)*5, r*int(cell_height)*5))
                        break
                else:
                    win.blit(normal_block, (c*int(cell_width)*5, r*int(cell_height)*5))

        for r in range(rows):
            for c in range(cols):
                for b in button_list:
                    if b[0] != c or b[1] != r:
                        continue
                    win.blit(on_button if b[2] else off_button, (c*cell_width, r*cell_height))

                if endpoint[0] == c and endpoint[1] == r:
                    win.blit(opened_trapdoor if isopen else closed_trapdoor, (c*cell_width, r*cell_height))

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

        pygame.draw.rect(win, CYAN if theme == "futuristic" else GRAY, (1000, 0, 200, HEIGHT))
        pygame.draw.line(win, BLACK, (1000, 0), (1000, HEIGHT))
        write("The Maze Gaem", 1010, 20, color=WHITE if theme == "futuristic" else BLACK)
        write(f"Time: {timer(start_time)}", 1010, 100, color=WHITE if theme == "futuristic" else BLACK)
        write(f"{buttons-count} {'buttons' if buttons-count != 1 else 'button'} left", 1010, 150, color=WHITE if theme == "futuristic" else BLACK)
        write(f"out of {buttons} {'buttons' if buttons != 1 else 'button'}", 1010, 180, color=WHITE if theme == "futuristic" else BLACK)
        write(f"Rows: {rows}", 1010, 230, color=WHITE if theme == "futuristic" else BLACK)
        write(f"Cols: {cols}", 1010, 280, color=WHITE if theme == "futuristic" else BLACK)
        write(f"Theme:", 1010, 330, color=WHITE if theme == "futuristic" else BLACK)
        write(f"{theme}", 1010, 360, color=WHITE if theme == "futuristic" else BLACK)

        pygame.draw.circle(win, WHITE if theme == "mordor" else BLACK,
                           (int(cx*cell_width+cell_width/2), int(cy*cell_height+cell_height/2)), cursor_rad)

        clock.tick(255)
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
        button("Custom", WIDTH // 2 - 225, HEIGHT // 2 + 125, 450, 150, DARKRED, RED, action=custom_form, fontSize=50)

        clock.tick(30)
        pygame.display.update()



menu()

