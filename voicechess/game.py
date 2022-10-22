from math import ceil
import re
import time
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
                # if event.type == pygame.QUIT:
                #     exit()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                BOARD.draw_pieces(BOARD, hist[-1], hist_moves) 
                pygame.display.update()
                pygame.event.poll()
                if players == 1:
                    player1 = player.Player("Gracz", BOARD)
                    player1.player_move(hist, hist_moves)
                    BOARD.draw_pieces(BOARD, hist[-1].rotate(), hist_moves)
                    pygame.display.update()
                    pygame.event.poll()
                    player1.engine_move(searcher, hist, hist_moves)
                    pygame.display.update()
                    pygame.event.poll()

                # else:
                #     player1 = Player("Gracz_1")
                #     player2 = Player("Gracz_2")

                    
