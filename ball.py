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


  def bounce_y(self):
    self.y_move *= -1

  def bounce_x(self):
    self.x_move *= -1

  def reset_position(self):
    self.goto(0,0)
    self.bounce_x()



