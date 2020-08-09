from Generator import Generator
import pygame
from time import time


def generation(rows, cols):
    gen = Generator(rows, cols)
    start_time = time()

    while not gen.done:
        gen.move()

    print(time()-start_time)
    return gen.Grid.grid, gen.start, gen.last


def main():
    WIDTH = 1000
    HEIGHT = 1000

    rows = int(input("Rows: "))
    cols = int(input("Cols: "))

    cell_width = WIDTH // cols
    cell_height = HEIGHT // rows

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    maze, start, last = generation(rows, cols)

    pygame.init()

    win = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()

    while True:
        win.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.draw.rect(win, GREEN, (last[0] * cell_width, last[1] * cell_height, cell_width, cell_height))

        pygame.draw.rect(win, RED, (start[0] * cell_width, start[1] * cell_height, cell_width, cell_height))

        for i in range(rows + 1):
            pygame.draw.line(win, BLACK, (0, i*cell_height), (WIDTH, i*cell_height), 1)

        for i in range(cols + 1):
            pygame.draw.line(win, BLACK, (i*cell_width, 0), (i*cell_width, HEIGHT), 1)

        for r in range(rows):
            for c in range(cols):
                if maze[c][r].up:
                    pygame.draw.line(win, WHITE, (c * cell_width, r * cell_height),
                                     ((c + 1) * cell_width, r * cell_height), 1)

                if maze[c][r].down:
                    pygame.draw.line(win, WHITE, (c * cell_width, (r + 1) * cell_height),
                                     ((c + 1) * cell_width, (r + 1) * cell_height), 1)

                if maze[c][r].left:
                    pygame.draw.line(win, WHITE, (c * cell_width, r * cell_height),
                                     (c * cell_width, (r + 1) * cell_height), 1)

                if maze[c][r].right:
                    pygame.draw.line(win, WHITE, ((c + 1) * cell_width, r * cell_height),
                                     ((c+1)*cell_width, (r+1)*cell_height), 1)



        clock.tick(30)
        pygame.display.update()

main()