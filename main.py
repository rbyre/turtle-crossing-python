from turtle import Screen
import time
from car import Car
from player_turtle import Playerturtle
from scoreboard import Scoreboard


LEVEL = 1
CURRENT_CARS = []


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

scoreboard = Scoreboard()

player1 = Playerturtle()


screen.listen() 
screen.onkey(player1.move_up, "Up")
screen.onkey(player1.move_down, "Down")


game_on = True
level_complete = False
CURRENT_CARS.append(Car())

while game_on:

  time.sleep(0.1)

  
  if level_complete:
    player1.reset_pos()
    CURRENT_CARS.append(Car())
    LEVEL += 1
    scoreboard.levelup()
    level_complete = not level_complete
    


  for car in CURRENT_CARS:
    if car.distance(player1) <= 20:
      # player1.gothit()
      scoreboard.game_over()
      game_on = False

    if car.xcor() > -300:
      car.move()
    else: 
      car.reset_pos()
    
    if player1.ycor() > 280:
      level_complete = True

  screen.update()




screen.exitonclick()