from turtle import Turtle
import random
t =Turtle()
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(1,1)
        self.penup()
        self.movingball()
    def movingball(self):
        y = random.randint(-250, 250)
        x = random.randint(-250, 250)
        self.goto(x,y)