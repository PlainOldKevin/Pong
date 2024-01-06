# Imports
from turtle import Turtle

class Scoreboard(Turtle):

    # Init function; setting scoreboard characteristics on creation
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup() # Lifts the pen up so no pen lines will be drawn from center (instantiation point)
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    # Function to update scoreboard
    def update(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.l_score, align="center", font=("Courier", 80, "bold"))
        self.goto(100, 190)
        self.write(self.r_score, align="center", font=("Courier", 80, "bold"))

    # Add point to left player
    def l_point(self):
        self.l_score += 1
        self.update()

    # Add point to right player
    def r_point(self):
        self.r_score += 1
        self.update()