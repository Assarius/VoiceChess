import pygame
import pygame_menu
import game


class Menu:
    def __init__(self, WIN):
        self.WIN = WIN

    def start_game_single(self):
        game.Game.main(players=1, WIN=self.WIN)

    def start_game_multi(self):
        game.Game.main(players=2, WIN=self.WIN)


    def draw_menu(self):
        pygame.init()
        menu = pygame_menu.Menu('VoiceChess', self.WIN.get_width(), self.WIN.get_height(), 
                                theme=pygame_menu.themes.THEME_BLUE)
        menu.add.button('SINGLEPLAYER', Menu.start_game_single, self)
        menu.add.button('MULTIPLAYER', Menu.start_game_multi, self)
        menu.add.button('WYJDŹ', pygame_menu.events.EXIT)
        menu.mainloop(self.WIN)
