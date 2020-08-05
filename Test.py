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
RED = (255, 0, 0)

win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def main():
    gen = Generator(rows, cols)

    while True:
        win.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        for i in range(rows + 1):
            pygame.draw.line(win, BLACK, (0, i*cell_height), (WIDTH, i*cell_height), 5)

        for i in range(cols + 1):
            pygame.draw.line(win, BLACK, (i*cell_width, 0), (i*cell_width, HEIGHT), 5)

        gen.move()

        clock.tick(FPS)
        pygame.display.update()


main()