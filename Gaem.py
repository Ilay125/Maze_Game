import pygame
import threading
from Classes.Generator import Generator

pygame.init()

WIDTH = 1000
HEIGHT = 1000

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

win = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def generation(rows, cols):
    gen = Generator(rows, cols)

    while not gen.done:
        gen.move()

    return gen.Grid.grid, gen.start, gen.last

def menu():
    while True:
        win.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



    clock.tick(30)
    pygame.display.update()
