import pygame
import sys
from pygame.locals import *
import mygamefile
import resources

pygame.init()

FPS = 2
FramePerSec = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

DISPLAYSURF = pygame.display.set_mode((200, 200))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game of Life")


def main():
    game = mygamefile.Game()
    game.board = resources.BOARD_WITH_BLINKER_A
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        DISPLAYSURF.fill(BLACK)
        game.advance_to_next_generation()
        for i, column in enumerate(game.board):
            for j, row in enumerate(column):
                surf = pygame.Surface((10, 10))
                surf.fill(WHITE)
                if row == 1:
                    DISPLAYSURF.blit(surf, (j*10, i*10))
        # cell.draw()
        pygame.display.update()
        FramePerSec.tick(FPS)


if __name__ == "__main__":
    main()