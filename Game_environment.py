import pygame
from Snake import Snake
from Food import Food
class Game_environment:
    """
    Class that models the enviroment in which the game is played.
    instance variables: screen = the pygame display
                        surface = the pygame surface
                        snake = A list of Snake ovjects
                        fps = The speed of the game
                        dir_change_location = A dictionary of coordinates pointing to directions
                        food = A Food object
    """
    def __init__(self):


    def events(self):
        """
        Contains the event loop for the pygame window
        :return: None
        """

    def update_position(self, pressed, x_coord, y_coord):
        """
        Method to make sure that all snake objects change direction at given point
        :param pressed: A pygame key object
        :param x_coord: The x coordinate where the change in direction happens
        :param y_coord: The y coordinate where the change in direction happens
        :return: None
        """


    def check_wall(self):
        """
        Method to check if the snake's head has hit the wall. Ends the game if
        so.
        :return: None
        """

    def check_food(self):
        """
        Checks if the snake has passed a food object. Makes appropriate changes
        if it has
        :return:
        """


if __name__ == '__main__':
    pygame.init()
    env = Game_environment()
    env.events()