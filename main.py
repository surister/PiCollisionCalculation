import pygame
from game import Game

if __name__ == '__main__':

    g = Game()
    while g.running:
        g.new()

pygame.quit()
