from Generator import Generator
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 800

rows = int(input("Rows: "))
cols = int(input("Cols: "))
info = input("Show info (Yes/No): ").lower()

cell_width = WIDTH//cols
cell_height = HEIGHT//rows

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (150, 150, 150)
CYAN = (0, 255, 255)
ORANGE = (255, 150, 0)

win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Maze Generator")
clock = pygame.time.Clock()


def write(txt, x, y, color, font="comicsansms", size=10, aa=True, angle=0):
    temp = pygame.font.SysFont(font, size)
    temp = temp.render(txt, aa, color)
    temp = pygame.transform.rotate(temp, angle)
    win.blit(temp, (x, y))


def main():
    FPS = 10
    gen = Generator(rows, cols)

    data_analysis_mode = False

    while True:

        win.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    data_analysis_mode = not data_analysis_mode
                if data_analysis_mode and event.key == pygame.K_UP and not gen.done:
                    gen.move()
                if not data_analysis_mode and event.key == pygame.K_RIGHT:
                    FPS = FPS+5 if FPS != 1 else 5
                if not data_analysis_mode and event.key == pygame.K_LEFT:
                    FPS = FPS-5 if FPS-5 > 0 else 1

        if not data_analysis_mode and not gen.done:
            gen.move()

        for c, r in gen.way:
            pygame.draw.rect(win, YELLOW if not gen.done else WHITE, (c * cell_width, r * cell_height, cell_width, cell_height))

        for c, r in gen.impossible:
            pygame.draw.rect(win, GRAY if not gen.done else WHITE, (c * cell_width, r * cell_height, cell_width, cell_height))

        if gen.done:
            pygame.draw.rect(win, ORANGE, (gen.last[0] * cell_width, gen.last[1] * cell_height, cell_width, cell_height))

        pygame.draw.rect(win, CYAN, (gen.start[0] * cell_width, gen.start[1] * cell_height, cell_width, cell_height))

        if not gen.done:
            pygame.draw.rect(win, PURPLE, (gen.loc[0] * cell_width, gen.loc[1] * cell_height, cell_width, cell_height))


        for i in range(rows + 1):
            pygame.draw.line(win, BLACK, (0, i*cell_height), (WIDTH, i*cell_height), 5)

        for i in range(cols + 1):
            pygame.draw.line(win, BLACK, (i*cell_width, 0), (i*cell_width, HEIGHT), 5)

        for r in range(rows):
            for c in range(cols):
                if gen.Grid.grid[c][r].up:
                    pygame.draw.line(win, RED if not gen.done else WHITE, (c*cell_width, r*cell_height), ((c+1)*cell_width, r*cell_height), 5)

                if gen.Grid.grid[c][r].down:
                    pygame.draw.line(win, RED if not gen.done else WHITE, (c*cell_width, (r+1)*cell_height),
                                     ((c+1)*cell_width, (r+1)*cell_height), 5)

                if gen.Grid.grid[c][r].left:
                    pygame.draw.line(win, RED if not gen.done else WHITE, (c*cell_width, r*cell_height), (c*cell_width, (r+1)*cell_height), 5)

                if gen.Grid.grid[c][r].right:
                    pygame.draw.line(win, RED if not gen.done else WHITE, ((c+1)*cell_width, r*cell_height), ((c+1)*cell_width, (r+1)*cell_height), 5)

        if not gen.done and info == "yes":
            for c in range(cols):
                for r in range(rows):
                    write("Up", c*cell_width+10, r*cell_height+10, GREEN if gen.Grid.grid[c][r].up else RED)
                    write("Down", c * cell_width + 10, r * cell_height + 20, GREEN if gen.Grid.grid[c][r].down else RED)
                    write("Left", c * cell_width + 10, r * cell_height + 30, GREEN if gen.Grid.grid[c][r].left else RED)
                    write("Right", c * cell_width + 10, r * cell_height + 40, GREEN if gen.Grid.grid[c][r].right else RED)


            write(f"Data analysis mode: {data_analysis_mode}", 5, HEIGHT-30, BLUE)
            write(f"FPS: {FPS}", 5, HEIGHT-20, BLUE)

        clock.tick(FPS)
        pygame.display.update()


main()