from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=900, height=600)
screen.title("Luka Shekelashvilis's Pong Game")
screen.tracer(0)


r_paddle = Paddle((435, 0))
l_paddle = Paddle((-435, 0))
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

while game_is_on: 
      time.sleep(0.08)
      screen.update()
      ball.move()

      if ball.ycor() > 280 or ball.ycor() < -280:
         ball.bounce_y()
    
      if ball.distance(r_paddle) < 35 and ball.xcor() > 320 or ball.distance(l_paddle) < 35 and ball.xcor() < -320:
          ball.bounce_x()

      if ball.xcor() < -440: 
         ball.reset()
         scoreboard.r_point()
      
      elif ball.xcor() > 430:
           ball.reset()
           scoreboard.l_point()



screen.exitonclick()

