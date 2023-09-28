from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
paddle2 = Paddle(350)
paddle1 = Paddle(-350)
ball = Ball()
screen.listen()
screen.onkey(paddle1.move_paddle_up, 'w')
screen.onkey(paddle1.move_paddle_down, 's')
screen.onkey(paddle2.move_paddle_up, 'Up')
screen.onkey(paddle2.move_paddle_down, 'Down')

game_is_on = True

while(game_is_on):
  time.sleep(0.1)
  screen.update()
  ball.move()
  if ball.ycor() >= 280 or ball.ycor() <= -280:
    ball.bounce_y()

  if ball.distance(paddle2) < 50 and ball.xcor() > 320 or ball.distance(paddle1) < 50 and ball.xcor() < -320:
    ball.bounce_x()

  if ball.xcor() > 380:
    ball.reset_position()

  if ball.xcor() < -380:
    ball.reset_position()




screen.exitonclick()