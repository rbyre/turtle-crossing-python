from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color("black")
    self.up()
    self.hideturtle()
    self.level = 1
    self.update_scoreboard()
    

  def update_scoreboard(self):
    self.goto(-250, 280)
    self.write(f"LEVEL: {self.level}", align="center", font=("Courier", 16, "normal"))

  def game_over(self):
    self.goto(-30, 0)
    self.write(f"GAME OVER!! DU KOM TIL LEVEL: {self.level}", align="center", font=("Courier", 16, "normal"))

  def levelup(self):
    self.clear()
    self.level += 1
    self.update_scoreboard()

  