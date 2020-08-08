from Generator import Generator
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 800

rows = int(input("Rows: "))
cols = int(input("Cols: "))
FPS = int(input("Speed (FPS): "))

cell_width = WIDTH//cols
cell_height = HEIGHT//rows

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def main():
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
                if data_analysis_mode and event.key == pygame.K_UP:
                    gen.move()

        if not data_analysis_mode:
            gen.move()

        pygame.draw.rect(win, PURPLE, (gen.loc[0] * cell_width, gen.loc[1] * cell_height, cell_width, cell_height))

        for i in range(rows + 1):
            pygame.draw.line(win, BLACK, (0, i*cell_height), (WIDTH, i*cell_height), 5)

        for i in range(cols + 1):
            pygame.draw.line(win, BLACK, (i*cell_width, 0), (i*cell_width, HEIGHT), 5)

        for r in range(rows):
            for c in range(cols):
                if gen.Grid.grid[c][r].up:
                    pygame.draw.line(win, RED, (c*cell_width, r*cell_height), ((c+1)*cell_width, r*cell_height), 5)

                if gen.Grid.grid[c][r].down:
                    pygame.draw.line(win, RED, (c*cell_width, r*cell_height), ((c-1)*cell_width, r*cell_height), 5)

                if gen.Grid.grid[c][r].left:
                    pygame.draw.line(win, RED, (c*cell_width, r*cell_height), (c*cell_width, (r-1)*cell_height), 5)

                if gen.Grid.grid[c][r].right:
                    pygame.draw.line(win, RED, (c*cell_width, r*cell_height), (c*cell_width, (r+1)*cell_height), 5)


        clock.tick(FPS)
        pygame.display.update()


main()