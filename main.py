from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Python Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.add_tail_segment()
        snake.increase_move_distance()
        screen.update()
    if snake.hit_the_wall(SCREEN_WIDTH/2 - 10, SCREEN_HEIGHT/2 - 10) or snake.hit_itself():
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()
