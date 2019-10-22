import pygame
from Snake import Snake
from Food import Food


class GameEnvironment:
    """
        Class that models the environment in which the game is played.
        instance variables: screen : the pygame display
                            surface : the pygame surface
                            snake : A list of Snake objects
                            fps : The speed of the game
                            dir_change_location : A dictionary of coordinates
                             pointing to directions to be followed at those
                             coordinates
                            food : A Food object
                            status : States whether the game is running or over
                            It is 1 if game is running, 0 if game is over.
        """
    def __init__(self):


    def events(self):
        """
                Contains the event loop for the pygame window.Rectangle
                images for the snake and the Circle images for food are created
                in this event loop. Calls to other GameEnvironment methods are
                made from here.
                :return: None
        """


    def update_position(self, pressed, x_coord, y_coord):
        """
        Method to make sure that all snake objects change direction at given
        point
        :param pressed: A pygame key object
        :param x_coord: The x coordinate where the change in direction happens
        :param y_coord: The y coordinate where the change in direction happens
        :return: None
        """


    def check_wall(self):
        """
        Method to check if the snake's head has hit the wall. Ends the game if
        this happens.
        :return: None
        """


    def check_food(self):
        """
        Checks if the snake has passed a food object. The length of the snake
        increases if this happens. Makes appropriate changes to the food object
        too.
        :return:
        """

    def check_suicide(self):
        """
        Checks if the snake turns into itself. Ends the game if this happens
        :return: None
        """

