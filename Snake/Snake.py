class Snake:
    def __init__(self, x, y, length = 3):
        self.length = length
        self.body = [(x, y)]
        self.direction = 0

        for i in range(1, length):
            self.body.append((x, y + i))

    def move(self):
        '''
        Moves the entire snake one space
        '''

    def eat(self):
        '''
        Adds a new segment to the snake.
        '''

    def turn(self):
        '''
        Sets the direction of the snake.
        '''

    def draw(self):
        '''
        Draws the snake to the screen.
        '''
    
