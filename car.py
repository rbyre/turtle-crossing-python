from turtle import Turtle
import random as r

CAR_COLORS = ['red', 'orange', 'green', 'blue', 'indigo', 'yellow', 'hotpink']
START_X_POS = 280

class Car(Turtle):
  def __init__(self):
    super().__init__()
    car_color = self.random_color()
    self.color(car_color)
    self.shape('square')
    self.shapesize(1, 2)
    self.up()
    self.start_position()
    self.move()
  


  def random_color(self):
    return r.choice(CAR_COLORS)
  
  def start_position(self):
    new_y_pos = r.randint(-250, 280)
    self.goto(START_X_POS, new_y_pos)
    
  def move(self):
    random_x = r.randint(10, 40)
    new_x = self.xcor() - random_x
    self.goto(new_x, self.ycor())

  def reset_pos(self):
    self.goto(START_X_POS, self.ycor())
  
