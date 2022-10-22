import pygame

def init():
    global white_king, black_king, white_queen, black_queen, white_rook,\
           black_rook, white_knight, black_knight, white_bishop, black_bishop,\
           white_pawn, black_pawn, white_field, black_field, selected_field,\
           empty_field, frame_field, field_1, field_2, field_3, field_4, field_5,\
           field_6, field_7, field_8, field_A, field_B, field_C, field_D, field_E,\
           field_F, field_G, field_H
    white_king = pygame.image.load('./voicechess/Assets/Pieces/White_King.png')
    black_king = pygame.image.load('./voicechess/Assets/Pieces/Black_King.png')
    white_queen = pygame.image.load('./voicechess/Assets/Pieces/White_Queen.png')
    black_queen = pygame.image.load('./voicechess/Assets/Pieces/Black_Queen.png')
    white_rook = pygame.image.load('./voicechess/Assets/Pieces/White_Rook.png')
    black_rook = pygame.image.load('./voicechess/Assets/Pieces/Black_Rook.png')
    white_knight = pygame.image.load('./voicechess/Assets/Pieces/White_Knight.png')
    black_knight = pygame.image.load('./voicechess/Assets/Pieces/Black_Knight.png')
    white_bishop = pygame.image.load('./voicechess/Assets/Pieces/White_Bishop.png')
    black_bishop = pygame.image.load('./voicechess/Assets/Pieces/Black_Bishop.png')
    white_pawn = pygame.image.load('./voicechess/Assets/Pieces/White_Pawn.png')
    black_pawn = pygame.image.load('./voicechess/Assets/Pieces/Black_Pawn.png')
    white_field = pygame.image.load('./voicechess/Assets/Board/White_Pole.png')
    black_field = pygame.image.load('./voicechess/Assets/Board/Black_Pole.png')
    selected_field = pygame.image.load('./voicechess/Assets/Board/Selected_Pole.png')
    empty_field = pygame.image.load('./voicechess/Assets/Board/Empty_Pole.png')
    frame_field = pygame.image.load('./voicechess/Assets/Board/Board_Pole.png')
    field_1 = pygame.image.load('./voicechess/Assets/Board/1.png')
    field_2 = pygame.image.load('./voicechess/Assets/Board/2.png')
    field_3 = pygame.image.load('./voicechess/Assets/Board/3.png')
    field_4 = pygame.image.load('./voicechess/Assets/Board/4.png')
    field_5 = pygame.image.load('./voicechess/Assets/Board/5.png')
    field_6 = pygame.image.load('./voicechess/Assets/Board/6.png')
    field_7 = pygame.image.load('./voicechess/Assets/Board/7.png')
    field_8 = pygame.image.load('./voicechess/Assets/Board/8.png')
    field_A = pygame.image.load('./voicechess/Assets/Board/A.png')
    field_B = pygame.image.load('./voicechess/Assets/Board/B.png')
    field_C = pygame.image.load('./voicechess/Assets/Board/C.png')
    field_D = pygame.image.load('./voicechess/Assets/Board/D.png')
    field_E = pygame.image.load('./voicechess/Assets/Board/E.png')
    field_F = pygame.image.load('./voicechess/Assets/Board/F.png')
    field_G = pygame.image.load('./voicechess/Assets/Board/G.png')
    field_H = pygame.image.load('./voicechess/Assets/Board/H.png')
