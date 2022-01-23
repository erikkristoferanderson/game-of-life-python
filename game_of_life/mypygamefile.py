import pygame
import sys
from pygame.locals import *
import mygamefile
from music import make_music, play_a_note
import resources

pygame.init()

FPS = 6
generation_frames = 3
FramePerSec = pygame.time.Clock()
input_wait_time = 1

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

DISPLAYSURF = pygame.display.set_mode((200, 200))
screen_width = 200
screen_height = 200
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game of Life")


def main():

    generation_counter = 0
    cursor_x = 9
    cursor_y = 9
    wait_for_input = 0
    paused = True
    play_a_song = False
    game = mygamefile.Game()
    prev_board = game.board
    # game.board = resources.BOARD_WITH_BLINKER_A
    while True:
        generation_counter += 1
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if not wait_for_input:
            pressed_keys = pygame.key.get_pressed()
            wait_for_input = input_wait_time
            if pressed_keys[K_e]:
                cursor_y -= 1
            if pressed_keys[K_d]:
                cursor_y += 1
            if pressed_keys[K_s]:
                cursor_x -= 1
            if pressed_keys[K_f]:
                cursor_x += 1
            if pressed_keys[K_SPACE]:
                paused = not paused
            if pressed_keys[K_RETURN]:
                game.swap_life_state(cursor_y, cursor_x)
                play_a_note(cursor_x)
        if wait_for_input > 0:
            wait_for_input -= 1
        DISPLAYSURF.fill(BLACK)
        if paused:
            pygame.draw.rect(DISPLAYSURF, RED, (0, 0, screen_width, screen_height), 3)

        if not paused:
            if generation_counter >= generation_frames:
                play_a_song = True
                game.advance_to_next_generation()
                generation_counter = 0





        for i, column in enumerate(game.board):
            for j, row in enumerate(column):
                surf = pygame.Surface((10, 10))
                surf.fill(WHITE)
                if row == 1:
                    DISPLAYSURF.blit(surf, (j*10, i*10))
        # cell.draw()
        pygame.draw.rect(DISPLAYSURF, GREEN, (cursor_x*10, cursor_y*10, 10, 10), 2)
        pygame.display.update()
        if play_a_song:
            make_music(game, prev_board)
            play_a_song = False
        FramePerSec.tick(FPS)
        prev_board = game.board


if __name__ == "__main__":
    main()