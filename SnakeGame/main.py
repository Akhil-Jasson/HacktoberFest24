# Todo 1. Create a snake body
# TODO 2. Move the Snake
# TODO 3. Control the snake
# TODO 4. Detect collision with food
# TODO 5. Create a scoreboard
# TODO 6. Detect Collision with wall
# TODO 7. Detect collision with tail

from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


count = 0
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    snake.move()
    scoreboard.display()
    if snake.tur_list[0].distance(food) < 15:
        food.refresh()
        count += 1
        scoreboard.count = count
        scoreboard.score()
        snake.extend()

    if snake.tur_list[0].xcor() > 280 or snake.tur_list[0].ycor() > 280 or snake.tur_list[0].xcor() < -280 or snake.tur_list[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for segment in snake.tur_list[1:]:
        if snake.tur_list[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
