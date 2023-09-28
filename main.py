from turtle import Turtle, Screen
from paddle import Paddle
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
paddle2 = Paddle(350)
paddle1 = Paddle(-350)
screen.listen()
screen.tracer(0)
screen.onkey(paddle1.move_paddle_up, 'w')
screen.onkey(paddle1.move_paddle_down, 's')
screen.onkey(paddle2.move_paddle_up, 'Up')
screen.onkey(paddle2.move_paddle_down, 'Down')

game_is_on = True

while(game_is_on):
  screen.update()
  time.sleep(0.01)

screen.exitonclick()