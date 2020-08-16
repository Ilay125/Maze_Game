import pygame
from Classes.Generator import Generator

def generation(rows, cols):
    gen = Generator(rows, cols)

    while not gen.done:
        gen.move()

    return gen.Grid.grid, gen.start, gen.last

