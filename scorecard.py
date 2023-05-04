from turtle import Turtle

class Scorecard(Turtle):
    def __init__(self):
        super(). __init__()
        self.level = 0
    def scoreboard(self):
        self.color("red")
        self.clear()
        self.penup()
        self.goto(0, 235)
        self.write(align="center",font=("courier",20,"normal",),arg=f"LEVEL: {self.level}")
        self.hideturtle()

    def increment(self):
        self.level += 1

