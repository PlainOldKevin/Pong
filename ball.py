# Imports
from turtle import Turtle

class Ball(Turtle):

    # Init function; setting ball characteristics on creation
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup() # Lifts the pen up so no pen lines will be drawn from center (instantiation point)