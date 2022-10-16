import pygame
import pygame_menu


class Menu:

    def start_game_single():
        Game.main(1)

    def start_game_multi():
        Game.main(2)      


    def draw_menu(WIN):
        pygame.init()
        menu = pygame_menu.Menu('Blindfold chess', WIN.get_width(), WIN.get_height(), 
                                theme=pygame_menu.themes.THEME_BLUE)
        menu.add.button('SINGLEPLAYER', Menu.start_game_single)
        menu.add.button('MULTIPLAYER', Menu.start_game_multi)
        menu.add.button('WYJDŹ', pygame_menu.events.EXIT)
        menu.mainloop(WIN)