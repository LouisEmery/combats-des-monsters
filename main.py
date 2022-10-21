import arcade
import arcade.gui
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
WINDOW_TITLE = "Arcade Tutoriel"

def main():
    arcade.create_text_sprite(text: "salut", )

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
    arcade.set_background_color(arcade.color.DARK_GRAY)
    arcade.start_render()
    arcade.draw_triangle_filled(0, 0,0, 480, 200, 480, arcade.color.GRAY)
    arcade.draw_triangle_filled(640, 0, 640, 480, 440, 480, arcade.color.GRAY)
    arcade.finish_render()
    arcade.run()


main()

