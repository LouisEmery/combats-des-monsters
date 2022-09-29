import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
WINDOW_TITLE = "Arcade Tutoriel"

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
    arcade.set_background_color(arcade.color.BLUE)
    arcade.start_render()
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.csscolor.RED)
    arcade.draw_rectangle_filled(320, 400, SCREEN_WIDTH, SCREEN_HEIGHT / 3, arcade.csscolor.WHITE)
    arcade.finish_render()
    arcade.run()


main()