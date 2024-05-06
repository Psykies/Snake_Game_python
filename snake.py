# creating a class to create a snake body and move the snake
# importing modules
from turtle import Turtle

# make a snake body

# constant for the snake class STARTING POINTS IS FOR FRIST 3 BODY OF SANKE, MOVE DISTANCE IS THE DISTANCE IT COVERS
#UP,DOWN ,RIGHT AND LEFT IS TJE DIRECTION OF NORTH SO
STARTING_POINT = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

body = []


class Snake ():
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for points in STARTING_POINT:
            self.add_body(points)

# function to add a new body part in the list of sanke body
    def add_body(self,points):
        new_body = Turtle("square")
        new_body.color("white")
        new_body.penup()
        new_body.goto(points)
        self.body.append(new_body)

#funtion to extend the sanke body
    def extend(self):
        # add a new body to the sanke
        self.add_body(self.body[-1].position())
# function to move the snake forward
    def move(self):
        for body_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[body_num - 1].xcor()
            new_y = self.body[body_num - 1].ycor()
            self.body[body_num].goto(new_x, new_y)
        self.body[0].forward(MOVE_DISTANCE)

#function to use the arrow button to ove the snake body
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
