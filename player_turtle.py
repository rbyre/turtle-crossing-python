from turtle import Turtle


class Playerturtle(Turtle):
  def __init__(self):
    super().__init__()
    self.shape('turtle')
    self.up()
    self.goto(0, -280)
    self.y_move = 20
    self.setheading(90)

  def move_up(self):
    new_y = self.ycor() + self.y_move
    self.goto(self.xcor(), new_y)

  def move_down(self):
    new_y = self.ycor() - self.y_move
    self.goto(self.xcor(), new_y)

  def gothit(self):
    self.reset_pos()

  def reset_pos(self):
    self.goto(0, -280)