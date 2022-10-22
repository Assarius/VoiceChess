import game
import menu
import fields
import window


if __name__ == "__main__":
    fields.init()
    WIN = window.Window()
    MENU = menu.Menu(WIN.get_window())
    MENU.draw_menu()
