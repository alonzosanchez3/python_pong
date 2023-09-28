from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, x):
    super().__init__()
    self.shape('square')
    self.x = x
    self.shapesize(stretch_wid=5, stretch_len=1)

    self.penup()
    self.color('white')
    self.goto(self.x, 0)
    # self.listen()
    # self.onkey(self.move_paddle_up, 'w')
    # self.onkey(self.move_paddle_down, 's')


  def move_paddle_up(self):

    current_y = self.ycor()
    self.setpos(self.x, current_y + 20)

  def move_paddle_down(self):
    current_y = self.ycor()
    self.setpos(self.x, current_y - 20)
