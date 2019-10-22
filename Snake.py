class Snake:
    """
        class to represent a single snake object
        instance variables:
        x_coord = the x coordinate of this snake object
        y_coord = the y coordinate of this snake object
        direction = the direction this snake object is moving in
        """
    def __init__(self, x_value, y_value, direction):

        self.x_coord = x_value
        self.y_coord = y_value
        self.direction = direction

    def get_position(self):
        """
                returns the x and y coordinates of this snake object
                :return: a tuple containing the coordinates
        >>> snake = Snake(50, 75, 'u')
        >>> snake.get_position()
        (50, 75)
        """
        return self.x_coord, self.y_coord

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
        76
        >>> snake.move('u')
        >>> snake.direction
        'd'
        >>> snake.y_coord
        77
        """
        if self.direction == 'u':

            if key_pressed == 'r':
                self.direction = 'r'
                self.x_coord += 1
            elif key_pressed == 'l':
                self.direction = 'l'
                self.x_coord -= 1
            else:
                self.y_coord -= 1

        elif self.direction == 'd':

            if key_pressed == 'r':
                self.direction = 'r'
                self.x_coord += 1
            elif key_pressed == 'l':
                self.direction = 'l'
                self.x_coord -= 1
            else:
                self.y_coord += 1

        elif self.direction == 'r':

            if key_pressed == 'u':
                self.direction = 'u'
                self.y_coord -= 1
            elif key_pressed == 'd':
                self.direction = 'd'
                self.y_coord += 1
            else:
                self.x_coord += 1

        else:

            if key_pressed == 'u':
                self.direction = 'u'
                self.y_coord -= 1
            elif key_pressed == 'd':
                self.direction = 'd'
                self.y_coord += 1
            else:
                self.x_coord -= 1

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
        if self.direction == 'u':
            x = self.x_coord
            y = self.y_coord - 20
            direction = self.direction
        elif self.direction == 'd':
            x = self.x_coord
            y = self.y_coord + 20
            direction = self.direction
        elif self.direction == 'r':
            x = self.x_coord + 20
            y = self.y_coord
            direction = self.direction
        else:
            x = self.x_coord - 20
            y = self.y_coord
            direction = self.direction

        return Snake(x, y, direction)

