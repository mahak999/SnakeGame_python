from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
FONT_SIZE = 34
FONT = ("Courier", FONT_SIZE, "normal")
ALIGNMENT = "center"
INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class SnakeClass():
    def __init__(self):
        '''
        Creates the snake object for the game
        '''
        self.snake = []
        self.draw(3, INITIAL_POSITIONS)
        self.snake[0].color()

    def draw(self, length, position_list):
        '''
        Draws the snake on the screen as per the inputted length and
        position_list, which is the list of positions where the snake should
        be drawn
        :param length: The length of snake
        :param position_list: the list of positions for the snake
        :return: none
        '''
        for i in range(length):
            new_dot = Turtle()
            new_dot.penup()
            new_dot.shape("square")
            new_dot.color("#4a503d")
            new_dot.setx(position_list[i][0])
            new_dot.sety(position_list[i][1])
            new_dot.setheading(0)
            self.snake.append(new_dot)

    def move_forward(self):
        '''
        Makes the snake move forard in the same direction as the value of its
        head direction
        '''
        for i in range(len(self.snake) - 1, 0, -1):
            new_x_cor = self.snake[i - 1].xcor()
            new_y_cor = self.snake[i - 1].ycor()
            self.snake[i].goto(x=new_x_cor, y=new_y_cor)
        self.snake[0].forward(MOVE_DISTANCE)

    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)

    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)

    def get_head(self):
        return self.snake[0]

    def size_increase(self):
        self.draw(1, [self.snake[-1].position()])
