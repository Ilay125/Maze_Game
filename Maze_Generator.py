from Generator import Generator
import pygame


def generation(rows, cols):
    gen = Generator(rows, cols)

    while not gen.done:
        gen.move()

    return gen.Grid.grid


def main():
    WIDTH = 800
    HEIGHT = 600

    rows = int(input("Rows: "))
    cols = int(input("Cols: "))

    cell_width = WIDTH // cols
    cell_height = HEIGHT // rows

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    maze = generation(rows, cols)

    pygame.init()

    win = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()

    while True:
        win.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        for r in range(rows):
            for c in range(cols):
                if not maze[c][r].up:
                    pygame.draw.line(win, BLACK, (c * cell_width, r * cell_height),
                                     ((c + 1) * cell_width, r * cell_height), 5)

                if maze[c][r].down:
                    pygame.draw.line(win, BLACK, (c * cell_width, (r + 1) * cell_height),
                                     ((c + 1) * cell_width, (r + 1) * cell_height), 5)

                if maze[c][r].left:
                    pygame.draw.line(win, BLACK, (c * cell_width, r * cell_height),
                                     (c * cell_width, (r + 1) * cell_height), 5)

                if maze[c][r].right:
                    pygame.draw.line(win, BLACK, ((c + 1) * cell_width, r * cell_height),
                                     ((c + 1) * cell_width, (r + 1) * cell_height), 5)

        pygame.draw.rect(win, GREEN, (maze.last[0] * cell_width, maze.last[1] * cell_height, cell_width, cell_height))

        pygame.draw.rect(win, RED, (maze.start[0] * cell_width, maze.start[1] * cell_height, cell_width, cell_height))

        clock.tick(30)
        pygame.display.update()

main()