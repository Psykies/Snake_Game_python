from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        # defining the body of the food
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("orange")
        self.speed("fastest")
        self.refresh()

    # generating the food for the snake at random location
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
