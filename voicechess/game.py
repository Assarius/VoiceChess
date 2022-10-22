from time import sleep
import fields
import pygame

from sunfish import sunfish
from sunfish import compressed


class Board:
    def __init__(self, WIN):
        self.BOARD = [  'FP',  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'FP',       # 0-9
                        '8',   'b', 'w', 'b', 'w', 'b', 'w', 'b', 'w', '8',        # 10-19
                        '7',   'w', 'b', 'w', 'b', 'w', 'b', 'w', 'b', '7',        # 20-29
                        '6',   'b', 'w', 'b', 'w', 'b', 'w', 'b', 'w', '6',        # 30-39
                        '5',   'w', 'b', 'w', 'b', 'w', 'b', 'w', 'b', '5',        # 40-49
                        '4',   'b', 'w', 'b', 'w', 'b', 'w', 'b', 'w', '4',        # 50-59
                        '3',   'w', 'b', 'w', 'b', 'w', 'b', 'w', 'b', '3',        # 60-69
                        '2',   'b', 'w', 'b', 'w', 'b', 'w', 'b', 'w', '2',        # 70-79
                        '1',   'w', 'b', 'w', 'b', 'w', 'b', 'w', 'b', '1',        # 80-89
                        'FP',  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'FP'        # 90-99
                        ]
        self.WIN = WIN
        self.fields_height = fields.empty_field.get_height()
        self.fields_width = fields.empty_field.get_width()

    def draw_board(self):
        self.WIN.fill((0, 0, 0))
        pos_x = 0
        pos_y = 0
        row = 1
        for i in self.BOARD:
            if i == 'FP': field = fields.frame_field
            if i == 'A': field = fields.field_A
            if i == 'B': field = fields.field_B
            if i == 'C': field = fields.field_C
            if i == 'D': field = fields.field_D
            if i == 'E': field = fields.field_E
            if i == 'F': field = fields.field_F
            if i == 'G': field = fields.field_G
            if i == 'H': field = fields.field_H
            if i == '1': field = fields.field_1
            if i == '2': field = fields.field_2
            if i == '3': field = fields.field_3
            if i == '4': field = fields.field_4
            if i == '5': field = fields.field_5
            if i == '6': field = fields.field_6
            if i == '7': field = fields.field_7
            if i == '8': field = fields.field_8
            if i == 'b': field = fields.black_field
            if i == 'w': field = fields.white_field
            if i == 's': field = fields.selected_field
            self.WIN.blit(field, (pos_x, pos_y))
            pos_x += self.fields_width
            if row%10 == 0:
                pos_y += self.fields_height
                pos_x = 0
            row += 1
        pygame.display.update()

    def get_board(self):
        return self.BOARD

    def draw_pieces(self, pos):
        uni_pieces = {'R':fields.white_rook, 'N':fields.white_knight, 'B':fields.white_bishop,
                    'Q':fields.white_queen, 'K':fields.white_king, 'P':fields.white_pawn,
                    'r':fields.black_rook, 'n':fields.black_knight, 'b':fields.black_bishop,
                    'q':fields.black_queen, 'k':fields.black_king, 'p':fields.black_pawn,
                    '.':fields.empty_field}
        pos_x = self.fields_width
        pos_y = self.fields_height
        for i, row in enumerate(pos.board.split()):
            for p in row:
                piece = uni_pieces.get(p, p)
                piece.get_rect(center=(pos_x/2, pos_y/2))
                self.WIN.blit(piece, (pos_x, pos_y))
                pos_x += self.fields_width
            pos_x = self.fields_width
            pos_y += self.fields_height

class Player:
    def __init__(self, name):
        self.name = name
        self.engine = "Sunfish"

    async def player_move():
        pass

    async def engine_move():
        pass

class Game:
    def main(players, WIN):
        
        BOARD = Board(WIN)
        clock = pygame.time.Clock()
        run = True
        hist = [sunfish.Position(sunfish.initial, 0, (True,True), (True,True), 0, 0)]
        searcher = compressed.Searcher()
        start_text = "Spacja aby rozpoczac"
        hist_moves = []

        while run:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                
                BOARD.draw_board()
                BOARD.draw_pieces(hist[-1]) 
                pygame.display.update()
                pygame.event.poll()
                if players == 1:
                    player = Player("Gracz")
                else:
                    player1 = Player("Gracz_1")
                    player2 = Player("Gracz_2")
                    
                    
