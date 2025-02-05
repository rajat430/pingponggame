from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position,shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.setposition(position)
        self.color("white")
        self.shape("square")
        self.shapesize(8,2)
    
    def up(self):
        self.setposition(self.xcor(),self.ycor()+20)
    def down(self):
        self.setposition(self.xcor(),self.ycor()-20)



