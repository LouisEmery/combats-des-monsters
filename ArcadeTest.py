import arcade
import os
path = r'C:\Utilisateurs\emerylo\Documents'
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
WINDOW_TITLE = "Arcade Tutoriel"

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
    arcade.set_background_color(arcade.color.ASH_GREY)
    arcade.start_render()
    points = [(0, 0), (280, 200), (280,380), (0, 480)]
    arcade.draw_polygon_filled(points, arcade.color.GRAY)
    points = [(640, 0), (360, 200), (360, 380), (640, 480)]
    arcade.draw_polygon_filled(points, arcade.color.GRAY)
    points = [(280, 200), (360, 200), (360, 380), (280,380)]
    arcade.draw_polygon_filled(points, arcade.color.DARK_BROWN)
    arcade.draw_circle_filled(340, 270, 10, arcade.color.GRAY)
    sprite = arcade.Sprite("Documents/MONSTER_1.png", 1)

    arcade.finish_render()
    arcade.run()


main()