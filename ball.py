# Imports
from turtle import Turtle

class Ball(Turtle):

    # Init function; setting ball characteristics on creation
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup() # Lifts the pen up so no pen lines will be drawn from center (instantiation point)
        self.x_move = 10
        self.y_move = 10

    # Movement function
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1