import random
from turtle import Turtle
POSITIVESLOPE=[i/10 for i in range(1,10)]
NEGATIVESLOPE=[i/10 for i in range(-1,-10,-1)]
class Ball(Turtle):
    init_x=0
    init_y=0
    m=0
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.shapesize(.5,.5)
        self.shape("circle")
        self.color("blue")
        self.setposition(0,0)
    
    def inital_move(self,p1,p2):
        if(Ball.m==0):
            Ball.m=random.choice(POSITIVESLOPE + NEGATIVESLOPE)
        Ball.init_y=int(Ball.m*Ball.init_x)
        self.setposition(Ball.init_x,Ball.init_y)
        print(f"x={self.xcor()},y={self.ycor()}) and m={Ball.m}")
        Ball.init_x=Ball.init_x+10
        print(f"p1 -- {self.distance(p1)}")
        print(f"p2 -- {self.distance(p2)}")
        if(self.collision(p1) == 1):
            print("entering 1")
            Ball.m=random.choice(POSITIVESLOPE )
            Ball.init_y=int(Ball.m*Ball.init_x)
            self.setposition(Ball.init_x,Ball.init_y)
            print(f"x={self.xcor()},y={self.ycor()}) and m={Ball.m}")
            Ball.init_x=Ball.init_x+10
        elif(self.collision(p2) == 1):
            print("entering 2")
            Ball.m=random.choice(POSITIVESLOPE)
            Ball.init_x=Ball.init_x-10
            Ball.init_y=int(Ball.m*Ball.init_x)
            self.setposition(Ball.init_x,Ball.init_y)
            Ball.init_x=Ball.init_x-10
        else:
            pass
        print(f"Location of Ball: {self.position()}")
        print(f"Location of P1: {p1.position()}")
        print(f"Location of P2: {p1.position()}")

    def collision(self,p):
        if(self.distance(p)<30):
            return 1
        else:
            return 0



        