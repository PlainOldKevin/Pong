# Imports
from turtle import Screen
from paddle import Paddle
from ball import Ball

# Create screen and give characteristics
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Initialize elements
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

# Screen listening for key inputs to move paddles
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# Bool to keep updating screen
game_on = True

# Game loop
while game_on:
    screen.update()

# Exit on click
screen.exitonclick()