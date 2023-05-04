from turtle import Turtle

class Driver(Turtle):
    def __init__(self):
        super(). __init__()
        self.pos = 10
        self.color("black")
        self.penup()
        self.shape("turtle")
        self.shapesize(stretch_wid=0.91, stretch_len=0.97)
        self.goto(0,-245)
        self.left(90)


    def move_up(self):
       self.fd(10)      #We can use both methods to make our car move🚘


