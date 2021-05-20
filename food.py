from turtle import Turtle
import random

FOOD_COLOR = ["yellow", "red", "dark slate blue"]


class TurtleFood(Turtle):
    def __init__(self):
        '''
        Creates a food object for the snake
        '''
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        '''
        Draws the food of the snake at random places
        :return: none
        '''
        random_x_pos = random.randint(-240, 240)
        random_y_pos = random.randint(-240, 240)
        self.color(random.choice(FOOD_COLOR))
        self.goto(random_x_pos, random_y_pos)
