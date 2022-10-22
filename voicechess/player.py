import pygame
import re
import time

import speech
from sunfish import sunfish

class Player:
    def __init__(self, name, BOARD):
        self.name = name
        self.engine = "Sunfish"
        self.BOARD = BOARD

    def player_move(self, hist, hist_moves):
        print(f'Ruch gracza {self.name}')
        self.BOARD.display_text(f'Ruch gracza {self.name}')
        # self.BOARD.display_history(hist_moves)
        move = None
        tmp_move = None
        pygame.display.update()
        while move not in hist[-1].gen_moves():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                move = speech.get_pos()
                if move is not None and len(move) == 4:
                    match1 = re.match('(^[a-hA-H)])([1-8])([a-hA-H])([1-8])', move)
                    if match1:
                        print(f"Robie ruch {move}")
                        tmp_move = move 
                        move = sunfish.parse(move[0]+move[1]), sunfish.parse(move[2]+move[3])
                else:
                    self.BOARD.display_text("Podaj poprawny ruch np. d2d4")
                    match1 = None 
                    move = None

        hist.append(hist[-1].move(move))
        hist_moves.append(tmp_move.upper())

    def engine_move(self, searcher, hist, hist_moves):
        print(f'Ruch gracza {self.engine}')
        # pass
        self.BOARD.display_text(f'Ruch gracza {self.engine}')
        # self.BOARD.display_history(hist_moves)
        # Fire up the engine to look for a move.
        start = time.time()
        for _depth, move, score in searcher.search(hist[-1], hist):
            if time.time() - start > 1:
                break

        # if score == sunfish.MATE_UPPER:
            # Game.display_text("Szach-mat!")
            # Game.display_history(hist_moves)
        # The black player moves from a rotated position, so we have to
        # 'back rotate' the move before printing it.        
        # print("Mój ruch:", sunfish.render(119-move[0]) + sunfish.render(119-move[1]))
        text = sunfish.render(119-move[0]) + sunfish.render(119-move[1])    
        hist_moves.append(text.upper())
        print(f"Ruch {self.engine}: {text}")
        self.BOARD.display_text(f'Ruch {self.engine}: {text}')
        # self.BOARD.display_history(hist_moves)
        hist.append(hist[-1].move(move))