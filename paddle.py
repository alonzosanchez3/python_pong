from turtle import Turtle

class Paddle(Turtle):
  def __init__(self):
    super().__init__()
    self.height = 100
    self.width = 20