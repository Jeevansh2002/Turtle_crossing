import time
from turtle import *
from driver import Driver
from cars import Cars
from scorecard import Scorecard

screen = Screen()
cherry_1 = Turtle()
cherry_1.hideturtle()
screen.screensize(canvwidth=600, canvheight=500)
screen.tracer(0)
is_game_on = True
driver = Driver()
cars = Cars()
score = Scorecard()
speed = 0.3
cherry_1.penup()
cherry_1.goto(-240, 249)
cherry_1.write(align="center",font=("courier",10,"normal"),arg="Finishing Line")
screen.listen()
screen.onkey(driver.move_up, key="Up")

while is_game_on:
    time.sleep = 0.1
    screen.update()
    cars.create_car()
    cars.moving(speed)
    score.scoreboard()
    #Finishing line
    if driver.ycor() > 248:
        speed *= 1.5
        cars.moving(speed)
        score.increment()
        driver.goto(0, -240)
    #Detection with turtle
    for i in range(len(cars.vehicles)):
        if cars.vehicles[i].distance(driver) < 26 and cars.vehicles[i].xcor() > -0.5:
            is_game_on = False
            cherry_1.color("black")
            cherry_1.goto(0,0)
            cherry_1.write(align="center", font=("courier",30,"normal"),arg="Game Over!")




exitonclick()
