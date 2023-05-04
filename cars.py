from turtle import Turtle
import random
MOVING_DISTANCE = 5
COLOR = ["blue", "yellow", "pink", "black", "red", "orange", "purple"]


class Cars(Turtle):
    def __init__(self):
        super(). __init__()
        self.vehicles = []

    def create_car(self):
        random_choice = random.randint(1,70)  #Nice technique🙂
        if random_choice == 3:
            position_y = random.randint(-210, 230)
            cherry = Turtle()
            cherry.penup()
            cherry.shape("square")
            cherry.shapesize(stretch_len=2, stretch_wid=1)
            random_color = random.choice(COLOR)
            cherry.color(random_color)
            cherry.goto(300, position_y)
            self.vehicles.append(cherry)
            self.hideturtle()

    def moving(self,speed):
        for car in self.vehicles:
            car.back(speed)










