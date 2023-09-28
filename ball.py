from turtle import Turtle

class Ball(Turtle):

  def __init__(self):
    super().__init__()
    self.shape('square')
    self.color('white')
    self.penup()
    self.goto(-300, -270)
    self.x_move = 10
    self.y_move = 10

  def move(self):
    x = self.xcor()
    y = self.ycor()
    self.setpos(x + self.x_move, y + self.y_move)


  def bounce(self):
    self.y_move *= -1



