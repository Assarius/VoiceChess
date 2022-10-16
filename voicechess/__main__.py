import game
import menu
import fields


if __name__ == "__main__":
    fields.init()
    WIN = game.Window()
    WIN.prepare_window()
    menu.Menu.draw_menu(WIN.get_window())
