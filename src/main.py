import time
import Paddle
import Ball
from turtle import Screen
s1=Screen()
s1.screensize(400,400)
s1.bgcolor("black")
p1=Paddle.Paddle((-300,0))
p2=Paddle.Paddle((300,0))
is_game_on=True
s1.listen()
ball=Ball.Ball()

while(is_game_on):
    s1.update()
    s1.onkey(key="Up",fun=p2.up)
    s1.onkey(key="Down",fun=p2.down)
    s1.onkey(key="w",fun=p1.up)
    s1.onkey(key="s",fun=p1.down)
    time.sleep(.2)
    ball.inital_move(p1,p2)
    time.sleep(.3)
    
    

















s1.exitonclick()
