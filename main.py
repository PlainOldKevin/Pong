# Imports
from turtle import Screen
from paddle import Paddle

# Create screen and give characteristics
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Initialize Paddle,
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_on = True

while game_on:
    screen.update()

# Exit on click
screen.exitonclick()