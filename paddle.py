# Imports
from turtle import Turtle

class Paddle(Turtle):

    # Init function; setting paddle characteristics on creation
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1) # Multiplies turtle size by w,l respectively (turtle starts at 20x20, so w x 5 = 100 and l x 1 = 20)
        self.penup() # Lifts the pen up so no pen lines will be drawn from center (instantiation point)
        self.goto(position)

    # Function to move paddle up
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # Function to move paddle down
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)