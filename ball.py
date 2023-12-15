# Imports
from turtle import Turtle

class Ball(Turtle):

    # Init function; setting ball characteristics on creation
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup() # Lifts the pen up so no pen lines will be drawn from center (instantiation point)

    # Movement function
    def move(self):
        new_x = self.xcor() + 1
        new_y = self.ycor() + 1
        self.goto(new_x, new_y)