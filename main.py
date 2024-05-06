# importing modules
from turtle import Screen
import time
from snake import Snake
from Food import Food
from Scoreboard import Scoreboard

# creating the screen board
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_point = [(0, 0), (-20, 0), (-40, 0)]

body = []

# here each function need to make this a snake game is brought from different class
# where each class have certain function like snake has body increase, move
# food has its methods where it can produce the food
# score board keeps the score

# different class are being called upon
snake = Snake()
food = Food()
score = Scoreboard()

# Setup input handling and event listener
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    # move the snake

    snake.move()

    # detect collision with food and generate new food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # detect collision with its tail
    for segment in snake.body:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
