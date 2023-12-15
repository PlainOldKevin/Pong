# Imports
from turtle import Screen
from paddle import Paddle

# Create screen and give characteristics
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Initialize Paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

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