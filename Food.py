import random


class Food:
    """Class that models the food object in the game
    parameters: x = list of x values of all the food objects
                y = list of y coordinates of all the food objects
                quantity = number of food objects currently present in the game
                eaten = number of food objects that have been eaten so far
                level = The difficulty level of the game. Initial level is 1
    """
    def __init__(self):
        pass

    def generate_food(self):
        """
        Generates food objects according to the level of the game. Higher level
        means higher number of food objects will be present in the game. Food
        is generated at random locations within the dimensions of the screen(800
        *600)
        :return:None

        >>> food = Food()
        >>> food.generate_food()
        >>> food.quantity
        1
        >>> food.level = 3
        >>> food.generate_food()
        >>> food.quantity
        3
        """


    def get_eaten(self, index):
        """
        Carries out procedures that represent food being eaten at a particular
        index from the coordinates list.
        :param index: the index of the food being eaten in both, self.x and
        self.y
        :return: None

        >>> food = Food()
        >>> food.generate_food()
        >>> coorx = food.x[0]
        >>> coory = food.y[0]
        >>> food.get_eaten(0)
        >>> coorx in food.x and coory in food.y
        False
        >>> len(food.x)
        1
        """

    def set_level(self):
        """
        This method increments the level according to how much food has been
        eaten.
        :return: None
        """

