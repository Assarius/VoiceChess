import pygame

from sunfish import sunfish
from sunfish import compressed

import board
import player


class Game:
    def main(players, WIN):
        BOARD = board.Board(WIN)
        clock = pygame.time.Clock()
        run = True
        hist = [sunfish.Position(sunfish.initial, 0, (True,True), (True,True), 0, 0)]
        searcher = compressed.Searcher()
        hist_moves = []
        while run:
            clock.tick(60)
            pygame.event.pump()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                BOARD.draw_pieces(BOARD, hist[-1], hist_moves) 
                pygame.display.update()
                pygame.event.poll()
                if players == 1:
                    player1 = player.Player("Gracz", BOARD)
                    if hist[-1].score <= -sunfish.MATE_LOWER:
                        BOARD.display_text('Przegrałeś')
                        break
                    player1.player_move(hist, hist_moves, player=1)
                    BOARD.draw_pieces(BOARD, hist[-1].rotate(), hist_moves)
                    if hist[-1].score <= -sunfish.MATE_LOWER:
                        BOARD.display_text('Wygrałeś')
                        break
                    pygame.display.update()
                    pygame.event.poll()
                    player1.engine_move(searcher, hist, hist_moves)
                    pygame.display.update()
                    pygame.event.poll()

                elif players == 2:
                    player1 = player.Player("Gracz_1", BOARD)
                    player2 = player.Player("Gracz_2", BOARD)
                    player1.player_move(hist, hist_moves, player=1)
                    BOARD.draw_pieces(BOARD, hist[-1].rotate(), hist_moves)
                    if hist[-1].score <= -sunfish.MATE_LOWER:
                        BOARD.display_text(f'{player1.name} wygrał')
                        break
                    pygame.display.update()
                    pygame.event.poll()
                    player2.player_move(hist, hist_moves, player=2)
                    BOARD.draw_pieces(BOARD, hist[-1].rotate(), hist_moves)
                    if hist[-1].score <= -sunfish.MATE_LOWER:
                        BOARD.display_text(f'{player2.name} wygrał')
                        break
                    pygame.display.update()
                    pygame.event.poll()
        pygame.quit()
