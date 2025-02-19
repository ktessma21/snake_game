from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Initialize screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Initialize snake and food
snake = Snake()
food = Food()
scoreboard = Scoreboard()
# Set up key bindings
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game loop
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.07)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 25:
        food.refresh()
        snake.extend()
        scoreboard.increment_score()
    
    # Detect collision with wall
    if snake.is_wall_collision() or snake.is_running_over_itself():
        scoreboard.game_over()
        snake.reset()


screen.exitonclick()
