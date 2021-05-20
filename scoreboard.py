from turtle import Turtle

FONT_SCORE = ("Courier", 24, "normal")
FONT_END = ("Courier", 36, "normal")

ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self, boundary_width, boundary_height):
        '''
        Creates a ScoreBoard object and also draws the boundary of the game
        :param boundary_width: width of the boundary of the snake game
        :param boundary_height: height of the boundary of the snake game
        '''
        super().__init__()
        self.penup()
        self.b_width = boundary_width
        self.b_height = boundary_height
        self.draw_boundary()
        self.score = 0
        self.write(arg="Score: " + str(self.score), align=ALIGNMENT,
                   font=FONT_SCORE)
        self.hideturtle()

    def update_score(self):
        '''
        Updates the score of the user
        :return: none
        '''
        self.clear()
        self.goto(0, 270)
        self.score += 1
        self.write(arg=f'Score: {self.score}', align="center",
                   font=FONT_SCORE)
        self.draw_boundary()

    def collision_check(self, snake_object):
        '''
        Checkes if the snake has collided with itself or with the boundary of
        the game
        :param snake_object: the snake object
        :return: true if there is collision of some sort and false otherwise
        '''
        # return True in case of collision
        boundary_width = self.b_width
        boundary_height = self.b_height
        curr_x = snake_object.snake[0].xcor()
        curr_y = snake_object.snake[0].ycor()
        if curr_x >= boundary_width or curr_x <= (-1) * boundary_width or \
                curr_y >= boundary_height or curr_y <= (-1) * boundary_height:
            self.goto(0.0, 0.0)
            self.write(arg="GAME OVER",
                       align=ALIGNMENT, font=FONT_END)
            return True
        # checking for self collision among snake
        else:
            for snake_portion in snake_object.snake[1:]:
                if snake_object.snake[0].distance(
                        snake_portion.position()) < 10:
                    self.goto(0.0, 0.0)
                    self.write(arg="GAME OVER",
                               align=ALIGNMENT, font=FONT_END)
                    return True
            return False

    def draw_boundary(self):
        '''
        draws the boundary of the snake game
        :return: none
        '''
        self.color("#00204a")
        x_cor = self.b_height
        y_cor = self.b_width
        self.goto(x_cor, y_cor)
        self.pendown()
        self.goto(x_cor, (-1 * y_cor))
        self.goto((-1 * x_cor), (-1 * y_cor))
        self.goto((-1 * x_cor), y_cor)
        self.goto(x_cor, y_cor)
        self.penup()
        self.goto(0, 270)
        self.color("#ff7b54")
