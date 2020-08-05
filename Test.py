from Generator import Generator
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 800

FPS = 30

rows = int(input("Rows: "))
cols = int(input("Cols: "))

cell_width = WIDTH//cols
cell_height = HEIGHT//rows

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def main():
    gen = Generator(rows, cols)

    while True:
        win.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        for i in range(rows + 1):
            pygame.draw.line(win, BLACK, (0, i*cell_height), (WIDTH, i*cell_height), 5)

        for i in range(cols + 1):
            pygame.draw.line(win, BLACK, (i*cell_width, 0), (i*cell_width, HEIGHT), 5)

        gen.move()

        for r in range(rows):
            for c in range(cols):
                if gen.Grid.grid[c][r].up:
                    pygame.draw.line(win, RED, (c*cell_width, r*cell_height), ((c-1)*cell_width, r*cell_height), 5)

                if gen.Grid.grid[c][r].down:
                    pygame.draw.line(win, RED, (c*cell_width, r*cell_height), ((c+1)*cell_width, r*cell_height), 5)

                if gen.Grid.grid[c][r].left:
                    pygame.draw.line(win, RED, (c*cell_width, r*cell_height), (c*cell_width, (r-1)*cell_height), 5)

                if gen.Grid.grid[c][r].right:
                    pygame.draw.line(win, RED, (c*cell_width, r*cell_height), (c*cell_width, (r+1)*cell_height), 5)


        clock.tick(FPS)
        pygame.display.update()


main()