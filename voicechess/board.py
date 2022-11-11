from math import ceil
import pygame

import fields

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

    def draw_board(self, history):
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
        self.display_history(history)
        pygame.display.update()

    def get_board(self):
        return self.BOARD

    def draw_pieces(self, BOARD, pos, history):
        BOARD.draw_board(history)
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

    def display_text(self, text):
        box = pygame.Rect(10 * self.fields_width + 1, 1, 6 * self.fields_width, 1 * self.fields_width - 1)
        font = pygame.font.Font(None, 32)
        board_color = (121, 103, 92)
        color = (255, 255, 255)
        text_surface = font.render(text, True, color)
        pygame.draw.rect(self.WIN, board_color, box, 0)
        self.WIN.blit(text_surface, (10 * self.fields_width + 5, 0.4 * self.fields_width))
        pygame.display.update()

    def display_history_field(self):
        box = pygame.Rect(10 * self.fields_width + 1, self.fields_width + 1, 6 * self.fields_width, 0.5 * self.fields_width - 1)
        font = pygame.font.Font(None, 32)
        board_color = (121, 103, 92)
        color = (255, 255, 255)
        text = "HISTORIA"
        text_surface = font.render(text, True, color)
        pygame.draw.rect(self.WIN, board_color, box, 0)

        self.WIN.blit(text_surface, (12.4 * self.fields_width + 5, self.fields_width + 5))
        pygame.display.update()

    def display_players_field(self, player):
        if player == 1:
            box = pygame.Rect(10 * self.fields_width + 1, 1.5 * self.fields_width + 1, 3 * self.fields_width - 1, 0.5 * self.fields_width - 1)
            text = "Gracz 1"
        if player == 2:
            box = pygame.Rect(13 * self.fields_width + 1, 1.5 * self.fields_width + 1, 3 * self.fields_width, 0.5 * self.fields_width - 1)
            text = "Gracz 2"
        font = pygame.font.Font(None, 32)
        board_color = (121, 103, 92)
        color = (255, 255, 255)
        
        text_surface = font.render(text, True, color)
        pygame.draw.rect(self.WIN, board_color, box, 0)

        if player == 1:
            self.WIN.blit(text_surface, (11 * self.fields_width + 5, 1.7 * self.fields_width + 5))
        if player == 2:
            self.WIN.blit(text_surface, (14 * self.fields_width + 5, 1.7 * self.fields_width + 5))
        pygame.display.update()

    def display_history(self, hist):
        self.display_history_field()
        self.display_players_field(1)
        self.display_players_field(2)
        box1 = pygame.Rect(10 * self.fields_width + 1, 2 * self.fields_width + 1, 3 * self.fields_width - 1, 8.5 * self.fields_width)
        box2 = pygame.Rect(13 * self.fields_width + 1, 2 * self.fields_width + 1, 3 * self.fields_width - 1, 8.5 * self.fields_width)
        font = pygame.font.Font(None, 32)
        board_color = (121, 103, 92)
        color = (255, 255, 255)
        pygame.draw.rect(self.WIN, board_color, box1, 0)
        pygame.draw.rect(self.WIN, board_color, box2, 0)
        for count, move in enumerate(hist):
            
            if count%2 ==0:
                text_surface = font.render(str(ceil((count+1)/2))+': '+move, True, color)
                self.WIN.blit(text_surface, (10 * self.fields_width + 5, 2 * self.fields_width + 5 + count * self.fields_width * 0.15))
            else:
                text_surface = font.render(str(int((count+1)/2))+': '+move, True, color)
                self.WIN.blit(text_surface, (13 * self.fields_width + 5, 2 * self.fields_width + 5 + count * self.fields_width * 0.15 - self.fields_width * 0.15))
        pygame.display.update()
