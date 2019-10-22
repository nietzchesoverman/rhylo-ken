class Snake:
    """
        class to represent a single snake object
        instance variables:
        x_coord = the x coordinate of this snake object
        y_coord = the y coordinate of this snake object
        direction = the direction this snake object is moving in
        """
    def __init__(self, x_value, y_value, direction):


    def get_position(self):
        """
                returns the x and y coordinates of this snake object
                :return: a tuple containing the coordinates
        >>> snake = Snake(50, 75, 'u')
        >>> snake.get_position()
        (50, 75)
        """

    def move(self, key_pressed):
        """
                Moves a single snake object in the given direction
                :param key_pressed: 'u', 'd', 'r' or 'l' representing up, down, right or left respectively
                :return: None
        >>> snake = Snake(50, 75, 'u')
        >>> snake.move('r')
        >>> snake.direction
        'r'
        >>> snake.x_coord
        51
        >>> snake.move('d')
        >>> snake.direction
        'd'
        >>> snake.y_coord
        74
        >>> snake.move('u')
        >>> snake.direction
        'd'
        >>> snake.y_coord
        73
        """


    def get_next_snake(self):
        """
                creates another snake object, hence increasing the length of
                the entire snake. The new snake object has the same direction
                as the current snake object. One snake object has dimensions of
                20 (an is square), so the position of the new snake object has
                to be shifted by 20 in the appropriate direction
                :return: Snake

         >>> snake = Snake(50, 75, 'u')
         >>> snake2 = snake.get_next_snake()
         >>> snake2.direction
         'u'
         >>> snake2.x_coord
         50
         >>> snake2.y_coord
         55
        """
