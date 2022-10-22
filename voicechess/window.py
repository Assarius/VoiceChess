import pygame
import pyautogui

import fields

class Window:
    def __init__(self):
        self.WIDTH, self.HEIGHT = pyautogui.size()
        self.WIDTH, self.HEIGHT = fields.empty_field.get_width(),\
                                  fields.empty_field.get_height()
        WIDTH, HEIGHT = 16 * self.WIDTH, 10 * self.HEIGHT
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #, pygame.FULLSCREEN)
        pygame.display.set_caption("VoiceChess")

    def get_window(self):
        return self.WIN

    def get_height(self):
        return self.HEIGHT

    def get_width(self):
        return self.WIDTH

    def scale_assets(self):
        scale = (int(self.HEIGHT/10-10), int(self.HEIGHT/10-10))
        fields.white_king = pygame.transform.scale(fields.white_king, scale)
        fields.black_king = pygame.transform.scale(fields.black_king, scale)
        fields.white_queen = pygame.transform.scale(fields.white_queen, scale)
        fields.black_queen = pygame.transform.scale(fields.black_queen, scale)
        fields.white_rook = pygame.transform.scale(fields.white_rook, scale)
        fields.black_rook = pygame.transform.scale(fields.black_rook, scale)
        fields.white_knight = pygame.transform.scale(fields.white_knight, scale)
        fields.black_knight = pygame.transform.scale(fields.black_knight, scale)
        fields.white_bishop = pygame.transform.scale(fields.white_bishop, scale)
        fields.black_bishop = pygame.transform.scale(fields.black_bishop, scale)
        fields.white_pawn = pygame.transform.scale(fields.white_pawn, scale)
        fields.black_pawn = pygame.transform.scale(fields.black_pawn, scale)
        fields.white_field = pygame.transform.scale(fields.white_field, scale)
        fields.black_field = pygame.transform.scale(fields.black_field, scale)
        fields.selected_field = pygame.transform.scale(fields.selected_field, scale)
        fields.empty_field = pygame.transform.scale(fields.empty_field, scale)
        fields.frame_field = pygame.transform.scale(fields.frame_field, scale)
        fields.field_1 = pygame.transform.scale(fields.field_1, scale)
        fields.field_2 = pygame.transform.scale(fields.field_2, scale)
        fields.field_3 = pygame.transform.scale(fields.field_3, scale)
        fields.field_4 = pygame.transform.scale(fields.field_4, scale)
        fields.field_5 = pygame.transform.scale(fields.field_5, scale)
        fields.field_6 = pygame.transform.scale(fields.field_6, scale)
        fields.field_7 = pygame.transform.scale(fields.field_7, scale)
        fields.field_8 = pygame.transform.scale(fields.field_8, scale)
        fields.field_A = pygame.transform.scale(fields.field_A, scale)
        fields.field_B = pygame.transform.scale(fields.field_B, scale)
        fields.field_C = pygame.transform.scale(fields.field_C, scale)
        fields.field_D = pygame.transform.scale(fields.field_D, scale)
        fields.field_E = pygame.transform.scale(fields.field_E, scale)
        fields.field_F = pygame.transform.scale(fields.field_F, scale)
        fields.field_G = pygame.transform.scale(fields.field_G, scale)
        fields.field_H = pygame.transform.scale(fields.field_H, scale)
        
