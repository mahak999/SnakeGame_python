from turtle import Screen
from time import sleep
from snake import SnakeClass
from food import TurtleFood
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("#d6efc7")
screen.tracer(0)
screen.setup(width=600, height=600)
screen.listen()

snake = SnakeClass()
food = TurtleFood()
score = ScoreBoard(260, 260)

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
screen.update()
while game_on:
    sleep(0.1)
    snake.move_forward()
    if snake.get_head().distance(food.position()) < 15:
        # they have collided
        food.new_food()
        snake.size_increase()
        score.update_score(1)
    score.collision_check(snake)

    screen.update()

screen.exitonclick()
